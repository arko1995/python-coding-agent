import sys
from pkg.calculator import Calculator
from pkg.render import format_json_output


def main() -> None:
    if len(sys.argv) < 1:
        calculator = Calculator()
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    expression = " ".join(sys.argv[1:])

    try:
        result = calculator.evaluate(expression)

        if result is not None:
            to_print = format_json_output(expression, result)
            print(to_print)

        else:
            print("Error: Expression is empty or contains only white spaces")
    except Exception as error:
        print(f"Error {error}")


if __name__ == "__main__":
    main()
