"""The mods documented by the wiki, in navigation order.

`jar` is the file-name prefix of the mod jar in the pack's mods/ folder.
`family` selects extra extractors (tensura = ManasCore skills and races).
"""

MODS = [
    {
        "slug": "tensura-reincarnated", "name": "Tensura: Reincarnated", "jar": "tensura-neoforge-",
        "modids": ["tensura"], "family": "tensura", "group": "Tensura",
        "blurb": "The base mod: reincarnate as a slime, goblin, daemon and more, grow your EP, learn skills and magic, and evolve.",
    },
    {
        "slug": "tr-nightmares", "name": "TR: Nightmares", "jar": "trnightmare-",
        "modids": ["trnightmare"], "family": "tensura", "group": "Tensura",
        "blurb": "A large Tensura addon with hundreds of skills (including God-class Ultimates), new races, egos, friendship and soul systems, bosses and dimensions.",
    },
    {
        "slug": "elite-tensura", "name": "Elite Tensura", "jar": "elitetensura-",
        "modids": ["elitetensura"], "family": "tensura", "group": "Tensura",
        "blurb": "Tensura addon with Ultimate skills, Saiyan-style races, the Divine Forge, nations, seasons and a guide book.",
    },
    {
        "slug": "tensura-more-skills", "name": "TensuraMoreSkills", "jar": "tensuramoreskills-",
        "modids": ["tensuramoreskills"], "family": "tensura", "group": "Tensura",
        "blurb": "Tensura addon adding more Unique and Ultimate skills, races and the Void Archive.",
    },
    {
        "slug": "tensura-mysticism", "name": "Tensura: Mysticism", "jar": "mysticism-neoforge-",
        "modids": ["mysticism"], "family": "tensura", "group": "Tensura",
        "blurb": "Tensura addon focused on races (wyrms, direwolves, insects, elementals, angels and more), soul energy and new skills.",
    },
    {
        "slug": "ascension", "name": "Ascension", "jar": "ascension-",
        "modids": ["ascension"], "family": "tensura", "group": "Tensura",
        "blurb": "Tensura: Ascension adds an Ultimate awakening system, ten new race lines with their own evolutions, skills and a dimension.",
    },
    {
        "slug": "nightmare-utils", "name": "Nightmare Utils", "jar": "nightmareutils-",
        "modids": ["nightmareutils"], "family": "tensura", "group": "Tensura",
        "blurb": "Library mod (Nightmare's Tensura Utils) used by TR: Nightmares. Adds the Mimicry system and shared helpers.",
    },
    {
        "slug": "enigmatic-legacy-plus", "name": "EnigmaticLegacy+", "jar": "enigmaticlegacyplus-",
        "modids": ["enigmaticlegacyplus"], "family": "enigmatic", "group": "Items & Equipment",
        "blurb": "Mysterious rings, amulets, spellstones, scrolls and cursed items, with the Seven Curses ring at its heart.",
        "default_config_file": "serverconfig/enigmaticlegacyplus-server.toml",
    },
    {
        "slug": "relics", "name": "Relics", "jar": "relics-",
        "modids": ["relics"], "family": "relics", "group": "Items & Equipment",
        "blurb": "Levelled, researchable relics found in chests. Each relic has abilities you unlock and upgrade.",
    },
    {
        "slug": "more-relics", "name": "More Relics", "jar": "morerelics-",
        "modids": ["morerelics"], "family": "relics", "group": "Items & Equipment",
        "blurb": "An addon for Relics with many more relics and their abilities.",
    },
    {
        "slug": "artifacts", "name": "Artifacts", "jar": "artifacts-neoforge-",
        "modids": ["artifacts"], "family": "artifacts", "group": "Items & Equipment",
        "blurb": "Wearable artifacts found in dungeons and from Mimics. In this pack, RAR-Compat turns them into levelled relics.",
    },
    {
        "slug": "gateways-to-eternity", "name": "Gateways To Eternity", "jar": "GatewaysToEternity-",
        "modids": ["gateways"], "family": "gateways", "group": "World & Utility",
        "blurb": "Gate Pearls open portals that spawn waves of enemies with rewards for surviving.",
    },
    {
        "slug": "corail-tombstone", "name": "Corail Tombstone", "jar": "tombstone-neoforge-",
        "modids": ["tombstone"], "family": "tombstone", "group": "World & Utility",
        "blurb": "Graves keep your items when you die, plus perks, magic scrolls, familiars and the Grave's Key.",
    },
]

# Jars that are read for supporting data (lang, tags, registries) but get no pages.
SUPPORT_JARS = ["manascore-neoforge-", "tensura_neb-neoforge-", "rarcompat-", "Placebo-"]

GROUPS = ["Tensura", "Items & Equipment", "World & Utility"]
