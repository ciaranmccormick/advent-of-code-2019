#! /bin/env python3

from argparse import ArgumentParser, Namespace
from itertools import permutations
from typing import List

from computer import Computer


def load_instructions(filename: str) -> List[int]:
    """Read in a list of comma separated integers"""
    with open(filename, "r") as f:
        codes = f.readline().split(",")
        codes = [int(code) for code in codes]
        return codes


def get_max_thruster_signal(amplifiers: List[int], phases: List[int]):
    return max(
        get_thruster_signal(amplifiers, p) for p in permutations(phases, len(phases))
    )


def get_thruster_signal(opcodes: List[int], phases: List[int]):
    out = 0
    for phase in phases:
        comp = Computer(opcodes)
        comp.value = out
        comp.input(phase)
        out = comp.run()

    return out


def loop_thruster_signal(intcodes: List[int], phases: List[int]):

    out = 0
    i = 0
    computers = []
    while True:
        if i // len(phases) == 0:
            phase = phases[i % len(phases)]
            comp = Computer(intcodes)
            comp.value = out
            computers.append(comp)
            comp.input(phase)
            out = comp.run()
        else:
            comp = computers[i % len(phases)]
            comp.value = out
            out = comp.run()

        if computers[-1].stop:
            return computers[-1].out
        i += 1


def get_max_loop_thruster_signal(amplifiers: List[int], phases: List[int]):
    return max(
        loop_thruster_signal(amplifiers, p) for p in permutations(phases, len(phases))
    )


def part_two(intcodes: List[int]):
    phases = range(5, 10)
    return get_max_loop_thruster_signal(intcodes, phases)


def part_one(opcodes: List[int]):
    phases = range(5)
    return get_max_thruster_signal(opcodes, phases)


def parse_args() -> Namespace:
    """Parse arguments."""
    parser = ArgumentParser()
    parser.add_argument("filename", help="File containing problem inputs.", type=str)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    intcodes = load_instructions(args.filename)
    answer1 = part_one(intcodes)
    print(f"Part One output = {answer1}")
    answer2 = part_two(intcodes)
    print(f"Part Two output = {answer2}")


if __name__ == "__main__":
    main()
