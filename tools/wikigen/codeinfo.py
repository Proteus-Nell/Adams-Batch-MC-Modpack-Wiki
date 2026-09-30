"""Small code-derived facts about items, effects, entities and commands."""
from __future__ import annotations

import re
from typing import Optional

from .javaindex import JavaIndex, JClass, text, walk, call_args, InstanceOf, EnumConst
from .registry import Reg

VANILLA_ITEM_BASES = {
    "SwordItem": "Weapons", "AxeItem": "Tools", "PickaxeItem": "Tools", "ShovelItem": "Tools", "HoeItem": "Tools",
    "DiggerItem": "Tools", "TieredItem": "Tools", "ArmorItem": "Armor", "ElytraItem": "Armor", "ShieldItem": "Weapons",
    "BowItem": "Weapons", "CrossbowItem": "Weapons", "TridentItem": "Weapons", "ProjectileWeaponItem": "Weapons",
    "SpawnEggItem": "Spawn Eggs", "DeferredSpawnEggItem": "Spawn Eggs", "BlockItem": "Blocks", "BucketItem": "Buckets",
    "RecordItem": "Music Discs", "PotionItem": "Potions", "MaceItem": "Weapons", "FishingRodItem": "Tools",
    "SmithingTemplateItem": "Smithing Templates", "BannerPatternItem": "Banner Patterns", "HorseArmorItem": "Armor",
    "AnimalArmorItem": "Armor", "ICurioItem": "Curios", "RelicItem": "Relics",
}

NAME_HINTS = [
    (r"_(sword|katana|kodachi|odachi|long_sword|great_sword|tachi|spear|scythe|dagger|axe_weapon|bow|crossbow|hammer|mace|gauntlet|staff|wand|blade|lance|rapier|halberd|trident|sickle|whip)$", "Weapons"),
    (r"_(helmet|chestplate|leggings|boots|mask|hood|robe|cape|cloak|armor)$", "Armor"),
    (r"_(pickaxe|shovel|hoe|axe|paxel|shears|hammer_tool)$", "Tools"),
    (r"_spawn_egg$", "Spawn Eggs"),
    (r"(^|_)(ingot|nugget|gem|dust|shard|scale|fang|horn|hide|leather|claw|crystal|ore|core|essence|fragment|scrap|bone|feather|string|web|stone)s?$", "Materials"),
    (r"_(schematic|blueprint)$", "Schematics"),
    (r"^music_disc_|_disc$", "Music Discs"),
    (r"_(bucket)$", "Buckets"),
    (r"(_potion|_elixir|_tonic|_bottle)$", "Potions"),
    (r"_(scroll|tome|book|manual|grimoire)$", "Books & Scrolls"),
    (r"(_ring|_amulet|_charm|_necklace|_bracelet|_belt|_gloves|_glove|_talisman|_pendant)$", "Accessories"),
]


def item_category(ix: JavaIndex, reg: Optional[Reg], path: str, pkg_hint: Optional[str] = None) -> str:
    if reg is not None and reg.cls and reg.cls in ix.classes:
        c = ix.classes[reg.cls]
        for a in [c.simple] + [x.rsplit(".", 1)[-1] for x in ix.ancestors(c)]:
            if a in VANILLA_ITEM_BASES:
                return VANILLA_ITEM_BASES[a]
    elif reg is not None and reg.cls:
        simple = reg.cls.rsplit(".", 1)[-1]
        if simple in VANILLA_ITEM_BASES:
            return VANILLA_ITEM_BASES[simple]
    if reg is not None and re.search(r"\.food\(|\bFoodProperties\b|Foods\.", text(reg.node)):
        return "Food"
    for pat, cat in NAME_HINTS:
        if re.search(pat, path):
            return cat
    return "Miscellaneous"


