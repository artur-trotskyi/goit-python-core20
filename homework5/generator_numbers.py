import re
from typing import Callable, List


def generator_numbers(text: str) -> List[float]:
    """
    Generates floating-point numbers from the text.

    :param text: Input text in which numbers are searched.
    :yield: Floating-point numbers as floats.
    """
    # Regular expression for finding numbers
    pattern = r'\b\d+\.\d+|\b\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable) -> float:
    """
    Calculates the total profit from the text using a generator function.

    :param text: Input text containing numbers.
    :param func: Generator function for extracting numbers.
    :return: Total sum of the numbers (profit).
    """
    return sum(func(text))


def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == "__main__":
    main()
