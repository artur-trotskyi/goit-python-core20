"""
Друге завдання

Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами,
що випали випадковим чином і в певному діапазоні під час чергового тиражу.
Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Вам необхідно написати функцію get_numbers_ticket(min, max, quantity),
яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.

Вона буде повертати випадковий набір чисел у межах заданих параметрів,
причому всі випадкові числа в наборі повинні бути унікальні.


Вимоги до завдання:

Параметри функції:
min - мінімальне можливе число у наборі (не менше 1).
max - максимальне можливе число у наборі (не більше 1000).
quantity - кількість чисел, які потрібно вибрати (значення між min і max).
Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
Функція повертає список випадково вибраних, відсортованих чисел.
Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.


Рекомендації для виконання:

Переконайтеся, що вхідні параметри відповідають заданим обмеженням.
Використовуйте модуль random для генерації випадкових чисел.
Використовуйте множину або інший механізм для забезпечення унікальності чисел.
Пам'ятайте, що функція get_numbers_ticket повертає відсортований список унікальних чисел.


Критерії оцінювання:

Валідність вхідних даних: функція повинна перевіряти коректність параметрів.
Унікальність результату: усі числа у видачі повинні бути унікальними.
Відповідність вимогам: результат має бути у вигляді відсортованого списку.
Читабельність коду: код має бути чистим і добре документованим.


Приклад:
Припустимо, вам потрібно вибрати 6 унікальних чисел для лотерейного квитка,
де числа повинні бути у діапазоні від 1 до 49. Ви можете використати вашу функцію так:


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

Цей код викликає функцію get_numbers_ticket з параметрами min=1, max=49 та quantity=6.
В результаті ви отримаєте список з 6 випадковими, унікальними та відсортованими числами,
наприклад, [4, 15, 23, 28, 37, 45]. Кожен раз при виклику функції ви отримуватимете різний набір чисел.
"""

import random
from typing import List


def get_numbers_ticket(min: int, max: int, quantity: int) -> List[int]:
    """
    Generates a sorted list of unique random numbers for a lottery ticket.

    :param min: Minimum number to include in the range (inclusive).
    :param max: Maximum number to include in the range (exclusive).
    :param quantity: Number of random unique numbers to generate.
    :return: Sorted list of random unique numbers.
    """
    try:
        validate_ticket_parameters(min, max, quantity)
        return sorted(random.sample(range(min, max), quantity))
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


def validate_ticket_parameters(min: int, max: int, quantity: int) -> None:
    """
    Validates the parameters for generating lottery ticket numbers.

    :param min: Minimum value in the range (inclusive).
    :param max: Maximum value in the range (exclusive, must not exceed 1000).
    :param quantity: Number of unique numbers to generate.
    :raises ValueError: If any parameter is invalid.
    """
    if not all(isinstance(param, int) for param in (min, max, quantity)):
        raise TypeError("All parameters must be integers.")
    if min < 1:
        raise ValueError("The minimum value must be at least 1.")
    if max > 1000:
        raise ValueError("The maximum value must not exceed 1000.")
    if max <= min:
        raise ValueError("The maximum value must be greater than the minimum value.")
    if quantity > max - min:
        raise ValueError("Quantity of numbers exceeds the available range.")


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket('1', 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(None, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(56, 4, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(999, 1000, 6)
print("Ваші лотерейні числа:", lottery_numbers)