def item_properties(ix: JavaIndex, reg: Reg) -> dict:
    """Stack size, durability, rarity etc. from the Item.Properties chain at registration."""
    props = {}
    nodes = [reg.node]
    # properties may be built inside the item constructor too
    if reg.cls and reg.cls in ix.classes:
        for m in ix.classes[reg.cls].methods.get("<init>", []):
            nodes.append(m.node)
    for root in nodes:
        for n in walk(root):
            if n.type != "method_invocation":
                continue
            name = text(n.child_by_field_name("name"))
            a = call_args(n)
            if name == "stacksTo" and a:
                v = ix.try_eval(a[0], reg.ctx)
                if isinstance(v, int):
                    props["stack"] = v
            elif name == "durability" and a:
                v = ix.try_eval(a[0], reg.ctx)
                if isinstance(v, int):
                    props["durability"] = v
            elif name == "rarity" and a:
                m = re.search(r"Rarity\.([A-Z_]+)", text(a[0]))
                if m:
                    props["rarity"] = m.group(1).title()
            elif name == "fireResistant":
                props["fire_resistant"] = True
            elif name == "food" and a:
                props["food"] = True
    return props


def tooltip_lines(ix: JavaIndex, cls: Optional[JClass], has_key, tr) -> list:
    """Tooltip text from appendHoverText: every call whose argument is a lang key.

    Arguments after the key (except ChatFormatting/Style) fill the %s placeholders,
    using config defaults where the code reads a config value.
    """
    out = []
    c = cls
    depth = 0
    while c is not None and depth < 6:
        for mname in ("appendHoverText", "addInformation", "appendTooltip"):
            m = c.method(mname)
            if m is None:
                continue
            for n in walk(m.node):
                if n.type != "method_invocation":
                    continue
                a = call_args(n)
                for i, arg in enumerate(a):
                    if arg.type not in ("string_literal", "identifier", "field_access", "binary_expression"):
                        continue
                    k = ix.try_eval(arg, c)
                    if not isinstance(k, str) or not has_key(k):
                        continue
                    if k.endswith("_alt") and has_key(k[:-4]):
                        break
                    vals = []
                    for extra in a[i + 1:]:
                        et = text(extra)
                        if et.startswith("ChatFormatting") or "Style" in et or et.startswith("TextColor"):
                            continue
                        v = ix.try_eval(extra, c, ix.locals_env(extra, c))
                        if isinstance(v, float) and v == int(v):
                            v = int(v)
                        vals.append(v if v is not None and not isinstance(v, InstanceOf) else "?")
                    line = _fill_placeholders(tr(k), vals)
                    if line and line not in out:
                        out.append(line)
                    break
        c = ix.resolve(c.superclass, c) if c.superclass else None
        depth += 1
    return out


def _fill_placeholders(t, vals):
    if t is None:
        return None
    i = 0

    def rep(mm):
        nonlocal i
        idx = mm.group(1)
        j = int(idx) - 1 if idx else i
        if not idx:
            i += 1
        return str(vals[j]) if j < len(vals) else "?"

    return re.sub(r"%(?:(\d+)\$)?[sd]", rep, t).replace("%%", "%")


def effect_info(ix: JavaIndex, reg: Reg) -> dict:
    info = {}
    srcs = [text(reg.node)]
    c = ix.classes.get(reg.cls) if reg.cls else None
    depth = 0
    while c is not None and depth < 5:
        for m in c.methods.get("<init>", []):
            srcs.append(m.src)
        c = ix.resolve(c.superclass, c) if c.superclass else None
        depth += 1
    for s in srcs:
        m = re.search(r"MobEffectCategory\.([A-Z]+)", s)
        if m and "category" not in info:
            info["category"] = m.group(1).title()
        m = re.search(r"MobEffectCategory\.[A-Z]+\s*,\s*(-?\d+|0x[0-9A-Fa-f]+)", s)
        if m and "color" not in info:
            try:
                v = int(m.group(1), 0) & 0xFFFFFF
                info["color"] = "#%06X" % v
            except ValueError:
                pass
    attrs = []
    for s in srcs:
        for m in re.finditer(r"addAttributeModifier\(\s*([A-Za-z_.]+)\s*,[^,]+,\s*(-?[\d.]+)[FfDd]?\s*,\s*(?:AttributeModifier\.)?(?:Operation\.)?([A-Z_]+)", s):
            attrs.append({"attribute": m.group(1).split(".")[-1].replace("_", " ").title(), "amount": m.group(2), "operation": m.group(3)})
    if attrs:
        info["attributes"] = attrs
    return info


