#!/usr/bin/env python3
"""Regenerates preview/index.html from the Phase 2 docs. Python standard library only.

    python3 preview/build.py

A one-off preview of Phase 2 (Look). Not the Phase 4 app and not the Phase 5 site.

Taken from the docs on every run, so a wording change only needs a re-run:
  - tokens, type scale, mark paths and specimens: docs/Art-Direction.md
  - the ritual and the full documents: docs/Flows.md, docs/Art-Direction.md, docs/Microcopy.md
  - every mock-screen line: docs/Microcopy.md, by entry id. See COPY below
If an entry changes shape, COPY raises rather than showing the wrong line.

Written by hand here, and nowhere else: the words around the frames (MOMENTS, LOOK), the
fixture values (FIXTURE) and the drawing formulas of Art-Direction §3 to §6.
"""
import datetime as dt
import html
import math
import random
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parent / "docs"
AD = (DOCS / "Art-Direction.md").read_text()
FLOWS = (DOCS / "Flows.md").read_text()
MICRO = (DOCS / "Microcopy.md").read_text()
esc = html.escape


# ---------------------------------------------------------------- markdown (only what the docs use)

def split_row(line):
    cells, cur, in_code, i = [], "", False, 0
    s = line.strip()[1:-1]
    while i < len(s):
        c = s[i]
        if c == "\\" and s[i + 1:i + 2] == "|":
            cur += "|"
            i += 2
            continue
        if c == "`":
            in_code = not in_code
        if c == "|" and not in_code:
            cells.append(cur.strip())
            cur = ""
        else:
            cur += c
        i += 1
    cells.append(cur.strip())
    return cells


