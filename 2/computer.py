from typing import List


class Computer:
    STOP = 99
    ADD = 1
    MULTIPLY = 2

    def __init__(self, intcodes: List[int]):
        self.intcodes = list(intcodes)
        self.pointer = 0
        self.prog_size = len(intcodes)

    def add(self):
        pos1, pos2, dest = self.get_parameters(3)
        value1 = self.intcodes[pos1]
        value2 = self.intcodes[pos2]
        self.intcodes[dest] = value1 + value2
        self.pointer += 4

    def multiply(self):
        pos1, pos2, dest = self.get_parameters(3)
        value1 = self.intcodes[pos1]
        value2 = self.intcodes[pos2]
        self.intcodes[dest] = value1 * value2
        self.pointer += 4

    def get_parameters(self, num):
        return self.intcodes[self.pointer + 1 : self.pointer + num + 1]

    def run(self):
        while self.pointer < self.prog_size:
            opcode = self.intcodes[self.pointer]
            if opcode == self.STOP:
                break
            elif opcode == self.ADD:
                self.add()
            elif opcode == self.MULTIPLY:
                self.multiply()

        return self.intcodes