ATTR_NAMES = {
    "MAX_HEALTH": "Health", "ATTACK_DAMAGE": "Attack damage", "ARMOR": "Armor", "ARMOR_TOUGHNESS": "Armor toughness",
    "MOVEMENT_SPEED": "Speed", "FOLLOW_RANGE": "Follow range", "KNOCKBACK_RESISTANCE": "Knockback resistance",
    "ATTACK_KNOCKBACK": "Attack knockback", "FLYING_SPEED": "Flying speed", "ATTACK_SPEED": "Attack speed",
    "STEP_HEIGHT": "Step height", "SCALE": "Scale", "GRAVITY": "Gravity", "SAFE_FALL_DISTANCE": "Safe fall distance",
}


def entity_attributes(ix: JavaIndex, cls: JClass, depth=0) -> dict:
    """Walk createAttributes()-style static builders, following super-builders."""
    if cls is None or depth > 6:
        return {}
    cand = None
    for name in ("createAttributes", "setAttributes", "createMobAttributes", "getAttributes", "attributes", "createAttributeMap", "prepareAttributes"):
        m = cls.method(name)
        if m is not None and "static" in text(m.node).split("(")[0]:
            cand = m
            break
    if cand is None:
        for ms in cls.methods.values():
            for m in ms:
                head = text(m.node).split("{")[0]
                if "static" in head and "AttributeSupplier" in head:
                    cand = m
                    break
            if cand:
                break
    if cand is None:
        sup = ix.resolve(cls.superclass, cls) if cls.superclass else None
        return entity_attributes(ix, sup, depth + 1) if sup is not None else {}
    out = {}
    # follow a parent builder call like Monster.createMonsterAttributes() / Parent.createAttributes()
    for n in walk(cand.node):
        if n.type == "method_invocation":
            nm = text(n.child_by_field_name("name"))
            obj = n.child_by_field_name("object")
            if nm.startswith("create") and obj is not None and obj.type == "identifier":
                oc = ix.resolve(text(obj), cls)
                if oc is not None and oc is not cls:
                    out.update(entity_attributes(ix, oc, depth + 1))
    for n in walk(cand.node):
        if n.type == "method_invocation" and text(n.child_by_field_name("name")) == "add":
            a = call_args(n)
            if len(a) >= 1:
                an = text(a[0]).split(".")[-1]
                if len(a) >= 2:
                    v = ix.try_eval(a[1], cls)
                    val = v if isinstance(v, (int, float)) else text(a[1])
                else:
                    val = "default"
                label = ATTR_NAMES.get(an, an.replace("_", " ").title())
                out[label] = val
    return out


def entity_class_info(ix: JavaIndex, cls) -> dict:
    """Class-only facts, for entities registered in ways we can't read the builder of."""
    info = {}
    if cls is None:
        return info
    info["class"] = cls.fqcn
    anc = [a.rsplit(".", 1)[-1] for a in ix.ancestors(cls)]
    info["living"] = any(a in LIVING_BASES for a in anc) or "createAttributes" in cls.src
    info["boss"] = "ServerBossEvent" in cls.src or "BossEvent" in cls.src or any("Boss" in a for a in anc)
    info["attributes"] = entity_attributes(ix, cls)
    info["ancestors"] = anc[:6]
    return info


LIVING_BASES = ("LivingEntity", "Mob", "PathfinderMob", "Monster", "Animal", "TamableAnimal", "AgeableMob", "WaterAnimal",
                "FlyingMob", "AbstractGolem", "Villager", "AbstractVillager")


