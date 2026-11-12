// Checks for the dotted circle in the prototype (Spec §20 AAAAA; Art-Direction §3.2, §3.3; Decisions-Needed B86-B88).
//
//     node --test prototype/test_prototype.mjs
//
// Runs the page's own script in a Node context with a minimal document, so the checks exercise the real code.
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import vm from "node:vm";

const HTML = readFileSync(new URL("./index.html", import.meta.url), "utf8");
const SCRIPT = HTML.match(/<script>([\s\S]*?)<\/script>/)[1];
const DAY = 86400000;

function boot() {
  const nodes = {};
  const node = id => (nodes[id] ??= { id, innerHTML: "", textContent: "", value: "", onclick: null });
  const ctx = vm.createContext({
    document: { getElementById: node, addEventListener() {}, createElement: () => ({ innerHTML: "", content: null }) },
    setInterval() {}, console, Date, Math, Object, Array, Set, String, Number, JSON,
  });
  vm.runInContext(SCRIPT, ctx);
  const run = code => vm.runInContext(code, ctx);
  return { run, screen: () => nodes.screen.innerHTML };
}

const RING = /<g class="ring (ink|soft)" data-place="(\d+)">(.*?)<\/g>/g;
const DOT = /<circle cx="([\d.]+)" cy="([\d.]+)" r="([\d.]+)"\/>/g;
function rings(svg) {
  const out = {};
  for (const [, ink, place, body] of svg.matchAll(RING)) out[+place] = { ink, dots: [...body.matchAll(DOT)].map(m => m.slice(1).map(Number)) };
  return out;
}
const angle = d => (Math.atan2(d[0] - 160, 160 - d[1]) * 180 / Math.PI + 360) % 360;
const radii = ring => new Set(ring.dots.map(d => d[2]));
const biggest = ring => ring.dots.filter(d => d[2] === Math.max(...radii(ring)));
const weekAngle = (ring, w, k) => (k * 135 + 360 * (w + 0.5) / 52) % 360;
const close = (a, b) => Math.abs(((a - b + 540) % 360) - 180) < 0.05;

test("the owner's profile at baseline shows one ring of 52 dots per finished reveal", () => {
  const { run, screen } = boot();
  run(`state.viewer = "lantern"; state.tab = "profile"; render();`);
  const rs = rings(screen());
  assert.deepEqual(Object.keys(rs).map(Number).sort(), [1, 2, 3, 4, 5]);
  for (const r of Object.values(rs)) assert.equal(r.dots.length, 52);
});

test("the owner sees at most three sizes, and her highlight weeks are the biggest", () => {
  const { run, screen } = boot();
  run(`state.viewer = "lantern"; render();`);
  const rs = rings(screen());
  for (const r of Object.values(rs)) assert.ok(radii(r).size <= 3);
  // Lantern #1 finished first (k = 1), so at baseline it is the oldest ring, place 5. Highlight opened 2021-07-17.
  const day = (Date.UTC(2021, 6, 17) - Date.UTC(2021, 0, 1)) / DAY;
  const big = biggest(rs[5]);
  assert.equal(big.length, 1);
  assert.ok(close(angle(big[0]), weekAngle(rs[5], Math.floor(day / 7), 1)));
});

test("the newest ring is next to the name, in full ink, and holds the newest journey", () => {
  const { run, screen } = boot();
  run(`state.viewer = "lantern"; render();`);
  const rs = rings(screen());
  assert.equal(rs[1].ink, "ink");
  for (const p of [2, 3, 4, 5]) assert.equal(rs[p].ink, "soft");
  const r1 = Math.hypot(rs[1].dots[0][0] - 160, rs[1].dots[0][1] - 160);
  const r2 = Math.hypot(rs[2].dots[0][0] - 160, rs[2].dots[0][1] - 160);
  assert.ok(r1 < r2);
  // Lantern #5 (k = 5) opened its highlight on 2025-08-09
  const day = (Date.UTC(2025, 7, 9) - Date.UTC(2025, 0, 1)) / DAY;
  assert.ok(close(angle(biggest(rs[1])[0]), weekAngle(rs[1], Math.floor(day / 7), 5)));
});