def inline(text, prefix):
    codes = []

    def keep(m):
        codes.append("<code>" + esc(m.group(1), quote=False) + "</code>")
        return "\0%d\0" % (len(codes) - 1)

    text = re.sub(r"`([^`]+)`", keep, text)
    text = esc(text, quote=False).replace("&lt;br&gt;", "<br>")
    text = re.sub(r"\[([^\]]+)\]\(#([^)]+)\)", lambda m: '<a href="#%s-%s">%s</a>' % (prefix, m.group(2), m.group(1)), text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    return re.sub(r"\0(\d+)\0", lambda m: codes[int(m.group(1))], text)


def slug(title):
    t = re.sub(r"[`*]", "", title).lower()
    t = re.sub(r"[^\w\- ]", "", t)
    return t.replace(" ", "-")


LIST_RE = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")


def render_list(lines, i, indent, prefix):
    first = LIST_RE.match(lines[i])
    ordered = first.group(2)[0].isdigit()
    tag = "ol" if ordered else "ul"
    start = int(first.group(2)[:-1]) if ordered else 1
    out = ["<%s%s>" % (tag, ' start="%d"' % start if start != 1 else "")]
    open_li = False
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and LIST_RE.match(lines[j]) and len(LIST_RE.match(lines[j]).group(1)) >= indent:
                i = j
                continue
            break
        m = LIST_RE.match(line)
        if not m:
            if len(line) - len(line.lstrip()) > indent and open_li:
                out.append("<br>" + inline(line.strip(), prefix))
                i += 1
                continue
            break
        level = len(m.group(1))
        if level < indent:
            break
        if level > indent:
            nested, i = render_list(lines, i, level, prefix)
            out.append(nested)
            continue
        if open_li:
            out.append("</li>")
        out.append("<li>" + inline(m.group(3), prefix))
        open_li = True
        i += 1
    if open_li:
        out.append("</li>")
    out.append("</%s>" % tag)
    return "".join(out), i


def render_md(text, prefix, shift=2):
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif line.startswith("```"):
            j = i + 1
            while not lines[j].startswith("```"):
                j += 1
            out.append("<pre><code>" + esc("\n".join(lines[i + 1:j]), quote=False) + "</code></pre>")
            i = j + 1
        elif re.match(r"^#{1,6} ", line):
            hashes, title = line.split(" ", 1)
            level = min(len(hashes) + shift, 6)
            out.append('<h%d id="%s-%s">%s</h%d>' % (level, prefix, slug(title), inline(title, prefix), level))
            i += 1
        elif re.match(r"^-{3,}\s*$", line):
            out.append("<hr>")
            i += 1
        elif line.startswith("|"):
            j = i
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            rows = [split_row(r) for r in lines[i:j]]
            head = "".join("<th>%s</th>" % inline(c, prefix) for c in rows[0])
            body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c, prefix) for c in r) for r in rows[2:])
            out.append('<div class="table"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (head, body))
            i = j
        elif LIST_RE.match(line):
            block, i = render_list(lines, i, len(LIST_RE.match(line).group(1)), prefix)
            out.append(block)
        else:
            j = i
            while j < len(lines) and lines[j].strip() and not re.match(r"^(#{1,6} |```|\||-{3,}\s*$)", lines[j]) and not LIST_RE.match(lines[j]):
                j += 1
            out.append("<p>%s</p>" % "<br>".join(inline(x, prefix) for x in lines[i:j]))
            i = j
    return "\n".join(out)


# ---------------------------------------------------------------- reading the docs

def section(text, heading):
    m = re.search(r"^%s\n(.*?)^---\s*$" % re.escape(heading), text, re.M | re.S)
    if not m:
        raise SystemExit("Section not found: " + heading)
    return m.group(1).strip()


def micro_strings(entry):
    for line in MICRO.split("\n"):
        if line.startswith("| %s |" % entry):
            return re.findall(r'"([^"]+)"', split_row(line)[3])
    raise SystemExit("Microcopy entry not found: " + entry)


def copy_of(entry, n):
    got = micro_strings(entry)
    if len(got) != n:
        raise SystemExit("%s now has %d strings, expected %d: update COPY in build.py" % (entry, len(got), n))
    return got


# Every line a mock screen shows, in one place. All of it comes from Microcopy.md.
M01 = copy_of("M-01", 5)   # S-01: the three types, then two lines on all of them
M02 = copy_of("M-02", 2)   # S-01: the button, then the Commit line
M10 = copy_of("M-10", 1)   # S-03: the sealed state
M11 = copy_of("M-11", 1)   # S-05: "Your Journey is ready."
M21 = copy_of("M-21", 1)   # S-07: how the map is described
M23 = copy_of("M-23", 1)   # S-05: the circle line
COPY = {"M-01": M01, "M-02": M02, "M-10": M10, "M-11": M11, "M-21": M21, "M-23": M23}

PATHS = {}
for row, key in (("Frame (core line)", "frame"), ("Map core", "core"), ("Mark, large", "m48")):
    m = re.search(r"^\| %s \|.*`(M[^`]+)` \|$" % re.escape(row), AD, re.M)
    if not m:
        raise SystemExit("Art-Direction path not found: " + row)
    PATHS[key] = m.group(1)

CSS_BLOCK = re.search(r"```css\n(.*?)```", AD, re.S).group(1)
LIGHT = re.search(r":root \{\n(.*?)\n\}", CSS_BLOCK, re.S).group(1)
DARK = re.search(r'\[data-mj-theme="dark"\] \{\n(.*?)\n\}', CSS_BLOCK, re.S).group(1)
COLOUR_RE = re.compile(r"--mj-([\w-]+):\s+(#[0-9A-Fa-f]{6});(?:[ \t]*/\*\s*(.*?)\s*\*/)?")
LIGHT_COLOURS = COLOUR_RE.findall(LIGHT)
DARK_COLOURS = {n: v for n, v, _ in COLOUR_RE.findall(DARK)}

FAMILY = {"Fraunces": "--mj-font-display", "Source Serif 4": "--mj-font-text", "Courier Prime": "--mj-font-label", "Caveat": "--mj-font-hand"}
TYPE_ROWS = re.findall(r"^\| `([\w-]+)` \| (Fraunces|Source Serif 4|Courier Prime|Caveat) \| (\d+) / (\d+)[^|]*\| ([\d.]+) \| (\d+)? ?\| ?([^|]*)\|$", AD, re.M)
SPECIMENS = re.findall(r"^\| `([\w-]+)` \| ([^|]+?) \|$", AD[AD.index("**Specimens.**"):AD.index("## 9. Texture")], re.M)
CLAUDE_MD = (HERE.parent / "CLAUDE.md").read_text()
if len(SPECIMENS) != 6 or any('"%s"' % s not in CLAUDE_MD for _, s in SPECIMENS):
    raise SystemExit("The six specimens no longer match CLAUDE.md, word for word")


def type_css():
    out = []
    for name, fam, size, line, rem, weight, settings in TYPE_ROWS:
        fvs = ""
        if "SOFT" in settings:
            fvs = "font-variation-settings:%s;" % settings.strip().strip("`")
        colour = "color:var(--mj-ballpoint);" if name == "hand" else ""
        out.append(".t-%s{font-family:var(%s);font-size:%srem;line-height:%.4frem;font-weight:%s;%s%s}" % (
            name, FAMILY[fam], rem, int(line) / 16, weight or 400, fvs, colour))
    return "\n".join(out)


# ---------------------------------------------------------------- drawing (Art-Direction §3 to §6)

def polar(r, deg, cx=160.0):
    a = math.radians(deg)
    return cx + r * math.sin(a), cx - r * math.cos(a)


CORE_R = 80


WEEKS = 52
FIRST_PITCH, PITCH_RATIO, CLEARANCE = 11, 0.85, 3
DOT_RATIOS = (0.12, 0.24, 0.36)   # a week with no photo, with a photo, the week a highlight opened
ANGLE_STEP = 135.0                # 19.5 dot spacings: each ring's dots sit halfway between the next ring's


def ring_values(j):
    """The ring at place j, counted from the frame outward, 1 the newest (§3.2, Spec §20 AAAAA).
    It depends on j alone, never on the count."""
    p = FIRST_PITCH * PITCH_RATIO ** (j - 1)
    r = CORE_R + CLEARANCE + sum(FIRST_PITCH * PITCH_RATIO ** i for i in range(j))
    return (p, r) + tuple(f * p for f in DOT_RATIOS) + (2 * math.pi * r / WEEKS,)


# The worked values of §3.2. The build stops if the formulas drift from the doc.
WORKED = re.findall(r"^\| (\d+) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|$", AD, re.M)
if len(WORKED) < 5:
    raise SystemExit("Art-Direction §3.2 worked values not found")
for row in WORKED:
    j = int(row[0])
    got = ring_values(j)
    for mine, theirs in zip(got, row[1:]):
        if abs(mine - float(theirs)) > 0.006:
            raise SystemExit("Ring table mismatch at place %d: %s against %s" % (j, got, row))
if not re.search(r"A%d %d 0 1 1" % (CORE_R, CORE_R), PATHS["frame"]):
    raise SystemExit("The frame path no longer has radius %d: update CORE_R" % CORE_R)


def week_of(day):
    """Day index from the commit date (0 is the commit date) to week 0..51. Week 52 takes the last 8 or 9 days.
    PROVISIONAL: B86"""
    return min(day // 7, WEEKS - 1)


def week_sizes(days=None, highlights=()):
    """52 sizes: 0 no photo, 1 one or more photos, 2 the week a highlight opened (Spec §20 AAAAA (b)).
    highlights: the opening day of each highlight that holds a photo (PROVISIONAL: B87). No count is kept."""
    sizes = [0] * WEEKS
    for d in days or ():
        sizes[week_of(d)] = max(sizes[week_of(d)], 1)
    for d in highlights:
        sizes[week_of(d)] = 2
    return sizes


def dot_ring(j, k, sizes=None):
    """The ring at place j for the journey that finished k-th. sizes=None gives 52 even dots, as every viewer
    but the owner sees them (PROVISIONAL: B88). The newest ring, place 1, is the brightest (Spec §20 IIII)."""
    p, r = ring_values(j)[:2]
    radii = ring_values(j)[2:5]
    theta = (k * ANGLE_STEP) % 360
    out = []
    for w, size in enumerate(sizes or [0] * WEEKS):
        x, y = polar(r, theta + 360 * (w + 0.5) / WEEKS)
        out.append('<circle cx="%.2f" cy="%.2f" r="%.2f"/>' % (x, y, radii[size]))
    return '<g class="ring %s" data-place="%d">%s</g>' % ("ink" if j == 1 else "soft", j, "".join(out))


def balanced(name):
    words = name.split(" ")
    if len(words) == 1:
        return words
    return min(([" ".join(words[:i]), " ".join(words[i:])] for i in range(1, len(words))), key=lambda ls: max(map(len, ls)))


def circle(name, journeys=()):
    """journeys: one entry per finished reveal, in the order of finishing, oldest first. An entry is None for
    even dots, or the owner's {"days": [...], "highlights": [...]} (day indices from the commit date).
    The newest is drawn next to the frame and every older ring one place further out (Spec §20 AAAAA (c))."""
    n = len(journeys)
    rings = "".join(
        dot_ring(n - i, i + 1, week_sizes(j["days"], j.get("highlights", ())) if j else None)
        for i, j in enumerate(journeys)
    )
    ls = balanced(name)
    top = 160 - 14.5 * (len(ls) - 1)
    text = "".join('<tspan x="160" y="%.1f">%s</tspan>' % (top + 29 * i, esc(x)) for i, x in enumerate(ls))
    return ('<svg class="circle" viewBox="0 0 320 320"><g class="line" aria-hidden="true"><path d="%s" stroke-width="2"/></g>'
            '<g class="dots" aria-hidden="true">%s</g>'
            '<text class="circle-name" text-anchor="middle" dominant-baseline="central" data-fixture>%s</text></svg>') % (PATHS["frame"], rings, text)


def mark(px, stroke):
    pad = px * 17 / 48  # clear space: one radius
    return '<svg class="line mark" style="margin:%.1fpx" viewBox="0 0 48 48" width="%d" height="%d" aria-hidden="true"><path d="%s" stroke-width="%s"/></svg>' % (pad, px, px, PATHS["m48"], stroke)


ENVELOPE = (
    '<div class="envelope" aria-hidden="true"><svg viewBox="0 0 280 196">'
    '<rect class="env-body" x=".75" y=".75" width="278.5" height="194.5" rx="2"/>'
    '<path class="env-flap" d="M1 1 L140 112 L279 1 Z"/>'
    '<circle class="env-seal" cx="140" cy="112" r="28"/>'
    '<path class="env-mark" transform="translate(116 88)" d="%s"/>'
    "</svg></div>" % PATHS["m48"]
)


def flat_graph(days, length):
    points = []
    for step in range(0, 601):
        x = 10 + step * 0.5
        rise = 0.0
        for d in days:
            dist = abs(x - (10 + 300 * (d + 0.5) / length))
            h = 300 * 4 / length
            if dist < h:
                rise = max(rise, math.cos(math.pi * dist / (2 * h)) ** 2)
        points.append("%.1f %.2f" % (x, 16 - 3 * rise))
    return '<svg class="flat line" viewBox="0 0 320 24" aria-hidden="true"><path d="M%s" stroke-width="1.25"/></svg>' % " L".join(points)


def layer_map(owner_lines, people):
    """people: (member id, name, radius). PROVISIONAL: B40, all three rings on a map with anyone on it; the core alone otherwise."""
    radii = (80, 115, 150) if people else ()
    rings = "".join('<circle class="layer" cx="180" cy="180" r="%d"/>' % r for r in radii)
    m = len(people)
    names = ""
    for j, (_, name, r) in enumerate(sorted(people)):
        t = (j + 0.5) / m * 280
        angle = -70 + t if t < 140 else 110 + (t - 140)
        x, y = polar(r, angle, 180.0)
        names += '<span class="person t-hand" style="left:%.2f%%;top:%.2f%%" data-fixture>%s</span>' % (x / 3.6, y / 3.6, esc(name))
    core = "<br>".join(esc(x) for x in owner_lines)
    return ('<div class="map"><svg viewBox="0 0 360 360" aria-hidden="true">%s<path class="line" d="%s" stroke-width="1.5"/></svg>'
            '<span class="map-core t-core-name" data-fixture>%s</span>%s</div>') % (rings, PATHS["core"], core, names)


# ---------------------------------------------------------------- fixture values (Phase-1-Proposal §3)

def journey_days(key, commit, unlock, count, also=(), skip_month=None, before=None):
    """The Proposal fixes each journey's dates and photo counts, not most capture days. The days here are invented."""
    start, end = dt.date.fromisoformat(commit), dt.date.fromisoformat(unlock)
    length = (end - start).days
    pool = [d for d in range(length)
            if (skip_month is None or (start + dt.timedelta(days=d)).month != skip_month)
            and (before is None or d < before)]
    days = set(random.Random(key).sample(pool, count))
    days.update((dt.date.fromisoformat(x) - start).days for x in also)
    return sorted(days), length


# Steady Lantern, Proposal §3.3. Highlights on their own dates, §3.3 Highlights.
LANTERN = [
    journey_days("lantern-1", "2021-01-01", "2022-01-01", 41, also=["2021-07-17"]),
    journey_days("lantern-2", "2022-01-01", "2023-01-01", 37),
    journey_days("lantern-3", "2023-01-01", "2024-01-01", 22, skip_month=3),
    journey_days("lantern-4", "2024-01-01", "2025-01-01", 24),
    journey_days("lantern-5", "2025-01-01", "2026-01-01", 12, also=["2025-08-09"]),
]
LANTERN_6 = journey_days("lantern-6", "2026-01-01", "2027-01-01", 9, before=297)


def day_index(commit, date):
    return (dt.date.fromisoformat(date) - dt.date.fromisoformat(commit)).days


# The owner's rings, oldest first. Highlights hold photos here (Proposal §3.3), so each marks its week (B87).
LANTERN_HIGHLIGHTS = [["2021-07-17"], [], [], [], ["2025-08-09"]]
LANTERN_COMMITS = ["2021-01-01", "2022-01-01", "2023-01-01", "2024-01-01", "2025-01-01"]
LANTERN_RINGS = [{"days": days, "highlights": [day_index(c, h) for h in hs]}
                 for (days, _), c, hs in zip(LANTERN, LANTERN_COMMITS, LANTERN_HIGHLIGHTS)]
LANTERN_6_RING = {"days": LANTERN_6[0], "highlights": []}

FIXTURE = {
    "type": "Contemplator",            # Steady Lantern #6
    "commit": "2026-01-01",
    "unlock": "2027-01-01",
    # Lantern's map at baseline, Proposal §3.4. Rings: tight 80, middle 115, outer 150 (Art-Direction §6)
    "map_people": [("hands", "Open Hands", 150), ("wind", "Second Wind", 80)],
}


# ---------------------------------------------------------------- the page

def line(entry, i, cls="t-body", tag="p"):
    return '<%s class="%s" data-m="%s">%s</%s>' % (tag, cls, entry, esc(COPY[entry][i], quote=False), tag)


def fixture(text, cls="t-label soft"):
    return '<p class="%s" data-fixture>%s</p>' % (cls, esc(text))


SCREEN_S01 = (
    "".join('<div class="type">%s</div>' % line("M-01", i) for i in range(3))
    + line("M-01", 3) + line("M-01", 4) + line("M-02", 1)
    + '<div class="press t-heading" data-m="M-02">%s</div>' % esc(M02[0])
)
SCREEN_S03 = (
    ENVELOPE
    + '<div class="facts">%s%s%s</div>' % (fixture(FIXTURE["type"]), fixture(FIXTURE["commit"]), fixture(FIXTURE["unlock"]))
    + line("M-10", 0, "t-display-m")
)
SCREEN_READY = circle("Steady Lantern", LANTERN_RINGS) + line("M-11", 0) + flat_graph(*LANTERN_6)
SCREEN_PROFILE = circle("Steady Lantern", LANTERN_RINGS + [LANTERN_6_RING])
SCREEN_NO_RINGS = circle("First Light") + line("M-23", 0)
SCREEN_MAP = layer_map(["Steady", "Lantern"], FIXTURE["map_people"]) + line("M-21", 0)

MOMENTS = [
    ("Commit", "S-01. First Light, who has never committed.",
     "One press that cannot be undone. No type is picked for you, so none is marked. This rust and the press that finishes a reveal are the only rust in the product.",
     "Where the line sits against the press is open (FQ-2). It is above the press here for now.",
     SCREEN_S01),
    ("The sealed year", "S-03. Steady Lantern, on the baseline date 2026-10-25.",
     "One shut envelope, the same on every date of the year and before and after every photo. The type and two plain dates, then the words, sit off the envelope.",
     "The type and dates are bare because their labels are not written yet (Microcopy MQ-3). The line for an open highlight shows only while one is open, and none is here.",
     SCREEN_S03),
    ("Your Journey is ready", "S-05. Steady Lantern, on 2027-01-01, when her year opens.",
     "The words, and the year drawn as a straight line, not yet bent. No ring has been added for this year, because the reveal is not finished. Nothing here asks for anything.",
     "How long this line stays is open (C18). Its type style is not specified, so it is plain reading text here.",
     SCREEN_READY),
    ("A profile", "S-05. Steady Lantern, once she has finished that reveal.",
     "Her year is now a ring of 52 weeks next to her name, and each older ring has moved out one place, a step finer. Bigger dots are weeks with photos, the biggest the weeks her highlights opened, and only she sees the sizes. Nothing celebrates it, and on this state the screen has no line of its own: a ring being added is one of the places left silent on purpose.",
     "The ways on from this screen are not placed yet (AD-10).",
     SCREEN_PROFILE),
    ("A profile, before any Commit", "S-05. First Light.",
     "The same screen for someone with no rings. It is a whole mark and a plain statement, with no button and no suggestion.",
     "The way to Commit is left out (AD-10, Microcopy MQ-3). Which states show this line is open (Microcopy MQ-7).",
     SCREEN_NO_RINGS),
    ("Your map", "S-07. Steady Lantern's own map, as at her last finished reveal.",
     "Only ever the owner's. Every name and every ring looks the same, so closeness is never a rank. With anyone on the map, all three rings are drawn (B40), so a ring never vanishes when its last person moves out.",
     "There are no words on the rings (B32). How a map busier than the fixtures' looks is for ux (AD-7).",
     SCREEN_MAP),
]


def moments():
    out = []
    for title, who, what, gap, screen in MOMENTS:
        out.append(
            '<article class="moment"><div class="phone">%s</div><div class="note">'
            '<h3 class="t-title">%s</h3><p class="t-label soft">%s</p><p class="t-body">%s</p><p class="t-small soft">%s</p>'
            "</div></article>" % (screen, esc(title), esc(who), esc(what), esc(gap))
        )
    return "\n".join(out)


def token_table():
    """Both sets of values, drawn on the light page. PROVISIONAL: B30, light theme only."""
    rows = "".join(
        '<tr><td class="t-label">--mj-%s</td><td><span class="swatch" style="background:%s"></span>%s</td>'
        '<td><span class="swatch" style="background:%s"></span>%s</td><td class="t-small soft">%s</td></tr>'
        % (name, value, value, DARK_COLOURS[name], DARK_COLOURS[name], esc(note))
        for name, value, note in LIGHT_COLOURS
    )
    return ('<div class="table"><table class="tokens"><thead><tr><th class="t-label">Token</th><th class="t-label">Light</th>'
            '<th class="t-label">Dark</th><th class="t-label">Use</th></tr></thead><tbody>%s</tbody></table></div>' % rows)


# States are named by ring count and journey state only (Art-Direction §4; R-185)
LOOK_STATES = [
    ("0 rings", "First Light", circle("First Light"),
     "The frame and the name, and nothing else: no ghost ring, start line or placeholder. It is the logo with a name in it."),
    ("1 or more rings", "Steady Lantern, as she sees her own", circle("Steady Lantern", LANTERN_RINGS),
     "One ring per journey, 52 dots, one per week. A week with photos has a bigger dot, however many it held, and the week a highlight opened has the biggest. The newest journey is next to her name and the brightest; each older ring is a step finer. Only the owner sees the sizes (B88)."),
    ("1 or more rings", "Long Way Round, as other viewers see it", circle("Long Way Round", [None] * 3),
     "Every ring is 52 even dots, so nothing shows which weeks held photos or where a highlight fell (B27, B88). Each ring's dots sit halfway between the dots of the ring next to it, so no ring has a start to count from."),
    ("1 or more rings", "Second Wind, drawn far ahead of the fixtures, as other viewers see it", circle("Second Wind", [None] * 30),
     "The same formula at every count, with no point where the drawing changes. The circle grows by a smaller step each time and never reaches an edge, and nothing is drawn beyond the oldest ring. The oldest rings' dots fall below a screen pixel. Whether that is acceptable is open (AD-25, B89)."),
]


def look():
    states = "".join(
        '<div class="state"><div class="state-draw">%s</div><div><h4 class="t-heading">%s</h4><p class="t-label soft">%s</p><p class="t-body">%s</p></div></div>'
        % (svg, title, who, text)
        for title, who, svg, text in LOOK_STATES
    )
    marks = "".join(mark(px, stroke) for px, stroke in ((96, 2.6), (48, 3), (32, 3.2), (24, 3.6), (16, 4.4)))
    specimens = "".join(
        '<div class="specimen"><p class="t-label soft">%s</p><p class="t-%s">%s</p></div>' % (name, name, esc(text, quote=False))
        for name, text in SPECIMENS
    )
    return (
        '<h3 class="t-title">The circle</h3>'
        '<p class="t-body measure">Named as the art direction names them, by ring count only. One to a row, because the art direction does not allow circles lined up to compare.</p>'
        + states
        + '<h3 class="t-title">The mark</h3><div class="marks">' + marks + "</div>"
        + '<p class="t-small soft measure">At 96, 48, 32, 24 and 16 px, from left to right. The line gets slightly heavier as it gets smaller. Each has one radius of clear space, and nothing is ever placed on it.</p>'
        + '<h3 class="t-title">The sealed envelope</h3>' + ENVELOPE
        + '<p class="t-body measure">One drawing, identical for everyone on every date. It does not change with how many photos it holds, how much of the year has gone, or which type was chosen. Only the theme can change it.</p>'
        + '<h3 class="t-title">The map</h3>' + layer_map(["Steady", "Lantern"], FIXTURE["map_people"])
        + '<p class="t-body measure">Wide, thin rings with names on them, in a ballpoint hand, around the owner\'s name. It has no identity rings, so the two ring systems never share a drawing. An empty map is the core alone (B40).</p>'
        + '<h3 class="t-title">Colour</h3>'
        + '<p class="t-body measure">The cream album page and the black-card album page. The prototype uses the light set only, with no switch (B30), so this page is drawn in light and the dark values are shown as swatches. There is no green, red, gold, silver or bronze, so no colour can mean success, failure or achievement.</p>'
        + token_table()
        + '<h3 class="t-title">Type</h3>'
        + '<p class="t-body measure">The six lines of the voice, word for word, one in each style. These show the styles only. Where each line goes in the product is in the microcopy.</p>'
        + specimens
    )


FONT_FACES = """
@font-face{font-family:"Fraunces";src:url("fonts/Fraunces.woff2") format("woff2");font-weight:100 900;font-display:swap}
@font-face{font-family:"Source Serif 4";src:url("fonts/SourceSerif4.woff2") format("woff2");font-weight:200 900;font-display:swap}
@font-face{font-family:"Courier Prime";src:url("fonts/CourierPrime-Regular.woff2") format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:"Caveat";src:url("fonts/Caveat.woff2") format("woff2");font-weight:400 700;font-display:swap}
"""

PAGE_CSS = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--mj-page) var(--mj-texture-grain);color:var(--mj-ink);font-family:var(--mj-font-text);font-size:1.0625rem;line-height:1.625rem;font-optical-sizing:auto}
main{max-width:64rem;margin:0 auto;padding:var(--mj-space-7) var(--mj-space-3) var(--mj-space-8)}
@media (min-width:44rem){main{padding-inline:var(--mj-space-6)}}
h1,h2,h3,h4,p{margin:0}
a{color:var(--mj-ballpoint)}
:focus-visible{outline:var(--mj-focus);outline-offset:var(--mj-focus-offset)}
.soft{color:var(--mj-ink-soft)}
.measure{max-width:var(--mj-measure)}
header p{max-width:var(--mj-measure);margin-top:var(--mj-space-4)}
section{margin-top:var(--mj-space-8);padding-top:var(--mj-space-6);border-top:1px solid var(--mj-rule)}
section>h2{margin-bottom:var(--mj-space-5)}
section>h3{margin-top:var(--mj-space-7);margin-bottom:var(--mj-space-3)}
section>h2+h3{margin-top:0}
section>.measure{margin-bottom:var(--mj-space-4)}
.prose{max-width:var(--mj-measure)}
.prose p{margin-bottom:var(--mj-space-4)}
.prose strong{font-weight:600}