def entity_type_info(ix: JavaIndex, reg: Reg) -> dict:
    s = text(reg.node)
    info = {}
    m = re.search(r"MobCategory\.([A-Z_]+)", s)
    if m:
        info["category"] = m.group(1).title()
    m = re.search(r"\.sized\(\s*([\d.]+)F?\s*,\s*([\d.]+)F?", s)
    if m:
        info["size"] = [float(m.group(1)), float(m.group(2))]
    if ".fireImmune()" in s:
        info["fire_immune"] = True
    m = re.search(r"(\w+)::new", s)
    cls = None
    if m:
        cls = ix.resolve(m.group(1), reg.ctx)
    if cls is None and reg.cls:
        cls = ix.classes.get(reg.cls)
    if cls is not None:
        info["class"] = cls.fqcn
        anc = [a.rsplit(".", 1)[-1] for a in ix.ancestors(cls)]
        info["living"] = any(a in ("LivingEntity", "Mob", "PathfinderMob", "Monster", "Animal", "TamableAnimal", "AgeableMob", "WaterAnimal", "FlyingMob", "AbstractGolem", "Villager", "AbstractVillager") for a in anc) or "createAttributes" in cls.src \
            or info.get("category") not in (None, "Misc")
        info["boss"] = "ServerBossEvent" in cls.src or "BossEvent" in cls.src or any("Boss" in a for a in anc)
        info["attributes"] = entity_attributes(ix, cls)
        info["ancestors"] = anc[:6]
    return info


# ------------------------------------------------------------------ commands
def commands(ix: JavaIndex, mod_keys: set) -> list:
    """Flattened command syntaxes: [{syntax, permission, source}]"""
    out = []
    for cls in ix.classes.values():
        if cls.mod not in mod_keys:
            continue
        for ms in cls.methods.values():
            for m in ms:
                if ".register(" not in m.src or "ispatcher" not in m.src:
                    continue
                for n in walk(m.node):
                    if n.type == "method_invocation" and text(n.child_by_field_name("name")) == "register":
                        obj = text(n.child_by_field_name("object"))
                        if "dispatcher" not in obj.lower() and "Dispatcher" not in obj:
                            continue
                        a = call_args(n)
                        if not a:
                            continue
                        env = _locals(m)
                        for path, perm in _cmd_paths(ix, a[0], cls, env, 0):
                            if path and path[0].startswith("<"):
                                continue
                            out.append({"syntax": "/" + " ".join(path), "permission": perm, "source": cls.fqcn})
    uniq = {}
    for c in out:
        uniq.setdefault(c["syntax"], c)
    return sorted(uniq.values(), key=lambda c: c["syntax"])


def _locals(m):
    env = {}
    for n in walk(m.node):
        if n.type == "local_variable_declaration":
            for d in n.named_children:
                if d.type == "variable_declarator" and d.child_by_field_name("value") is not None:
                    env[text(d.child_by_field_name("name"))] = d.child_by_field_name("value")
    return env


def _cmd_paths(ix, node, ctx, env, depth):
    """Yield ([tokens], permission) for each executable path under a builder expression."""
    if node is None or depth > 14:
        return
    if node.type == "identifier" and text(node) in env:
        yield from _cmd_paths(ix, env[text(node)], ctx, env, depth + 1)
        return
    while node is not None and node.type in ("parenthesized_expression", "cast_expression"):
        node = node.child_by_field_name("value") if node.type == "cast_expression" else (node.named_children[0] if node.named_children else None)
    if node is None or node.type != "method_invocation":
        return
    # flatten chain (casts and parentheses are common in decompiled builders)
    calls = []
    cur = node
    while cur is not None:
        if cur.type == "method_invocation":
            calls.append(cur)
            cur = cur.child_by_field_name("object")
        elif cur.type == "cast_expression":
            cur = cur.child_by_field_name("value")
        elif cur.type == "parenthesized_expression":
            cur = cur.named_children[0] if cur.named_children else None
        else:
            break
    calls.reverse()
    if not calls:
        return
    head = calls[0]
    hname = text(head.child_by_field_name("name"))
    ha = call_args(head)
    token = None
    if hname == "literal" and ha:
        v = ix.try_eval(ha[0], ctx)
        token = v if isinstance(v, str) else "<%s>" % text(ha[0])
    elif hname == "argument" and ha:
        v = ix.try_eval(ha[0], ctx)
        token = "<%s>" % (v if isinstance(v, str) else text(ha[0]))
    else:
        # a helper returning a builder
        target = _resolve_call(ix, head, ctx)
        if target is not None:
            m, c = target
            for r in m.returns():
                yield from _cmd_paths(ix, r, c, _locals(m), depth + 1)
        return
    perm = None
    children = []
    executes = False
    for c in calls[1:]:
        nm = text(c.child_by_field_name("name"))
        a = call_args(c)
        if nm == "then" and a:
            children.append(a[0])
        elif nm == "executes":
            executes = True
        elif nm == "requires" and a:
            mm = re.search(r"hasPermission\((\d)\)", text(a[0]))
            if mm:
                perm = int(mm.group(1))
            elif "hasPermission" in text(a[0]) or "permission" in text(a[0]).lower():
                perm = perm or 2
    if executes:
        yield [token], perm
    for ch in children:
        for sub, p in _cmd_paths(ix, ch, ctx, env, depth + 1):
            yield [token] + sub, (p if p is not None else perm)