test("anyone else sees the same rings as even dots, with no sizes", () => {
  const { run, screen } = boot();
  run(`state.viewer = "wind"; state.sub = "user:lantern"; render();`);
  const rs = rings(screen());
  assert.equal(Object.keys(rs).length, 5);
  for (const r of Object.values(rs)) { assert.equal(r.dots.length, 52); assert.equal(radii(r).size, 1); }
});

test("a finished reveal adds its ring next to the name, and older rings move out keeping their pattern", () => {
  const { run } = boot();
  const before = rings(run(`circleSvg("lantern", "lantern")`));
  run(`clock = Date.UTC(2027, 0, 2); jumpedAt = Date.now(); finishReveal(state.journeys.lantern6);`);
  const after = rings(run(`circleSvg("lantern", "lantern")`));
  assert.equal(Object.keys(after).length, 6);
  for (const p of [1, 2, 3, 4, 5]) {
    const was = before[p].dots.map((d, i) => [angle(d), d[2] === Math.min(...radii(before[p])) ? 0 : 1, i]);
    const now = after[p + 1].dots.map((d, i) => [angle(d), d[2] === Math.min(...radii(after[p + 1])) ? 0 : 1, i]);
    for (let i = 0; i < 52; i++) { assert.ok(close(was[i][0], now[i][0])); assert.equal(was[i][1], now[i][1]); }
  }
});

test("the sealed year adds nothing to the circle, photo or no photo", () => {
  const { run } = boot();
  const at = iso => run(`clock = Date.parse("${iso}"); jumpedAt = Date.now(); circleSvg("lantern", "lantern")`);
  const a = at("2026-02-01T00:00:00Z"), b = at("2026-07-01T00:00:00Z"), c = at("2026-12-31T00:00:00Z");
  assert.equal(a, b); assert.equal(b, c);
  run(`state.viewer = "lantern"; press();`);
  assert.equal(run(`circleSvg("lantern", "lantern")`), c);
});

test("a highlight that held no photo leaves no biggest dot (B87)", () => {
  const { run } = boot();
  run(`
    clock = Date.UTC(2026, 10, 1); jumpedAt = Date.now(); state.viewer = "light";
    state.journeys.light1 = { id: "light1", owner: "light", n: 1, commit: now(), unlock: addMonths(now(), 12), type: "E", chapter: null, tags: [], finished: null, highlights: [], photoIds: [] };
    startHighlight();
    clock = Date.UTC(2026, 10, 10); jumpedAt = Date.now(); press();
    clock = Date.UTC(2027, 10, 2); jumpedAt = Date.now(); finishReveal(state.journeys.light1);
  `);
  const rs = rings(run(`circleSvg("light", "light")`));
  assert.equal(Object.keys(rs).length, 1);
  assert.equal(radii(rs[1]).size, 2); // no-photo and photo: the empty highlight drew nothing
});

test("the fixture highlights hold their photos inside their 24 hours (Proposal §3.3)", () => {
  const { run } = boot();
  for (const [id, start, count] of [["lantern1", "2021-07-17T10:00:00Z", 19], ["lantern5", "2025-08-09T09:00:00Z", 12], ["hands2", "2024-06-18T06:00:00Z", 30]]) {
    const ps = JSON.parse(run(`JSON.stringify(state.journeys.${id}.photoIds.map(i => state.photos[i]).filter(p => p.inHighlight).map(p => p.captured))`));
    assert.equal(ps.length, count, id);
    const t0 = Date.parse(start);
    for (const t of ps) assert.ok(t >= t0 && t < t0 + DAY, id);
  }
});

test("the circle's markup carries no number for a screen reader", () => {
  const { run } = boot();
  const svg = run(`circleSvg("lantern", "wind")`);
  for (const m of svg.matchAll(/aria-label="([^"]*)"/g)) assert.doesNotMatch(m[1], /\d/);
  assert.match(svg, /aria-hidden="true"/);
});
