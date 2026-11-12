"""Checks for the dotted circle in build.py (Spec §20 AAAAA; Art-Direction §3.2, §3.3).

    python3 -m unittest discover -s preview

Standard library only, like build.py. Importing build reads the docs and runs its own checks.
"""
import math
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

DOT = re.compile(r'<circle cx="([\d.]+)" cy="([\d.]+)" r="([\d.]+)"/>')
RING = re.compile(r'<g class="ring (ink|soft)" data-place="(\d+)">(.*?)</g>')


def dots(svg):
    return [tuple(float(x) for x in m) for m in DOT.findall(svg)]


def rings(svg):
    """{place: (ink, [(cx, cy, r), ...])}"""
    return {int(place): (ink, dots(body)) for ink, place, body in RING.findall(svg)}


def radius_of(dot):
    return math.hypot(dot[0] - 160, dot[1] - 160)


class WeekTests(unittest.TestCase):
    def test_the_first_week_holds_the_first_seven_days(self):
        self.assertEqual([build.week_of(d) for d in range(8)], [0] * 7 + [1])

    def test_week_52_takes_the_last_8_or_9_days(self):
        self.assertEqual(build.week_of(356), 50)
        self.assertEqual(build.week_of(357), 51)
        self.assertEqual(build.week_of(364), 51)  # day 365 of 365
        self.assertEqual(build.week_of(365), 51)  # day 366 of 366


class SizeTests(unittest.TestCase):
    def test_a_plain_ring_is_all_no_photo_dots(self):
        self.assertEqual(build.week_sizes(), [0] * 52)

    def test_many_photos_in_one_week_make_one_photo_dot(self):
        sizes = build.week_sizes(days=[0, 1, 2, 3, 6])
        self.assertEqual(sizes[0], 1)
        self.assertEqual(sum(1 for s in sizes if s), 1)

    def test_the_week_a_highlight_opened_is_the_biggest(self):
        sizes = build.week_sizes(days=[10, 200, 201], highlights=[200])
        self.assertEqual(sizes[200 // 7], 2)
        self.assertEqual(sizes[10 // 7], 1)

    def test_only_three_sizes_exist(self):
        sizes = build.week_sizes(days=range(0, 365, 3), highlights=[40, 41, 300])
        self.assertLessEqual(set(sizes), {0, 1, 2})


class RingTests(unittest.TestCase):
    def test_worked_values_match_the_art_direction(self):
        self.assertGreaterEqual(len(build.WORKED), 5)
        for row in build.WORKED:
            got = build.ring_values(int(row[0]))
            for mine, theirs in zip(got, row[1:]):
                self.assertAlmostEqual(mine, float(theirs), delta=0.006)

    def test_every_ring_has_52_dots_at_its_places_radii(self):
        for place in (1, 2, 5, 12):
            p, r, none, photo, high, gap = build.ring_values(place)
            svg = build.dot_ring(place, 3, build.week_sizes(days=[0, 100], highlights=[200]))
            ds = dots(svg)
            self.assertEqual(len(ds), 52)
            self.assertLessEqual({d[2] for d in ds}, {round(none, 2), round(photo, 2), round(high, 2)})
            for d in ds:
                self.assertAlmostEqual(radius_of(d), r, delta=0.02)

    def test_the_biggest_dots_never_touch(self):
        for place in (1, 2, 3, 8):
            p, r, none, photo, high, gap = build.ring_values(place)
            self.assertGreater(gap, 2 * high)
            p2, r2, _, _, high2, _ = build.ring_values(place + 1)
            self.assertGreater(r2 - r, high + high2)
        self.assertGreater(build.ring_values(1)[1] - build.ring_values(1)[4], build.CORE_R + 1)

    def test_no_dot_reaches_the_frames_crossing_ends(self):
        nums = [float(x) for x in re.findall(r"-?[\d.]+", build.PATHS["frame"])]
        ends = [(nums[0], nums[1]), (nums[-2], nums[-1])]
        reach = max(math.hypot(x - 160, y - 160) for x, y in ends)
        p, r, none, photo, high, gap = build.ring_values(1)
        self.assertGreater(r - high, reach + 1)


class CircleTests(unittest.TestCase):
    def owner_journey(self):
        return {"days": [0, 7, 14], "highlights": [], "length": 365}

    def test_no_rings_draws_the_frame_and_name_only(self):
        svg = build.circle("First Light")
        self.assertEqual(rings(svg), {})
        self.assertEqual(dots(svg), [])

    def test_the_newest_ring_is_next_to_the_frame(self):
        # Finishing order, oldest first: an even ring, then the owner's newest with three photo weeks
        svg = build.circle("Steady Lantern", [None, self.owner_journey()])
        rs = rings(svg)
        self.assertEqual(sorted(rs), [1, 2])
        inner_r = {d[2] for d in rs[1][1]}
        outer_r = {d[2] for d in rs[2][1]}
        self.assertEqual(len(inner_r), 2)  # no-photo and photo sizes: the newest journey
        self.assertEqual(len(outer_r), 1)  # the older, even ring
        self.assertLess(radius_of(rs[1][1][0]), radius_of(rs[2][1][0]))

    def test_the_newest_ring_is_the_brightest(self):
        rs = rings(build.circle("Long Way Round", [None, None, None]))
        self.assertEqual(rs[1][0], "ink")
        self.assertEqual({rs[2][0], rs[3][0]}, {"soft"})

    def test_a_ring_keeps_its_pattern_as_it_moves_out(self):
        def photo_angles(svg, place):
            _, ds = rings(svg)[place]
            small = min(d[2] for d in ds)
            return sorted(round(math.degrees(math.atan2(d[0] - 160, 160 - d[1])) % 360, 1) for d in ds if d[2] > small)
        alone = build.circle("Steady Lantern", [self.owner_journey()])
        later = build.circle("Steady Lantern", [self.owner_journey(), None])
        self.assertEqual(photo_angles(alone, 1), photo_angles(later, 2))

    def test_each_rings_dots_sit_halfway_between_the_next_rings(self):
        def angles(svg, place):
            return sorted(math.degrees(math.atan2(d[0] - 160, 160 - d[1])) % 360 for d in rings(svg)[place][1])
        svg = build.circle("Second Wind", [None] * 5)
        spacing = 360 / 52
        for place in (1, 2, 3, 4):
            offset = (angles(svg, place + 1)[0] - angles(svg, place)[0]) % spacing
            self.assertAlmostEqual(offset, spacing / 2, delta=0.05)

    def test_plain_circles_with_the_same_count_are_identical_apart_from_the_name(self):
        a = build.circle("Second Wind", [None] * 4).replace("Second", "X").replace("Wind", "Y")
        b = build.circle("Open Hands", [None] * 4).replace("Open", "X").replace("Hands", "Y")
        self.assertEqual(a, b)

    def test_any_count_fits_inside_the_box(self):
        ds = dots(build.circle("Second Wind", [None] * 40))
        self.assertEqual(len(ds), 40 * 52)
        self.assertLess(max(radius_of(d) + d[2] for d in ds), 160)

    def test_the_rings_carry_no_count_for_a_screen_reader(self):
        svg = build.circle("Second Wind", [None] * 6)
        self.assertNotIn("aria-label", svg)
        self.assertIn('aria-hidden="true"', svg)


if __name__ == "__main__":
    unittest.main()
