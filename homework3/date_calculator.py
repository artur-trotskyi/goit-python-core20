"""
Перше завдання

Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.


Вимоги до завдання:

Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної.
Якщо задана дата пізніша за поточну, результат має бути від'ємним.
У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
Для роботи з датами слід використовувати модуль datetime Python.


Рекомендації для виконання:

Імпортуйте модуль datetime.
Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
Отримайте поточну дату, використовуючи datetime.today().
Розрахуйте різницю між поточною датою та заданою датою.
Поверніть різницю у днях як ціле число.


Критерії оцінювання:

Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
Читабельність коду: код повинен бути чистим і добре документованим.


Приклад:

Якщо сьогодні 5 травня 2021 року, виклик get_days_from_today("2021-10-09") повинен повернути 157,
оскільки 9 жовтня 2021 року є на 157 днів пізніше від 5 травня 2021 року.
"""

from datetime import datetime, date


def string_to_date(date_string: str) -> date:
    """
    Converts a string to a date object.
    """
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(
            f"Error: Date '{date_string}' does not match format 'YYYY-MM-DD', or is not a valid date, for example: 2021-10-09")


def get_days_from_today(date_string: str) -> int | str:
    """
    Calculates the number of days between the current date and the provided date string.
    """
    try:
        request_date = string_to_date(date_string)
        current_date = datetime.today().date()
        return (request_date - current_date).days
    except ValueError as e:
        return str(e)


# Example usage
print(get_days_from_today('2225-01-14'))
print(get_days_from_today('2005-01-14'))
print(get_days_from_today('1905-01-14'))
print(get_days_from_today('2025-01-41'))
print(get_days_from_today('20250141'))
print(get_days_from_today('test'))