/* Drawings */
.line,.line path{fill:none;stroke:var(--mj-ink);stroke-linecap:round;stroke-linejoin:round}
.dots .ink{fill:var(--mj-ink)}.dots .soft{fill:var(--mj-ink-soft)}
.circle{display:block;width:100%;max-width:320px;height:auto}
.circle-name{font-family:var(--mj-font-display);font-size:26px;font-weight:500;font-variation-settings:"SOFT" 100,"WONK" 1;fill:var(--mj-ink)}
.state{display:flex;flex-wrap:wrap;gap:var(--mj-space-5);align-items:center;margin-bottom:var(--mj-space-6)}
.state-draw{flex:0 1 320px;min-width:240px}
.state>div:last-child{flex:1 1 16rem;max-width:var(--mj-measure)}
.state h4{margin-bottom:var(--mj-space-1)}
.state .t-label{margin-bottom:var(--mj-space-2)}
.marks{display:flex;flex-wrap:wrap;align-items:center;margin-bottom:var(--mj-space-3)}
.mark{display:block;flex:none}
.mark path{stroke-linecap:round}
.envelope{position:relative;width:min(280px,100%);flex:none;margin-bottom:var(--mj-space-4)}
.envelope svg{display:block;width:100%;height:auto;stroke:var(--mj-ink);stroke-linejoin:round}
.envelope::after{content:"";position:absolute;inset:0;background:var(--mj-texture-grain);border-radius:var(--mj-radius-paper);pointer-events:none}
.env-body{fill:var(--mj-kraft);stroke-width:1.5}
.env-flap{fill:var(--mj-kraft-shade);stroke-width:1.25}
.env-seal{fill:var(--mj-print);stroke-width:1.25}
.env-mark{fill:none;stroke-width:2.4;stroke-linecap:round}
.map{position:relative;width:min(360px,100%);aspect-ratio:1;margin-bottom:var(--mj-space-4)}
.map svg{display:block;width:100%;height:100%}
.layer{fill:none;stroke:var(--mj-line);stroke-width:1}
.map path{fill:none;stroke-linecap:round;stroke-linejoin:round}
.map-core{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);text-align:center}
.person{position:absolute;transform:translate(-50%,-50%);background:var(--mj-page) var(--mj-texture-grain);padding:0 4px;white-space:nowrap}
@media (max-width:359px){.map-core{font-size:.875rem;line-height:1.0625rem}}
.flat{display:block;width:100%;height:auto}

