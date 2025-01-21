############################### Упакування у byte-рядки та розпакування із byte-рядків ###############################

"""
Для серіалізації/десеріалізації об'єктів Python, коли важлива швидкість, коректність і невеликий розмір пам'яті,
що використовується, найкраще підійде пакет pickle.
У пакета pickle є дві пари парних методів:
Перша пара методів - це dumps, який упаковує в byte-рядок об'єкт, і loads - він розпаковує з byte-рядки в об'єкт.
Ці методи потрібні, коли ми хочемо контролювати, що робити з byte поданням, наприклад, відправити його по мережі
або прийняти з мережі.
"""
import pickle

some_data = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}

byte_string = pickle.dumps(some_data)
unpacked = pickle.loads(byte_string)

print(unpacked == some_data)  # True
print(unpacked is some_data)  # False

"""
У цьому прикладі упакований у byte_string словник some_data розпакован в unpacked та unpacked суворо дорівнює some_data, 
але це все ж таки не той самий об'єкт.
Друга пара методів: dump та load - вони упаковують у відкритий для byte-запису файл і розпаковують з відкритого для 
byte-читання файлу.

"""

import pickle

some_data = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}

file_name = 'data.bin'

with open(file_name, "wb") as fh:
    pickle.dump(some_data, fh)

with open(file_name, "rb") as fh:
    unpacked = pickle.load(fh)

print(unpacked == some_data)  # True
print(unpacked is some_data)  # False
"""
Результат аналогічний попередньому прикладу.
Головна відмінність у тому, що під час виконання цього коду в робочій папці з'явився файл data.bin.
"""

############################### Упакування у byte-рядки та розпакування із byte-рядків ###############################

import pickle

# Об'єкт для серіалізації
my_data = {"key": "value", "num": 42}

# Серіалізація об'єкта в байтовий рядок
serialized_data = pickle.dumps(my_data)
# Виведе байтовий рядок
print(serialized_data)

# Десеріалізація об'єкта з байтового рядка
deserialized_data = pickle.loads(serialized_data)
# Виведе вихідний об'єкт Python
print(deserialized_data)

##################################### Упакування у файл та розпакування з файлу #####################################

import pickle

# Список контактів для серіалізації
contacts = [
    {"name": "Alice", "phone": "123456789"},
    {"name": "Bob", "phone": "987654321"},
    {"name": "Charlie", "phone": "555555555"},
]

# Серіалізація даних у файл
with open("contacts.pickle", "wb") as file:
    pickle.dump(contacts, file)

print("Contacts serialized and saved to 'contacts.pickle'.")

import pickle

# Десеріалізація даних з файлу
with open("contacts.pickle", "rb") as file:
    restored_contacts = pickle.load(file)

print("Restored contacts:")
for contact in restored_contacts:
    print(f"Name: {contact['name']}, Phone: {contact['phone']}")

####################################################### Faker #######################################################

from faker import Factory, Faker
import json

fake = Faker(locale='uk_UA')

users = []


def create_users(user_list, n=10):
    for _ in range(n):
        user_list.append({
            'name': fake.name(),
            'phone_number': fake.phone_number(),
            'email': fake.email(),
            'address': fake.address(),
            'birthday': fake.date()
        })
    to_json(user_list)


def to_json(user_list):
    with open('users.json', 'w', encoding='utf-8') as file:
        json.dump(user_list, file, indent=4, ensure_ascii=False)
        print('Users were saved.')


create_users(users, 12)

from csv import DictWriter
import json

file_json = 'users.json'
file_csv = 'users_new.csv'


def get_users():
    with open(file_json) as reader:
        users = json.load(reader)
        return users


def write_table():
    users = get_users()
    with open(file_csv, 'w', encoding='utf-8', newline='') as file:
        fieldsnames = users[0].keys()
        writer = DictWriter(file, delimiter=';', fieldnames=fieldsnames)
        writer.writeheader()
        for row in users:
            writer.writerow(rowdict=row)
        print('CSV table was created.')


write_table()

############################################# Робота з класами користувача #############################################

# Збереження налаштувань
settings = {'theme': 'dark', 'language': 'ukrainian'}
with open('settings.pickle', 'wb') as f:
    pickle.dump(settings, f)

# Завантаження налаштувань
with open('settings.pickle', 'rb') as f:
    loaded_settings = pickle.load(f)

#################################### Серіалізація об'єктів Python за допомогою JSON ####################################

import json

some_data = {
    "key": "value",
    2: [1, 2, 3],
    "my_tuple": (5, 6),
    "my_dict": {"key": "value"},
}

json_string = json.dumps(some_data)
print(json_string)
unpacked_some_data = json.loads(json_string)
print(unpacked_some_data)

### якщо у файл

import json

# Python об'єкт (словник)
data = {"name": "Gupalo Vasyl", "age": 30, "isStudent": True}

# Серіалізація у файл
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

# Десеріалізація з файлу
with open("data.json", "r", encoding="utf-8") as f:
    data_from_file = json.load(f)
    print(data_from_file)

### виправити та записати дані в файл JSON, використовуючи кирилицю
# Python об'єкт (словник)
data = {"name": "Гупало Василь", "age": 30, "isStudent": True}

# Серіалізація у файл
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

########################################## Робота з таблицями CSV у Python ##########################################

import csv

# Дані для запису
rows = [
    ["name", "age", "specialty"],
    ["Василь Гупало", 30, "Математика"],
    ["Марія Петренко", 22, "Фізика"],
    ["Олександр Коваленко", 20, "Інформатика"],
]

# Відкриваємо файл для запису
with open("data.csv", "w", newline="", encoding="utf-8") as csvfile:
    # Створюємо об'єкт writer
    writer = csv.writer(csvfile, delimiter=",")
    # Записуємо рядки даних
    writer.writerows(rows)

# Відкриваємо CSV файл
with open("data.csv", newline="", encoding="utf-8") as csvfile:
    # Створюємо об'єкт reader
    reader = csv.reader(csvfile, delimiter=",")
    # Проходимося по кожному рядку у файлі
    for row in reader:
        print(", ".join(row))

"""
Використання DictReader і DictWriter полегшує доступ до полів за їхніми назвами та автоматизує процес запису заголовків стовпців.
"""

import csv

# Запис у CSV файл зі словників
with open("students.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["name", "age", "specialty"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"name": "Олег Олегов", "age": 23, "specialty": "Історія"})
    writer.writerow({"name": "Анна Сергіївна", "age": 22, "specialty": "Біологія"})

# Читання з CSV файлу в словники
with open("students.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["name"], row["age"], row["specialty"])

### Наступний приклад:
import csv

FILENAME = "users.csv"

users = [
    {"name": "Микола", "age": 22, "gender": "male"},
    {"name": "Марія", "age": 22, "gender": "female"},
    {"name": "Назар", "age": 22, "gender": "male"},
]

with open(FILENAME, "w", encoding="utf-8", newline="") as f:
    columns = users[0].keys()
    writer = csv.DictWriter(f, delimiter=",", fieldnames=columns)
    writer.writeheader()
    for row in users:
        writer.writerow(row)

with open(FILENAME, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)
