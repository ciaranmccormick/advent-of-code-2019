from computer import Computer, get_opcode, Instruction, process_instruction
import pytest


@pytest.mark.parametrize("test_input,expected", [("02", 2), ("01", 1), ("99", 99)])
def test_get_opcode(test_input, expected):
    assert expected == get_opcode(test_input)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (1002, Instruction(2, 0, 1, 0)),
        (10001, Instruction(1, 0, 0, 1)),
        (99, Instruction(99, 0, 0, 0)),
    ],
)
def test_read_instruction(test_input, expected):
    assert expected == process_instruction(test_input)


def test_process_opcodes():
    test_input = [3, 0, 4, 0, 99]
    expected = 1
    comp = Computer(test_input, 1)
    assert expected == comp.run()