/* Tokens and type */
.tokens{border-collapse:collapse;min-width:100%}
.tokens th{text-align:left;font-weight:400;padding:0 var(--mj-space-3) var(--mj-space-2) 0}
.tokens td{padding:var(--mj-space-2) var(--mj-space-3) var(--mj-space-2) 0;vertical-align:top;border-top:1px solid var(--mj-rule)}
.tokens td:nth-child(2),.tokens td:nth-child(3){font-family:var(--mj-font-label);font-size:.875rem;white-space:nowrap}
.swatch{display:block;width:var(--mj-space-7);height:var(--mj-space-6);margin-bottom:var(--mj-space-1);border:1px solid var(--mj-line);border-radius:var(--mj-radius-paper)}
.specimen{padding:var(--mj-space-3) 0;border-top:1px solid var(--mj-rule);max-width:44rem}
.specimen .t-label{margin-bottom:var(--mj-space-1)}

/* Frames. They are pictures of screens: nothing in them can be pressed */
.moment{display:grid;gap:var(--mj-space-4);grid-template-columns:minmax(0,1fr);margin-top:var(--mj-space-7)}
@media (min-width:52rem){.moment{grid-template-columns:362px minmax(0,1fr);gap:var(--mj-space-7);align-items:start}}
.phone{width:min(362px,100%);min-height:640px;border:1px solid var(--mj-line);border-radius:var(--mj-radius-paper);padding:var(--mj-space-5) 20px;display:flex;flex-direction:column;gap:var(--mj-space-4);overflow:hidden}
.phone .circle,.phone .envelope{margin-inline:auto}
.phone .map{width:auto;margin:0 -20px}
.phone>.t-body{max-width:100%}
.note{max-width:var(--mj-measure);display:flex;flex-direction:column;gap:var(--mj-space-2)}
.type{background:var(--mj-print);border:1px solid var(--mj-line);border-radius:var(--mj-radius-paper);padding:var(--mj-space-3)}
.press{background:var(--mj-rust);color:var(--mj-on-rust);border-radius:var(--mj-radius-paper);min-height:var(--mj-target);padding:var(--mj-space-2) var(--mj-space-5);text-align:center}
.facts{display:flex;flex-direction:column}

