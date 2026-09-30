/* Filter chips + text search for tables wrapped in <div class="filter-table" data-filter="Column">.
   Cells may hold several values separated by " / " (a race can be both Starting and Final).
   The chosen filter is kept in the URL (?stage=final) so a filtered view can be linked. */
(function () {
  "use strict";

  function el(tag, cls, txt) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (txt != null) e.textContent = txt;
    return e;
  }

  function readParam(name) {
    try {
      return new URLSearchParams(window.location.search).get(name) || "";
    } catch (e) {
      return "";
    }
  }

  function writeParam(name, value) {
    try {
      var url = new URL(window.location.href);
      if (value) url.searchParams.set(name, value);
      else url.searchParams.delete(name);
      window.history.replaceState(window.history.state, "", url);
    } catch (e) { /* history unavailable: filtering still works */ }
  }

  function setup(box) {
    if (box.getAttribute("data-ready")) return;
    var table = box.querySelector("table");
    if (!table || !table.tHead || !table.tBodies.length) return;
    var col = box.getAttribute("data-filter") || "Stage";
    var param = col.toLowerCase();
    var heads = Array.prototype.map.call(table.tHead.rows[0].cells, function (c) { return c.textContent.trim(); });
    var ci = heads.indexOf(col);
    if (ci < 0) return;
    box.setAttribute("data-ready", "1");

    var rows = Array.prototype.slice.call(table.tBodies[0].rows);
    var values = (box.getAttribute("data-order") || "").split(",").filter(Boolean);
    rows.forEach(function (tr) {
      var cellEl = tr.cells[ci];
      tr._vals = cellEl ? cellEl.textContent.split("/").map(function (s) { return s.trim(); }).filter(Boolean) : [];
      tr._text = tr.textContent.toLowerCase();
      tr._vals.forEach(function (v) { if (values.indexOf(v) < 0) values.push(v); });
    });

    var bar = el("div", "filter-bar");
    bar.setAttribute("role", "group");
    bar.setAttribute("aria-label", "Filter by " + col.toLowerCase());
    bar.appendChild(el("span", "filter-label", col + ":"));
    var chips = [];
    function chip(value, label, count) {
      var b = el("button", "filter-chip");
      b.type = "button";
      b.setAttribute("data-value", value);
      b.setAttribute("aria-pressed", "false");
      b.appendChild(document.createTextNode(label + " "));
      b.appendChild(el("span", "filter-chip-count", String(count)));
      b.addEventListener("click", function () { select(value, true); });
      chips.push(b);
      bar.appendChild(b);
    }
    chip("", "All", rows.length);
    values.forEach(function (v) {
      chip(v, v, rows.filter(function (tr) { return tr._vals.indexOf(v) >= 0; }).length);
    });

    var search = el("input", "filter-search");
    search.type = "search";
    search.placeholder = "Search this table";
    search.setAttribute("aria-label", "Search this table");
    bar.appendChild(search);
    var status = el("span", "filter-count");
    status.setAttribute("aria-live", "polite");
    bar.appendChild(status);

    var empty = el("p", "filter-empty", "No rows match this filter.");
    empty.hidden = true;

    box.insertBefore(bar, box.firstChild);
    table.parentNode.insertBefore(empty, table.nextSibling);

    var current = "";
    function apply() {
      var q = search.value.trim().toLowerCase();
      var shown = 0;
      rows.forEach(function (tr) {
        var ok = (!current || tr._vals.indexOf(current) >= 0) && (!q || tr._text.indexOf(q) >= 0);
        tr.hidden = !ok;
        if (ok) shown++;
      });
      status.textContent = "Showing " + shown + " of " + rows.length;
      empty.hidden = shown > 0;
    }
    function select(value, remember) {
      current = value;
      chips.forEach(function (b) {
        b.setAttribute("aria-pressed", b.getAttribute("data-value") === value ? "true" : "false");
      });
      if (remember) writeParam(param, value.toLowerCase());
      apply();
    }
    search.addEventListener("input", apply);

    var wanted = readParam(param).toLowerCase();
    var start = values.filter(function (v) { return v.toLowerCase() === wanted; })[0] || "";
    select(start, false);
  }

  function init() {
    Array.prototype.forEach.call(document.querySelectorAll(".filter-table"), setup);
  }

  if (typeof window.document$ !== "undefined" && window.document$.subscribe) {
    window.document$.subscribe(init);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