def _resolve_call(ix, inv, ctx):
    name = text(inv.child_by_field_name("name"))
    obj = inv.child_by_field_name("object")
    owner = ctx
    if obj is not None:
        oc = ix.resolve(text(obj), ctx)
        if oc is None:
            return None
        owner = oc
    for m in owner.methods.get(name, []):
        return m, owner
    return None


# ------------------------------------------------- ManasCore annotation commands
PERM_LEVELS = {"PLAYER": 0, "MODERATOR": 1, "GAMEMASTER": 2, "ADMIN": 3, "OWNER": 4}


def _annotations(node) -> dict:
    """{name: {arg: node}} for the annotations on a class/method/parameter node."""
    out = {}
    for c in node.children:
        if c.type != "modifiers":
            continue
        for a in c.children:
            if a.type not in ("annotation", "marker_annotation"):
                continue
            name = text(a.child_by_field_name("name"))
            args = {}
            al = a.child_by_field_name("arguments")
            if al is not None:
                for p in al.named_children:
                    if p.type == "element_value_pair":
                        args[text(p.child_by_field_name("key"))] = p.child_by_field_name("value")
                    else:
                        args["value"] = p
            out[name] = args
    return out


def annotation_commands(ix: JavaIndex, mod_keys: set) -> list:
    roots = []
    for cls in ix.classes.values():
        if cls.mod not in mod_keys:
            continue
        for ms in cls.methods.values():
            for m in ms:
                if "registerCommand(" not in m.src:
                    continue
                for n in walk(m.node):
                    if n.type == "method_invocation" and text(n.child_by_field_name("name")) == "registerCommand":
                        for a in call_args(n):
                            t = text(a)
                            if t.endswith(".class"):
                                rc = ix.resolve(t[:-6], cls)
                                if rc is not None:
                                    roots.append(rc)
    out = []
    seen = set()

    def visit(c, prefix, perm, depth):
        if depth > 8 or c.fqcn in seen and depth == 0:
            return
        ann = _annotations(c.node)
        cmd = ann.get("Command")
        if cmd is None:
            return
        names = []
        v = cmd.get("value")
        if v is not None:
            ev = ix.try_eval(v, c)
            if isinstance(ev, list):
                names = [str(x) for x in ev]
            elif isinstance(ev, str):
                names = [ev]
            elif v.type == "element_value_array_initializer":
                names = [ix.try_eval(x, c) for x in v.named_children]
        if not names:
            return
        p = ann.get("Permission")
        if p is not None and "permissionLevel" in p:
            lvl = text(p["permissionLevel"]).split(".")[-1]
            perm = PERM_LEVELS.get(lvl, perm)
        for name in names[:1]:
            path = prefix + [name]
            for ms in c.methods.values():
                for m in ms:
                    mann = _annotations(m.node)
                    if "Execute" not in mann:
                        continue
                    mperm = perm
                    mp = mann.get("Permission")
                    if mp is not None and "permissionLevel" in mp:
                        mperm = PERM_LEVELS.get(text(mp["permissionLevel"]).split(".")[-1], mperm)
                    toks = []
                    fp = m.node.child_by_field_name("parameters")
                    for par in (fp.named_children if fp is not None else []):
                        pann = _annotations(par)
                        if "SenderArg" in pann or not pann:
                            continue
                        an, args = next(iter(pann.items()))
                        if an == "LiteralArg":
                            lv = ix.try_eval(args.get("value"), c) if args.get("value") is not None else None
                            toks.append(str(lv) if lv else text(par.child_by_field_name("name")))
                        else:
                            lv = ix.try_eval(args.get("value"), c) if args.get("value") is not None else None
                            label = lv if isinstance(lv, str) else text(par.child_by_field_name("name"))
                            opt = "Optional" in an or "Nullable" in text(par)
                            toks.append(("[%s]" if opt else "<%s>") % label)
                    out.append({"syntax": "/" + " ".join(path + toks), "permission": mperm, "source": c.fqcn})
            subs = cmd.get("subCommands")
            if subs is not None:
                for sn in walk(subs):
                    if sn.type == "class_literal":
                        sc = ix.resolve(text(sn)[:-6], c)
                        if sc is not None:
                            visit(sc, path, perm, depth + 1)

    for r in roots:
        visit(r, [], 0, 0)
        seen.add(r.fqcn)
    uniq = {}
    for c in out:
        uniq.setdefault(c["syntax"], c)
    return sorted(uniq.values(), key=lambda c: c["syntax"])


