import pytest
from parser.parser import Parser


def test_parse_x():
    input_string = "x"
    parser = Parser(input_string)
    result = parser.parse()
    assert result


def test_parse_x_neg():
    input_string = "-x"
    parser = Parser(input_string)
    result = parser.parse()
    assert result


def test_parse_x_power():
    input_string = "x^3"
    parser = Parser(input_string)
    result = parser.parse()
    assert result


def test_parse_neg_3x():
    input_string = "-3x"
    parser = Parser(input_string)
    result = parser.parse()
    assert result


def test_parse_complex_example():
    input_string = "x^2-28x^120+467x^2+x-1200"
    parser = Parser(input_string)
    result = parser.parse()
    assert result


@pytest.mark.parametrize(
    "input_string",
    [
        "0x",
        "1x^3",
        "1x",
        "-1x",
        "x+0",
        "0+x",
        "x^0",
        "x^1",
        "x^-25",
    ],
)
def test_invalid_inputs(input_string):
    parser = Parser(input_string)
    with pytest.raises(SyntaxError):
        tree = parser.parse()
        assert tree == []
