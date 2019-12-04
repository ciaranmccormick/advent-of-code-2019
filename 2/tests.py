from main import process_opcodes, load_instructions
from collections import namedtuple
from pathlib import Path
import unittest

TestData = namedtuple("TestData", "test_input,expected")

process_opcodes_test_data = (
    TestData([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
    TestData([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
    TestData([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
    TestData([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
)


class TestDayTwo(unittest.TestCase):
    def test_process_opcodes(self):
        for data in process_opcodes_test_data:
            with self.subTest(data=data):
                actual = process_opcodes(data.test_input)
                self.assertListEqual(data.expected, actual)

    def test_load_intcode(self):
        here = Path(__file__).parent.absolute()
        filepath = here.joinpath("inputs.txt")
        with open(filepath, "r") as f:
            expected = int(f.readline()[0])
        self.assertEqual(expected, load_instructions(filepath)[0])


if __name__ == "__main__":
    unittest.main()
