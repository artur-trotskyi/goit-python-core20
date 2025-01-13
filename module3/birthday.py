from typing import List, Dict, Any
from datetime import datetime, date, timedelta

users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.18"}
]


def string_to_date(date_string: str) -> date:
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date: date) -> str:
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def find_next_weekday(start_date: datetime.date, weekday: int) -> datetime.date:
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def get_upcoming_birthdays(users: List[Dict[str, Any]], days: int = 7) -> List[Dict[str, Any]]:
    upcoming_birthdays = []
    today = date.today()
    for user in users:
        # змінюємо рік на поточний
        congratulation_date = user['birthday'].replace(year=today.year)
        # перевірка чи дата не минула
        if congratulation_date < today:
            congratulation_date = user['birthday'].replace(year=today.year + 1)

        remaining_days = (congratulation_date - today).days
        if 0 <= remaining_days <= days:
            congratulation_date = adjust_for_weekend(congratulation_date)
            upcoming_birthdays.append(
                {"name": user["name"], "congratulation_date": date_to_string(congratulation_date)})

    return upcoming_birthdays


def adjust_for_weekend(birthday: datetime.date) -> datetime.date:
    return find_next_weekday(birthday, 0) if birthday.weekday() >= 5 else birthday


print(get_upcoming_birthdays(prepare_user_list(users), 7))