# ------------------------------------------------------------------ game rules
def gamerules(ix: JavaIndex, mod_keys: set, res=None) -> list:
    """GameRules.register("name", Category.X, BooleanValue.create(true)) calls."""
    out = []
    for cls in ix.classes.values():
        if cls.mod not in mod_keys or "GameRules.register" not in cls.src:
            continue
        for n in walk(cls.node):
            if n.type != "method_invocation" or text(n.child_by_field_name("name")) != "register":
                continue
            if text(n.child_by_field_name("object")) not in ("GameRules",):
                continue
            a = call_args(n)
            if len(a) < 3:
                continue
            name = ix.try_eval(a[0], cls)
            if not isinstance(name, str):
                continue
            vt = text(a[2])
            kind = "boolean" if "BooleanValue" in vt else "integer" if "IntegerValue" in vt else "other"
            default = None
            for m in walk(a[2]):
                if m.type == "method_invocation" and text(m.child_by_field_name("name")) == "create":
                    ca = call_args(m)
                    if ca:
                        default = ix.try_eval(ca[0], cls)
                    break
            desc = None
            if res is not None:
                for k in ("gamerule." + name, "gamerule.%s.description" % name):
                    if res.has(k) and k.endswith("description"):
                        desc = res.tr(k)
                title = res.tr("gamerule." + name)
            else:
                title = None
            out.append({"name": name, "type": kind, "default": default, "category": text(a[1]).split(".")[-1],
                        "title": title, "description": desc})
    uniq = {}
    for g in out:
        uniq.setdefault(g["name"], g)
    return sorted(uniq.values(), key=lambda g: g["name"].lower())


# vanilla MobEffects constants whose registry id differs from the lower-cased name
VANILLA_EFFECT_IDS = {
    "MOVEMENT_SPEED": "speed", "MOVEMENT_SLOWDOWN": "slowness", "DIG_SPEED": "haste", "DIG_SLOWDOWN": "mining_fatigue",
    "DAMAGE_BOOST": "strength", "HEAL": "instant_health", "HARM": "instant_damage", "JUMP": "jump_boost",
    "CONFUSION": "nausea", "DAMAGE_RESISTANCE": "resistance",
}


