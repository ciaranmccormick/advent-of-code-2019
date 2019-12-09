#! /bin/env python3

from argparse import ArgumentParser, Namespace
from typing import List

BLACK = 0
WHITE = 1
TRANS = 2


def read_pixels(filename: str) -> List[int]:
    """Read in a list of comma separated integers"""
    with open(filename, "r") as f:
        pixels = f.readline().replace("\n", "")
        pixels = [int(pixel) for pixel in pixels]
        return pixels


def parse_args() -> Namespace:
    """Parse arguments."""
    parser = ArgumentParser()
    parser.add_argument("filename", help="File containing problem inputs.", type=str)
    args = parser.parse_args()
    return args


def build_layers(image: List[int], width: int, height: int) -> List[List[int]]:
    layers = []
    chunk_size = width * height
    i = 0
    while i < len(image):
        chunk = image[i : i + chunk_size]
        layers.append(chunk)
        i += chunk_size
    return layers


def count_digits(layer: List[int], digit: int):
    return len([pixel for pixel in layer if pixel == digit])


def get_layer_with_min_digit(layers: List[List[int]], digit: int) -> List[int]:
    min_layer = None
    min_count = len(layers[0])
    for layer in layers:
        digit_count = count_digits(layer, digit)
        if digit_count < min_count:
            min_layer = layer
            min_count = digit_count

    return min_layer


def decode_image(layers: List[List[int]]) -> List[int]:
    layer_len = len(layers[0])

    i = 0
    final_image = []
    while i < layer_len:
        final_image.append(TRANS)
        for layer in layers:
            visible_pixel = layer[i]
            if visible_pixel == BLACK:
                final_image[i] = BLACK
                break
            elif visible_pixel == WHITE:
                final_image[i] = WHITE
                break

        i += 1
    return final_image


def print_image(image: List[int], width: int, height: int):

    i = 0
    while i < height:
        start = i * width
        row = image[start : start + width]
        print(" ".join([str(digit) for digit in row]).replace("0", " "))
        i += 1


def part_two(image: List[int], width: int, height: int):
    layers = build_layers(image, width, height)
    decoded_image = decode_image(layers)
    print_image(decoded_image, width, height)


def part_one(image: List[int], width: int, height: int) -> int:
    layers = build_layers(image, width, height)
    layer = get_layer_with_min_digit(layers, 0)
    ones = count_digits(layer, 1)
    twos = count_digits(layer, 2)

    return ones * twos


def main():
    args = parse_args()
    width = 25
    height = 6
    image = read_pixels(args.filename)
    answer = part_one(image, width, height)
    print(f"Answer to Part One = {answer}")
    part_two(image, width, height)


if __name__ == "__main__":
    main()
