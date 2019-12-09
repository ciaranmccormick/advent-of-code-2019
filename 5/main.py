#! /bin/env python3

from argparse import ArgumentParser, Namespace
from typing import List

from computer import Computer


def load_instructions(filename: str) -> List[int]:
    """Read in a list of comma separated integers"""
    with open(filename, "r") as f:
        codes = f.readline().split(",")
        codes = [int(code) for code in codes]
        return codes


def parse_args() -> Namespace:
    """Parse arguments."""
    parser = ArgumentParser()
    parser.add_argument("filename", help="File containing problem inputs.", type=str)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    program = load_instructions(args.filename)

    comp = Computer(program, 1)
    answer1 = comp.run()
    print(f"Part One output={answer1}")

    comp = Computer(program, 5)
    answer2 = comp.run()
    print(f"Part Two output={answer2}")


if __name__ == "__main__":
    main()
