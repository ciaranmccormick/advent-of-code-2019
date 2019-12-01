from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import List


def load_masses(filepath: Path) -> List[int]:
    """Read in a file containing masses."""
    with open(filepath, "r") as f:
        lines = f.readlines()

    lines = [int(line.replace("\n", "")) for line in lines]
    return lines


def calculate_total_fuel(mass: int) -> int:
    """Recursively calculate the required fuel."""
    fuel = calculate_required_fuel(mass)
    if fuel == 0:
        return fuel
    else:
        return fuel + calculate_total_fuel(fuel)


def calculate_required_fuel(mass: int) -> int:
    """Calculate amount of fuel for a required mass."""
    fuel = mass // 3 - 2
    if fuel < 1:
        return 0
    else:
        return fuel


def part_one(masses: List[int]):
    total_fuel = sum([calculate_required_fuel(mass) for mass in masses])
    return total_fuel


def part_two(masses: List[int]):
    total_fuel = sum([calculate_total_fuel(mass) for mass in masses])
    return total_fuel


def parse_args() -> Namespace:
    """Parse arguments."""
    parser = ArgumentParser()
    parser.add_argument("filename", help="File containing problem inputs.", type=str)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    masses = load_masses(args.filename)
    total_fuel = part_one(masses)
    print(f"Part One answer: {total_fuel}")
    total_fuel = part_two(masses)
    print(f"Part Two answer: {total_fuel}")


if __name__ == "__main__":
    main()
