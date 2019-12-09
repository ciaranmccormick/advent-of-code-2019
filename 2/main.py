#! /bin/env python3

from argparse import ArgumentParser, Namespace
from typing import List, Tuple
from computer import Computer

STOP = 99
ADD = 1
MULTIPLY = 2


def load_instructions(filename: str) -> List[int]:
    """Read in a list of comma separated integers"""
    with open(filename, "r") as f:
        codes = f.readline().split(",")
        codes = [int(code) for code in codes]
        return codes


def process_opcodes(opcodes: List[int]) -> List[int]:
    """
    Processes the list of opcodes and applies instructions.
    Returns the modified opcode list.
    """
    i = 0
    inputs = list(opcodes)  # make a copy of the list
    while i < len(inputs):
        opcode = inputs[i]
        if opcode == STOP:
            break

        pos1, pos2, dest = inputs[i + 1 : i + 4]
        val1 = inputs[pos1]
        val2 = inputs[pos2]

        if opcode == ADD:
            result = val1 + val2
        elif opcode == MULTIPLY:
            result = val1 * val2

        inputs[dest] = result
        i += 4
    return inputs


def part_two(intcodes: List[int]) -> Tuple[int, int]:
    """Get solution to Part Two"""
    for noun in range(1, 100):
        for verb in range(1, 100):
            intcodes[1] = noun
            intcodes[2] = verb
            comp = Computer(intcodes)
            processed = comp.run()
            if processed[0] == 19690720:
                return noun, verb


def part_one(opcodes: List[int]) -> int:
    """
    Get solution to Part One
    """
    opcodes[1] = 12
    opcodes[2] = 2
    comp = Computer(opcodes)
    codes = comp.run()
    return codes[0]


def parse_args() -> Namespace:
    """Parse arguments."""
    parser = ArgumentParser()
    parser.add_argument("filename", help="File containing problem inputs.", type=str)
    parser.add_argument(
        "multiplier", help="The number multiply noun and verb by.", type=int
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    opcodes = load_instructions(args.filename)

    zero_value = part_one(opcodes)
    print(f"Part One: answer={zero_value}")

    noun, verb = part_two(opcodes)
    part_two_answer = args.multiplier * noun + verb
    print(f"Part Two: noun={noun}, verb={verb}, answer={part_two_answer}")


if __name__ == "__main__":
    main()
