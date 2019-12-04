import unittest

from daythree import (
    Point,
    generate_points,
    get_intersections,
    steps_taken,
    part_one,
    part_two,
)
from collections import namedtuple


class DayThreeTest(unittest.TestCase):
    def test_generate_points(self):
        inputs = [
            (
                ["R2", "D3"],
                [Point(1, 0), Point(2, 0), Point(2, -1), Point(2, -2), Point(2, -3)],
            ),
            (["D3", "L1"], [Point(0, -1), Point(0, -2), Point(0, -3), Point(-1, -3)],),
            (["L2", "U2"], [Point(-1, 0), Point(-2, 0), Point(-2, 1), Point(-2, 2)],),
            (
                ["U3", "R2"],
                [Point(0, 1), Point(0, 2), Point(0, 3), Point(1, 3), Point(2, 3)],
            ),
        ]
        for data in inputs:
            with self.subTest(data=data):
                actual = generate_points(Point(0, 0), data[0])
                assert sorted(data[1]) == sorted(actual)

    def test_part_one(self):
        TestData = namedtuple("TestData", "wire_one,wire_two,expected")
        inputs = [
            TestData(
                ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
                ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
                159,
            ),
            TestData(
                [
                    "R98",
                    "U47",
                    "R26",
                    "D63",
                    "R33",
                    "U87",
                    "L62",
                    "D20",
                    "R33",
                    "U53",
                    "R51",
                ],
                ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"],
                135,
            ),
            TestData(["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"], 6),
        ]
        for data in inputs:
            with self.subTest(data=data):
                points1 = generate_points(Point(0, 0), data.wire_one)
                points2 = generate_points(Point(0, 0), data.wire_two)
                intersections = get_intersections(points1, points2)
                assert data.expected == part_one(intersections)

    def test_part_two(self):
        TestData = namedtuple("TestData", "wire_one,wire_two,expected")
        inputs = [
            TestData(
                ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
                ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
                610,
            ),
            TestData(
                [
                    "R98",
                    "U47",
                    "R26",
                    "D63",
                    "R33",
                    "U87",
                    "L62",
                    "D20",
                    "R33",
                    "U53",
                    "R51",
                ],
                ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"],
                410,
            ),
            TestData(["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"], 30),
        ]
        for data in inputs:
            with self.subTest(data=data):
                points1 = generate_points(Point(0, 0), data.wire_one)
                points2 = generate_points(Point(0, 0), data.wire_two)
                intersections = get_intersections(points1, points2)
                assert data.expected == part_two(intersections, points1, points2)

    def test_intersections(self):
        p1 = [Point(1, 1), Point(1, 2), Point(1, 3)]
        p2 = [Point(5, 6), Point(6, 6), Point(6, 7)]
        actual = get_intersections(p1, p2)
        assert [] == actual
        p1 = [Point(1, 1), Point(1, 2), Point(1, 3)]
        p2 = [Point(1, 2), Point(2, 2), Point(3, 2)]
        actual = get_intersections(p1, p2)
        assert [Point(1, 2)] == actual

    def test_number_of_steps(self):
        point = Point(3, 3)
        points1 = generate_points(Point(0, 0), ["R8", "U5", "L5", "D3"])
        expected = 20
        actual = steps_taken(point, points1)
        assert expected == actual
        points2 = generate_points(Point(0, 0), ["U7", "R6", "D4", "L4"])
        actual = steps_taken(point, points2)
        assert expected == actual

        point = Point(6, 5)
        points1 = generate_points(Point(0, 0), ["R8", "U5", "L5", "D3"])
        expected = 15
        actual = steps_taken(point, points1)
        assert expected == actual
        points2 = generate_points(Point(0, 0), ["U7", "R6", "D4", "L4"])
        actual = steps_taken(point, points2)
        assert expected == actual


if __name__ == "__main__":
    unittest.main()
