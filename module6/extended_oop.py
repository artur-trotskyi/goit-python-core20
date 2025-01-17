################################################## Класи контейнери ##################################################


###################################################### UserDict ######################################################


# UserDict — це клас, що міститься в модулі collections і слугує обгорткою навколо словника.
# Він дозволяє легше створювати власні класи словників, модифікуючи або додаючи нову поведінку до стандартних методів словника.

from collections import UserDict

from collections import UserDict

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    }
]


class Customer(UserDict):
    def phone_info(self):
        return f"{self.get('name')}: {self.get('phone')}"

    def email_info(self):
        return f"{self.get('name')}: {self.get('email')}"


if __name__ == "__main__":
    customers = [Customer(el) for el in contacts]

    print("---------------------------")

    for customer in customers:
        print(customer.phone_info())

    print("---------------------------")

    for customer in customers:
        print(customer.email_info())

###################################################### UserList ######################################################

# UserList - це клас, який дозволяє створювати власні версії списків з додатковими функціями.
# Ви можете додавати нові методи або змінювати ті, що вже існують, щоб вони працювали по-іншому.
# Це корисно, коли вам потрібен список, який робить щось спеціальне, чого не робить звичайний список Python.

from collections import UserList


class MyList(UserList):
    # Додавання спеціалізованої поведінки. Наприклад, метод для додавання елемента, якщо він ще не існує
    def add_if_not_exists(self, item):
        if item not in self.data:
            self.data.append(item)


# Створення екземпляру MyList
my_list = MyList([1, 2, 3])
print("Оригінальний список:", my_list)

# Додавання елементу, якщо він не існує
my_list.add_if_not_exists(3)  # Не додасться, бо вже існує
my_list.add_if_not_exists(4)  # Додасться, бо ще не існує
print("Оновлений список:", my_list)


##################

class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))


countable = CountableList([1, '2', 3, '4'])
countable.append('5')
print(countable.sum())

###################################################### UserString ######################################################

# Він дозволяє створювати класи, які наслідують поведінку звичайного рядка, з можливістю додавання нових методів або
# зміни стандартної поведінки рядків. Це корисно, коли вам потрібно працювати з рядками спеціалізованим чином,
# який не підтримується стандартними рядками Python.

from collections import UserString


# Створення класу, який розширює UserString
class MyString(UserString):
    # Додавання методу, який перевіряє, чи рядок є паліндромом
    def is_palindrome(self):
        return self.data == self.data[::-1]


# Створення екземпляру MyString
my_string = MyString("radar")
print("Рядок:", my_string)
print("Чи є паліндромом?", my_string.is_palindrome())

# Створення іншого екземпляру MyString
another_string = MyString("hello")
print("Рядок:", another_string)
print("Чи є паліндромом?", another_string.is_palindrome())


# показує модифікований рядок з методом truncate, який обмежує розмір рядка до MAX_LEN символів.

class TruncatedString(UserString):
    MAX_LEN = 7

    def truncate(self):
        self.data = self.data[:self.MAX_LEN]


ts = TruncatedString('hello world!')
ts.truncate()
print(ts)


##################################################### Collections #####################################################


class Phones(UserList):
    def set_phone(self, phone):
        self.data.append(phone)

    def get_phones(self):
        return self.data


class User(UserDict):
    def set_name(self, name):
        self.data['name'] = name

    def get_name(self):
        return self.data.get('name')

    def set_phone(self, phone):
        phone_list = self.data.get('phones', Phones())
        phone_list.data.append(phone)
        self.data['phones'] = phone_list

    def get_phones(self):
        return self.data.get('phones')


user_1 = User()
user_1.set_name('Bill')
user_1.set_phone('09889465468')
user_1.set_phone('06895951111')
print(user_1.get_name(), user_1.get_phones())

###################################################### @dataclass ######################################################

from dataclasses import dataclass


@dataclass
class Rectangle:
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height


rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
rect3 = Rectangle(8, 6)

print(f"Площа прямокутника 1: {rect1.area()}")
print(f"Площа прямокутника 2: {rect2.area()}")
print(f"Площа прямокутника 3: {rect3.area()}")

##################################################### Enumeration #####################################################

from enum import Enum, auto


class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()


class Order:
    def __init__(self, name: str, status: OrderStatus):
        self.name = name
        self.status = status

    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

    def display_status(self):
        print(f"Статус замовлення '{self.name}': {self.status.name}.")


order1 = Order("Ноутбук", OrderStatus.NEW)
order2 = Order("Книга", OrderStatus.NEW)

order1.display_status()
order2.display_status()

order1.update_status(OrderStatus.PROCESSING)
order2.update_status(OrderStatus.SHIPPED)

order1.display_status()
order2.display_status()


##################################################### Агрегація #####################################################

class Owner:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"


class Cat:
    def __init__(self, nickname: str, age: int, owner: Owner):
        self.nickname = nickname
        self.age = age
        self.owner = owner

    def get_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"

    def sound(self):
        return "Meow"


owner = Owner("Boris", "+380503002010")
cat = Cat("Simon", 4, owner)

print(cat.owner.info())
print(cat.get_info())


##################################################### Композиція #####################################################

class Task:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Задача: {self.name}, Опис: {self.description}")


class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list(Task) = []

    def add_task(self, name: str, description: str):
        self.tasks.append(Task(name, description))

    def remove_task(self, name: str):
        self.tasks = [task for task in self.tasks if task.name != name]

    def display_project_info(self):
        print(f"Проект: {self.name}")
        for task in self.tasks:
            task.display_info()


# Створення проекту
my_project = Project("Веб-розробка")

# Додавання задач
my_project.add_task("Дизайн інтерфейсу", "Створити макет головної сторінки.")
my_project.add_task("Розробка API", "Реалізувати ендпоінти для користувачів.")

# Відображення інформації про проект
my_project.display_project_info()

# Видалення задачі
my_project.remove_task("Розробка API")

# Перевірка видалення задачі
my_project.display_project_info()

#################################################### Власні винятки ####################################################

try:
    # Код, який може викликати виняток
    result = 10 / 0
except ZeroDivisionError:
    # Обробка винятку ділення на нуль
    print("Ділення на нуль!")
except Exception as e:
    # Обробка будь-якого іншого винятку
    print(f"Виникла помилка: {e}")
else:
    # Виконується, якщо виняток не був викликаний
    print("Все пройшло успішно!")
finally:
    # Виконується завжди, незалежно від того, був виняток чи ні
    print("Блок finally завжди виконується.")


########################


# Визначення власного класу винятку
class AgeVerificationError(Exception):
    def __init__(self, message="Вік не задовольняє мінімальній вимозі"):
        self.message = message
        super().__init__(self.message)


# Функція для перевірки віку
def verify_age(age: int):
    if age < 18:
        raise AgeVerificationError("Вік особи меньший за 18 років")


if __name__ == "__main__":
    # Обробка винятку
    try:
        verify_age(16)  # Змініть вік для різних результатів
    except AgeVerificationError as e:
        print(f"Виняток: {e}")
    else:
        print("Вік перевірено, особа доросла.")


########################


class NameTooShortError(Exception):
    pass


class NameStartsFromLowError(Exception):
    pass


def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameTooShortError("Name is too short, need more than 2 symbols")
    if not name[0].isupper():
        raise NameStartsFromLowError("Name should start from capital letter")
    return name


if __name__ == "__main__":
    try:
        name = enter_name()
        print(f"Hello, {name}")
    except (NameTooShortError, NameStartsFromLowError) as e:
        print(e)
