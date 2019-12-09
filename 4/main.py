from argparse import ArgumentParser, Namespace
from typing import List


def contains_repeats(password: str) -> bool:
    """Test if a string of characters contains repeating characters,
       e.g. "123454" -> False
            "123354" -> True
            "111111" -> True
    """
    prev_digit = password[0]
    password = password[1:]
    for digit in password:
        if prev_digit == digit:
            return True
        prev_digit = digit
    return False


def always_increases(password: str) -> bool:
    """ Checks if a string of integers is always the same or increasing."""
    prev_digit = "0"
    for digit in password:
        if int(prev_digit) > int(digit):
            return False
        prev_digit = digit
    return True


def contains_more_than_two_repeats(password: str) -> bool:
    """Checks if password has characters that have more than 2 consecutive repeats."""

    prev_digit = password[0]
    password = password[1:]
    repeat = 0
    for digit in password:
        if prev_digit == digit:
            repeat += 1
        else:
            repeat = 0

        if repeat > 1:
            return True

        prev_digit = digit

    return False


def contains_two_repeats_only(password: str) -> bool:
    """Returns 2 if password has only 2 consecutive repeats."""
    prev = ""
    count = 1
    for digit in password:
        if prev == digit:
            count += 1
        else:
            if count == 2:
                break
            count = 1
        prev = digit

    if count == 2:
        return True
    return False


def part_one(start: int, end: int) -> List[str]:
    passwords = [str(password) for password in range(start, end + 1)]
    passwords = [
        password
        for password in passwords
        if contains_repeats(password) and always_increases(password)
    ]
    return passwords


def part_two(passwords: List[str]) -> List[str]:
    passwords = [
        password
        for password in passwords
        if not contains_more_than_two_repeats(password)
        or contains_two_repeats_only(password)
    ]
    return passwords


def parse_args() -> Namespace:
    """Parse arguments."""
    parser = ArgumentParser()
    parser.add_argument("start", help="Start of password range.", type=int)
    parser.add_argument("end", help="End of password range.", type=int)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    passwords = part_one(args.start, args.end)
    print(f"Part One answer={len(passwords)}")

    passwords = part_two(passwords)
    print(f"Part Two answer={len(passwords)}")


if __name__ == "__main__":
    main()
