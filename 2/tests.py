from computer import Computer
from main import load_instructions
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
        ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
        ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ],
)
def test_computer_run(test_input, expected):
    computer = Computer(test_input)
    assert expected == computer.run()


def test_load_intcode():
    here = Path(__file__).parent.absolute()
    filepath = here.joinpath("inputs.txt")
    with open(filepath, "r") as f:
        expected = int(f.readline()[0])
    assert expected, load_instructions(filepath)[0]
