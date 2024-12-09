import json
from parser.parser import Parser


def show_hello():
    print("Welcome to the polynomial parser")
    print("Enter a polynomial to parse or press CTRL + C to quit")


def loop():
    input_string = input("Enter a polynomial: ")
    parser = Parser(input_string)
    try:
        result = parser.parse()
        print("Result syntax tree:")
        print(json.dumps(result, indent=2))
        print("Parsed successfully!")
    except SyntaxError as e:
        print("Failed to parse the polynomial")
        print("Error message:")
        print("\t", e)


def main():
    show_hello()
    while True:
        loop()


if __name__ == "__main__":
    main()
