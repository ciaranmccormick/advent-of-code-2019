from argparse import ArgumentParser, Namespace
from collections import namedtuple
from typing import List, Tuple

LEFT = "L"
RIGHT = "R"
UP = "U"
DOWN = "D"

Point = namedtuple("Point", "x,y")
Points = List[Point]


def load_movements(filename: str) -> Tuple[List[str], List[str]]:
    """
    Reads a file with two lines, both with the format:
    'R34,L32,D45,U98,...\n'
    """
    with open(filename, "r") as f:
        wire_one = f.readline().replace("\n", "").split(",")
        wire_two = f.readline().replace("\n", "").split(",")
    return wire_one, wire_two


def generate_points(start: Point, moves: List[str]) -> Points:
    """
    Given a list of moves in the form ["R32", "L15", ...] and a starting point.
    Get a list of all the points "visited".
    """
    visited = []
    for move in moves:
        direction = move[0]
        mag = int(move[1:])

        x, y = start
        if direction == UP:
            # x stays the same, y increases
            points = [Point(x, i) for i in range(y + 1, y + 1 + mag)]
        elif direction == DOWN:
            # x stays the same, y decreases
            points = [Point(x, i) for i in range(y - 1, y - 1 - mag, -1)]
        elif direction == RIGHT:
            # y stays the same, x increases
            points = [Point(i, y) for i in range(x + 1, x + 1 + mag)]
        elif direction == LEFT:
            # y stays the same, x decreases
            points = [Point(i, y) for i in range(x - 1, x - 1 - mag, -1)]

        visited += points
        start = points[-1]

    return visited


def get_intersections(list1: Points, list2: Points) -> Points:
    """Returns all the points that exist in both lists"""
    return list(set(list1).intersection(list2))


def steps_taken(point: Point, points: Points):
    """
    Given a list of points find the location of point in the list.
    This is equivalent to the number of "step" taken.
    Add 1 since zero indexing.
    """
    steps = points.index(point) + 1
    return steps


def part_one(intersections: Points) -> int:
    """Get the intersection with the smallest Manhatten distance."""
    minimum = min([abs(p.x) + abs(p.y) for p in intersections])
    return minimum


def part_two(intersections: Points, wire_one: Points, wire_two: Points) -> int:
    """Get the intersection with the lowest number of steps taken."""
    steps = [
        steps_taken(point, wire_one) + steps_taken(point, wire_two)
        for point in intersections
    ]
    return min(steps)


def parse_args() -> Namespace:
    """Parse arguments."""
    parser = ArgumentParser()
    parser.add_argument("filename", help="File containing problem inputs.", type=str)
    args = parser.parse_args()
    return args


def main():
    origin = Point(0, 0)
    args = parse_args()

    moves1, moves2 = load_movements(args.filename)

    wire_one = generate_points(origin, moves1)
    wire_two = generate_points(origin, moves2)
    intersections = get_intersections(wire_one, wire_two)

    answer1 = part_one(intersections)
    print(f"Part One answer={answer1}")

    answer2 = part_two(intersections, wire_one, wire_two)
    print(f"Part Two answer={answer2}")


if __name__ == "__main__":
    main()
