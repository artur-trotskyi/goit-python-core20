from collections import UserDict


class Field:
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    # реалізація класу
    pass


class Phone(Field):
    def __init__(self, value) -> None:
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must be exactly 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones = []

    def __str__(self) -> str:
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        phone = self.find_phone(old_phone)
        if phone:
            self.add_phone(new_phone)

            self.remove_phone(old_phone)
            return
        raise ValueError(f"Phone {old_phone} not found.")

    def find_phone(self, phone: str) -> Phone | None:
        for i, record_phone in enumerate(self.phones):
            if phone == str(record_phone):
                return self.phones[i]
        return None

    def remove_phone(self, phone: str) -> None:
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
        else:
            raise ValueError(f"Phone {phone} not found.")


class AddressBook(UserDict):
    def __str__(self) -> str:
        records = ', '.join(f"{key} => [ {record} ]" for key, record in self.data.items())
        return f"AddressBook: {records or 'empty'}"

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name, None)

    def delete(self, name: str) -> Record:
        if name not in self.data:
            raise ValueError(f"Record with name {name} does not exist.")
        return self.data.pop(name)


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_phone("4444455555")
print(john_record)

john_record.remove_phone("4444455555")
print(john_record)

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")

# Виведення всіх записів у книзі
print(book)