/* The documents */
details{margin-top:var(--mj-space-3);border:1px solid var(--mj-line);border-radius:var(--mj-radius-paper)}
summary{min-height:var(--mj-target);padding:var(--mj-space-2) var(--mj-space-3);cursor:default}
.doc{padding:0 var(--mj-space-3) var(--mj-space-5);font-size:.9375rem;line-height:1.375rem}
.doc p,.doc ul,.doc ol{max-width:var(--mj-measure);margin:var(--mj-space-3) 0}
.doc ul,.doc ol{padding-left:var(--mj-space-5)}
.doc li ul,.doc li ol{margin:var(--mj-space-1) 0}
.doc h3,.doc h4,.doc h5,.doc h6{font-family:var(--mj-font-display);font-variation-settings:"SOFT" 100,"WONK" 0;font-weight:500;margin:var(--mj-space-6) 0 var(--mj-space-2)}
.doc h3{font-size:1.5625rem;line-height:1.875rem}
.doc h4{font-size:1.25rem;line-height:1.625rem}
.doc h5,.doc h6{font-size:.9375rem;line-height:1.375rem}
.doc hr{border:0;border-top:1px solid var(--mj-rule);margin:var(--mj-space-5) 0}
.doc code{font-family:var(--mj-font-label);font-size:.875rem;overflow-wrap:anywhere}
.doc pre{overflow-x:auto;background:var(--mj-print);padding:var(--mj-space-3);border-radius:var(--mj-radius-paper)}
.doc pre code{overflow-wrap:normal;white-space:pre}
.table{overflow-x:auto;margin:var(--mj-space-3) 0}
.doc table{border-collapse:collapse;min-width:100%}
.doc th,.doc td{text-align:left;vertical-align:top;padding:var(--mj-space-2);border-top:1px solid var(--mj-rule);min-width:7rem}
.doc th{font-family:var(--mj-font-label);font-weight:400;font-size:.875rem}
footer{margin-top:var(--mj-space-7)}
"""


def doc(title, prefix, text):
    return '<details><summary class="t-heading">%s</summary><div class="doc">%s</div></details>' % (title, render_md(text, prefix))


def build():
    ritual = section(FLOWS, "## The ritual in plain words")
    page = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<meta name="color-scheme" content="light">
<title>My Journey: Phase 2 preview</title>
<link rel="icon" href="data:,">
<style>
{fonts}
/* Tokens, word for word from docs/Art-Direction.md section 8 */
:root {{
{light}
}}
/* PROVISIONAL: B30. Light theme only: the dark tokens exist, with no control and no device switch */
{types}
{css}
</style>
</head>
<body>
<main>
<header>
<h1 class="t-display-l">My Journey: Phase 2 preview</h1>
<p class="t-body">This is a preview of Phase 2, on paper, with dummy data. It is not the working app, and it has not all been decided. The colours and fonts are the art director's proposals.</p>
<p class="t-small soft">It is drawn in the light theme only, as the prototype's working default (B30). This page makes no outside requests, and it has no scripts.</p>
</header>

<section>
<h2 class="t-display-m">The ritual</h2>
<div class="prose">{ritual}</div>
</section>

<section>
<h2 class="t-display-m">The look</h2>
{look}
</section>

<section>
<h2 class="t-display-m">The moments</h2>
<p class="t-body measure">Pictures of screens, in the order of the ritual. Nothing in them can be pressed. Every line inside a frame is the recommended line from the microcopy, word for word, and the names and dates are dummy data.</p>
<p class="t-small soft measure">Navigation is left out of every frame: where the ways sit is open (AD-10), and their words are not written (Microcopy MQ-3). The art direction draws each mark only beside its word, so none is shown. The weeks marked on the rings are invented, because the dummy data fixes how many photos a journey holds and only a few of their dates. The highlight weeks are the fixture's own.</p>
{moments}
</section>

<section>
<h2 class="t-display-m">The documents</h2>
<p class="t-body measure">The full text of the three Phase 2 documents, with their open questions. Open one to read it.</p>
{flows}
{ad}
{micro}
</section>

<footer>
<p class="t-small soft">Fonts are hosted with this page, under the SIL Open Font License 1.1: <a href="fonts/OFL-fraunces.txt">Fraunces</a>, <a href="fonts/OFL-sourceserif4.txt">Source Serif 4</a>, <a href="fonts/OFL-courierprime.txt">Courier Prime</a> and <a href="fonts/OFL-caveat.txt">Caveat</a>.</p>
</footer>
</main>
</body>
</html>
""".format(
        fonts=FONT_FACES.strip(),
        light=LIGHT,
        types=type_css(),
        css=PAGE_CSS.strip(),
        ritual=render_md(ritual, "ritual"),
        look=look(),
        moments=moments(),
        flows=doc("Flows", "flows", FLOWS),
        ad=doc("Art direction", "ad", AD),
        micro=doc("Microcopy", "micro", MICRO),
    )
    (HERE / "index.html").write_text(page)
    print("wrote", HERE / "index.html", len(page) // 1024, "KiB")


if __name__ == "__main__":
    build()