def _food_node(ix: JavaIndex, reg: Reg):
    """The FoodProperties builder chain an item uses: `.food(X)` or a FoodProperties constant passed to the item."""
    roots = [(reg.node, reg.ctx)]
    c = ix.classes.get(reg.cls) if reg.cls else None
    depth = 0
    while c is not None and depth < 4:
        for m in c.methods.get("<init>", []):
            roots.append((m.node, c))
        for mn in ("getFoodProperties",):
            for m in c.methods.get(mn, []):
                roots.append((m.node, c))
        c = ix.resolve(c.superclass, c) if c.superclass else None
        depth += 1
    for root, ctx in roots:
        for n in walk(root):
            if n.type == "method_invocation" and text(n.child_by_field_name("name")) in ("nutrition", "saturationModifier"):
                # an inline builder: climb to the top of the chain
                top = n
                while top.parent is not None and top.parent.type == "method_invocation":
                    top = top.parent
                return top, ctx
            ff = None
            if n.type == "identifier" and n.parent is not None and n.parent.type == "argument_list" \
                    and n.parent.parent is not None and text(n.parent.parent.child_by_field_name("name")) == "food":
                # .food(PROPERTIES) with a constant of the item class
                ff = ix.find_field(ctx, text(n))
            if n.type == "field_access":
                oc = ix.resolve(text(n.child_by_field_name("object")), ctx)
                ff = ix.find_field(oc, text(n.child_by_field_name("field"))) if oc is not None else None
            if ff is not None:
                if ff is not None and ff.value is not None and "FoodProperties" in (ff.type or "") + text(ff.value)[:80]:
                    val = ff.value
                    if val.type == "method_invocation" and val.child_by_field_name("object") is None and not call_args(val):
                        # LIFE_ESSENCE = createEssenceProperties();
                        fm = ff.cls.method(text(val.child_by_field_name("name")))
                        rets = fm.returns() if fm is not None else []
                        val = rets[0] if rets else val
                    if re.search(r"nutrition|\.effect\(|alwaysEdible", text(val)):
                        return val, ff.cls
    return None, None


def food_facts(ix: JavaIndex, reg: Reg, effect_ids: dict) -> dict:
    """nutrition, saturation, always edible, eat effects: {"nutrition": 4, "saturation": 1.2, "effects": [...]}.

    effect_ids maps "owner.fqcn.FIELD" to a registry id for mod effects."""
    node, ctx = _food_node(ix, reg)
    if node is None:
        return {}
    out = {}
    effects = []
    for n in walk(node):
        if n.type != "method_invocation":
            continue
        name = text(n.child_by_field_name("name"))
        a = call_args(n)
        if name == "nutrition" and a:
            v = ix.try_eval(a[0], ctx)
            if isinstance(v, (int, float)):
                out["nutrition"] = v
        elif name == "saturationModifier" and a:
            v = ix.try_eval(a[0], ctx)
            if isinstance(v, (int, float)):
                out["saturation"] = round(float(v), 3)
        elif name == "alwaysEdible":
            out["always_edible"] = True
        elif name == "fast":
            out["fast"] = True
        elif name == "effect" and a:
            inst = next((x for x in walk(a[0]) if x.type == "object_creation_expression" and "MobEffectInstance" in text(x.child_by_field_name("type"))), None)
            if inst is None:
                continue
            ia = call_args(inst)
            if not ia:
                continue
            consts = re.findall(r"([A-Za-z_][\w.]*?)\.([A-Z][A-Z0-9_]+)\b", text(ia[0]))
            eid = None
            if consts:
                owner, const = consts[-1]
                if owner.rsplit(".", 1)[-1] == "MobEffects":
                    eid = "minecraft:" + VANILLA_EFFECT_IDS.get(const, const.lower())
                else:
                    oc = ix.resolve(owner, ctx)
                    eid = effect_ids.get("%s.%s" % (oc.fqcn if oc is not None else owner, const))
            dur = ix.try_eval(ia[1], ctx) if len(ia) > 1 else None
            amp = ix.try_eval(ia[2], ctx) if len(ia) > 2 else 0
            prob = ix.try_eval(a[1], ctx) if len(a) > 1 else 1.0
            effects.append({"effect": eid, "duration": dur if isinstance(dur, (int, float)) else None,
                            "amplifier": amp if isinstance(amp, int) else 0,
                            "chance": float(prob) if isinstance(prob, (int, float)) else 1.0})
    if effects:
        out["effects"] = effects[::-1]  # the walk sees the builder chain inside out
    return out
