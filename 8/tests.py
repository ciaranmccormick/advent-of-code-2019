from main import build_layers, count_digits, get_layer_with_min_digit, decode_image


def test_build_layers():
    image = "123456789012"
    image = [int(pixel) for pixel in image]
    width = 3
    height = 2
    expected = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 0, 1, 2]]
    assert expected == build_layers(image, width, height)


def test_count_digits():
    test_input = [1, 2, 4, 5, 6, 7, 6]
    expected = 2
    assert expected == count_digits(test_input, 6)


def test_get_layer_with_max_digit():
    test_input = [[1, 2, 3, 3], [1, 2, 3, 4], [1, 2, 3, 3]]
    actual = get_layer_with_min_digit(test_input, 3)
    expected = [1, 2, 3, 4]
    assert expected == actual


def test_decode_image():
    width = 2
    height = 2
    image = "0222112222120000"
    image = [int(pixel) for pixel in image]
    layers = build_layers(image, width, height)
    actual = decode_image(layers)
    expected = [0, 1, 1, 0]
    assert expected == actual
