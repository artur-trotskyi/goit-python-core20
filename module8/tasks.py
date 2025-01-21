#################### Task 1

import pickle

contacts = {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

filename = 'test_file'


def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as fh:
        pickle.dump(contacts, fh)


def read_contacts_from_file(filename):
    with open(filename, "rb") as fh:
        return pickle.load(fh)


write_contacts_to_file(filename, contacts)
read_contacts_from_file(filename)

#################### Task 2

import json

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }
]


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump({'contacts': contacts}, file, indent=4, ensure_ascii=False)


def read_contacts_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as reader:
        return json.load(reader)['contacts']


filename = 'filename.json'

write_contacts_to_file(filename, contacts)
print(read_contacts_from_file(filename))

#################### Task 3

import csv

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }
]

filename = 'filename.csv'


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline="", encoding="utf-8") as csvfile:
        fieldnames = contacts[0].keys()
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)  # Запис усіх рядків за один раз
        print('CSV table was created.')


def read_contacts_from_file(filename):
    contacts_from_file = []
    with open(filename, 'r', newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            if 'favorite' in row:
                row['favorite'] = row['favorite'].lower() == 'true'
            contacts_from_file.append(row)
    return contacts_from_file


write_contacts_to_file(filename, contacts)
print(read_contacts_from_file(filename))

#################### Task 4

import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name,
        self.email = email,
        self.phone = phone,
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        self.contacts = contacts if contacts else []
        self.filename = filename

    def save_to_file(self):
        with open(self.filename, "wb") as pickle_file:
            pickle.dump(self, pickle_file)

    def read_from_file(self):
        with open(self.filename, "rb") as pickle_file:
            return pickle.load(pickle_file)


contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]
persons = Contacts("user_class.dat", contacts)

persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True

#################### Task 5


import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None, count_save: int = 0):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = count_save

    def save_to_file(self):
        with open(self.filename, "wb") as pickle_file:
            pickle.dump(self, pickle_file)

    def read_from_file(self):
        with open(self.filename, "rb") as pickle_file:
            content = pickle.load(pickle_file)
        return content

    def __getstate__(self):
        state = self.__dict__.copy()
        state['count_save'] += 1
        return state


contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3

#################### Task 6


import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None, is_unpacking=False):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0
        self.is_unpacking = is_unpacking

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        value["is_unpacking"] = True
        self.__dict__.update(value)


persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons.is_unpacking)  # False
print(person_from_file.is_unpacking)  # True

#################### Task 7

import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)


person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

copy_person = copy_class_person(person)

print(copy_person == person)  # False
print(copy_person.name == person.name)  # True

#################### Task 8

import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True


contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]


def copy_class_contacts(contacts):
    return copy.deepcopy(contacts)


persons = Contacts("user_class.dat", contacts)
new_persons = copy_class_contacts(persons)
new_persons.contacts[0].name = "Another name"
print(persons.contacts[0].name)  # Allen Raymond
print(new_persons.contacts[0].name)  # Another name

#################### Task 9


import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        # Поверхнева копія: просто копіюємо значення атрибутів
        return Person(self.name, self.email, self.phone, self.favorite)

    def __deepcopy__(self, memo):
        # Для Person глибока копія така ж, як і поверхнева, тому ми можемо просто використовувати __copy__
        return self.__copy__()


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        # Поверхнева копія для Contacts: копіюємо список контактів як є
        new_contacts = self.contacts.copy()  # створюємо новий список, але контакти не копіюються глибоко
        return Contacts(self.filename, new_contacts)

    def __deepcopy__(self, memo):
        # Глибока копія для Contacts: для кожного контакту створюємо глибоку копію
        new_contacts = [copy.deepcopy(contact, memo) for contact in self.contacts]
        new_instance = Contacts(self.filename, new_contacts)
        return new_instance
