from collections import namedtuple
from typing import List

Instruction = namedtuple("Instruction", "opcode,mode1,mode2,mode3")
POSITION = 0


def get_opcode(opcode: str) -> int:
    total = 0
    for i, digit in enumerate(reversed(opcode)):
        total += int(digit) * pow(10, i)

    return total


def process_instruction(instruction: int):
    instruction = f"{instruction:0>5}"
    opcode = instruction[-2:]
    opcode = get_opcode(opcode)
    modes = [int(mode) for mode in reversed(instruction[:3])]
    return Instruction(opcode, *modes)


class Computer:
    STOP = 99
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMPIFTRUE = 5
    JUMPIFFALSE = 6
    LESSTHAN = 7
    EQUALS = 8

    def __init__(self, intcodes: List[int], value: int):
        self.intcodes = list(intcodes)
        self.pointer = 0
        self.prog_size = len(intcodes)
        self.value = value

    def add(self, *modes):
        value1, value2 = self.get_parameters(*modes[:2])
        dest = self.intcodes[self.pointer + 3]
        self.intcodes[dest] = value1 + value2
        self.pointer += 4

    def multiply(self, *modes):
        value1, value2 = self.get_parameters(*modes[:2])
        dest = self.intcodes[self.pointer + 3]
        self.intcodes[dest] = value1 * value2
        self.pointer += 4

    def input(self, value: int):
        dest = self.intcodes[self.pointer + 1]
        self.intcodes[dest] = value
        self.pointer += 2

    def output(self):
        src = self.intcodes[self.pointer + 1]
        self.pointer += 2
        return self.intcodes[src]

    def jump_if_true(self, *modes):
        value1, value2 = self.get_parameters(*modes[:2])
        if value1 != 0:
            self.pointer = value2
        else:
            self.pointer += 3

    def jump_if_false(self, *modes):
        value1, value2 = self.get_parameters(*modes[:2])
        if value1 == 0:
            self.pointer = value2
        else:
            self.pointer += 3

    def less_than(self, *modes):
        value1, value2 = self.get_parameters(*modes[:2])
        dest = self.intcodes[self.pointer + 3]
        if value1 < value2:
            self.intcodes[dest] = 1
        else:
            self.intcodes[dest] = 0
        self.pointer += 4

    def equals(self, *modes):
        value1, value2 = self.get_parameters(*modes[:2])
        dest = self.intcodes[self.pointer + 3]

        if value1 == value2:
            self.intcodes[dest] = 1
        else:
            self.intcodes[dest] = 0

        self.pointer += 4

    def get_parameters(self, *modes):
        params = []
        for i, mode in enumerate(modes):
            if mode == POSITION:
                pos = self.intcodes[self.pointer + i + 1]
                params.append(self.intcodes[pos])
            else:
                val = self.intcodes[self.pointer + i + 1]
                params.append(val)

        return params

    def run(self):
        while self.pointer < self.prog_size:
            opcode, *modes = process_instruction(self.intcodes[self.pointer])

            if opcode == self.STOP:
                break
            elif opcode == self.ADD:
                self.add(*modes)
            elif opcode == self.MULTIPLY:
                self.multiply(*modes)
            elif opcode == self.INPUT:
                self.input(self.value)
            elif opcode == self.OUTPUT:
                self.out = self.output()
            elif opcode == self.JUMPIFTRUE:
                self.jump_if_true(*modes)
            elif opcode == self.JUMPIFFALSE:
                self.jump_if_false(*modes)
            elif opcode == self.LESSTHAN:
                self.less_than(*modes)
            elif opcode == self.EQUALS:
                self.equals(*modes)

        return self.out

