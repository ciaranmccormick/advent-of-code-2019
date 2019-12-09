from argparse import ArgumentParser, Namespace
from collections import namedtuple
from typing import List, Optional

Orbit = namedtuple("Orbit", "centre,orbiter")


def load_orbits(filename: str):
    with open(filename, "r") as f:
        lines = f.readlines()
        lines = [line.replace("\n", "") for line in lines]
        orbits = [Orbit(*line.split(")")) for line in lines]
    return orbits


def number_of_transfers(start: str, end: str, orbits: List[Orbit]):
    common_orbit = get_first_common_orbit(start, end, orbits)
    start_to_common = moves_between_orbits(start, common_orbit, orbits)
    end_to_common = moves_between_orbits(end, common_orbit, orbits)
    return start_to_common + end_to_common


def get_first_common_orbit(body1: str, body2: str, orbits: List[Orbit]) -> str:
    bodies1 = [get_direct_orbit(body1, orbits)] + get_indirect_orbits(body1, orbits)
    bodies2 = [get_direct_orbit(body2, orbits)] + get_indirect_orbits(body2, orbits)
    for b in bodies1:
        if b in bodies2:
            return b


def moves_between_orbits(src: str, dest: str, orbits: List[Orbit]) -> int:
    io = get_direct_orbit(src, orbits)
    total = 0
    while True:
        total += 1
        io = get_direct_orbit(io, orbits)
        if io == dest or io is None:
            break
    return total


def get_indirect_orbits(name: str, orbits: List[Orbit]) -> Optional[List[str]]:
    io = get_direct_orbit(name, orbits)
    indirect_orbits = []
    while True:
        io = get_direct_orbit(io, orbits)
        if io is None:
            break
        indirect_orbits.append(io)

    return indirect_orbits


def get_direct_orbit(name: str, orbits: List[Orbit]) -> Optional[str]:
    for orbit in orbits:
        if orbit.orbiter == name:
            return orbit.centre


def get_total_orbits(name: str, orbits: List[Orbit]) -> int:
    total = 0
    direct = get_direct_orbit(name, orbits)
    if direct is not None:
        total += 1

    indirect = get_indirect_orbits(name, orbits)
    total += len(indirect)
    return total


def get_total_map_orbits(orbits: List[Orbit]) -> int:
    centres = [o.centre for o in orbits]
    orbiters = [o.orbiter for o in orbits]
    bodies = list(set(centres + orbiters))
    total = sum([get_total_orbits(body, orbits) for body in bodies])
    return total


def parse_args() -> Namespace:
    """Parse arguments."""
    parser = ArgumentParser()
    parser.add_argument("filename", help="File containing problem inputs.", type=str)
    args = parser.parse_args()
    return args


def part_two(orbits: List[Orbit]):
    total = number_of_transfers("YOU", "SAN", orbits)
    return total


def part_one(orbits: List[Orbit]):
    total = get_total_map_orbits(orbits)
    return total


def main():
    args = parse_args()
    orbits = load_orbits(args.filename)
    assert orbits[0] == Orbit("LH2", "LD6")
    total_orbits = part_one(orbits)
    print(f"Part One answer: {total_orbits}")
    total_transfers = part_two(orbits)
    print(f"Part Two answer: {total_transfers}")


if __name__ == "__main__":
    main()
