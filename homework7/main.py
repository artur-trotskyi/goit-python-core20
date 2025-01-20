from collections import UserDict
from datetime import datetime, date, timedelta
from typing import List, Dict, Any, Optional, Tuple


class Field:
    def __init__(self, value: str) -> None:
        if not value:
            raise ValueError("Field value cannot be empty.")
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    # Class implementation for Name (to be added later)
    pass


class Phone(Field):
    def __init__(self, value) -> None:
        # Ensure phone number is 10 digits
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must be exactly 10 digits.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value: str) -> None:
        try:
            date_object = datetime.strptime(value, "%d.%m.%Y").date()
            # Ensure birthday is not in the future
            if date_object > datetime.now().date():
                raise ValueError("Birthday cannot be in the future.")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY.")
        super().__init__(value)


class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones: List[Phone] = []
        self.birthday: Optional[Birthday] = None

    def __str__(self) -> str:
        return f"Contact Name: {self.name}; Phones: {', '.join(p.value for p in self.phones)}; Birthday: {self.birthday}"

    def add_phone(self, phone: str) -> None:
        # Avoid duplicate phone numbers
        if phone not in [p.value for p in self.phones]:
            self.phones.append(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        # Ensure the old and new phone numbers are different
        if old_phone == new_phone:
            raise ValueError("Old phone and new phone are the same. No changes made.")

        phone = self.find_phone(old_phone)
        if not phone:
            raise ValueError(f"Phone {old_phone} not found.")

        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone: str) -> Phone | None:
        for i, record_phone in enumerate(self.phones):
            if phone == str(record_phone):
                return self.phones[i]
        return None

    def remove_phone(self, phone: str) -> None:
        phone_obj = self.find_phone(phone)
        if not phone_obj:
            raise ValueError(f"Phone {phone} not found.")

        self.phones.remove(phone_obj)

    def add_birthday(self, birthday: Birthday) -> None:
        self.birthday = birthday


class AddressBook(UserDict):
    def __str__(self) -> str:
        records = '\n'.join(f"{record}" for record in self.data.values())
        return f"AddressBook:\n{records if records else 'empty'}"

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name, None)

    def delete(self, name: str) -> Record:
        if name not in self.data:
            raise ValueError(f"Record with name {name} does not exist.")
        return self.data.pop(name)

    def get_upcoming_birthdays(self, days: int = 7) -> List[Dict[str, Any]]:
        """
        Returns a list of contacts with birthdays within the next 'days' days, including today.
        """
        upcoming_birthdays = []
        today = date.today()

        for record in self.data.values():
            if not record.birthday or not record.birthday.value:
                continue
            birthday_date = self.string_to_date(record.birthday.value)
            # Set birthday to this year
            congratulation_date = birthday_date.replace(year=today.year)

            # If birthday has already passed this year, move it to next year
            if congratulation_date < today:
                congratulation_date = birthday_date.replace(year=today.year + 1)

            # Calculate days remaining until the birthday
            remaining_days = (congratulation_date - today).days

            # If birthday is within 'days' days
            if 0 <= remaining_days <= days:
                # Adjust for weekends
                congratulation_date = self.adjust_for_weekend(congratulation_date)
                upcoming_birthdays.append({
                    "name": record.name.value,
                    "birthday": self.date_to_string(congratulation_date),
                    "days_left": remaining_days
                })
        return upcoming_birthdays

    @staticmethod
    def string_to_date(date_string: str) -> date:
        return datetime.strptime(date_string, "%d.%m.%Y").date()

    @staticmethod
    def adjust_for_weekend(birthday: date) -> date:
        # Adjust birthday to the next weekday if it falls on a weekend
        return AddressBook.find_next_weekday(birthday, 0) if birthday.weekday() >= 5 else birthday

    @staticmethod
    def find_next_weekday(start_date: date, weekday: int) -> date:
        # Finds the next weekday starting from `start_date`
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)

    @staticmethod
    def date_to_string(date_obj: date) -> str:
        # Converts a date object to a string in the format YYYY.MM.DD
        return date_obj.strftime("%d.%m.%Y")


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    if not user_input:
        return '', []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Invalid input. Error: {str(e)}"
        except IndexError as e:
            return f"Missing required parameters. Please provide all necessary information. Error: {str(e)}"
        except KeyError as e:
            return f"Key error occurred. Error: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred. Please try again later. Error: {str(e)}"

    return inner


@input_error
def add_contact(args, book: AddressBook) -> str:
    name, phone, *_ = args
    record = get_contact(name, book)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook) -> str:
    name, old_phone, new_phone, *_ = args
    record = get_contact(name, book)
    if not record:
        raise ValueError(f"Contact {name} not found.")
    record.edit_phone(old_phone, new_phone)
    return f"Phone number {old_phone} was changed to {new_phone} for contact {name}."


def get_contact(name: str, book: AddressBook) -> Record | None:
    return book.find(name) or None


def all_contacts(book: AddressBook) -> AddressBook:
    return book


def display_phone_numbers(record: Record, name: str) -> None:
    if not record:
        print(f"Contact {name} not found.")
        return

    if not record.phones:
        print(f"No phone numbers found for contact {name}.")
        return

    phones = [str(phone) for phone in record.phones]
    print(f"Phone number(s) for contact {name}: {', '.join(phones)}")
    return


@input_error
def add_birthday(args, book: AddressBook) -> str:
    name, birthday_date, *_ = args
    record = get_contact(name, book)
    if not record:
        raise ValueError(f"Contact not found.")
    message = f"Birthday was updated for contact {record.name}." if record.birthday is not None \
        else f"Birthday was added for contact {record.name}."
    record.add_birthday(Birthday(birthday_date))
    return message


@input_error
def show_birthday(args, book: AddressBook) -> str:
    name, *_ = args
    record = get_contact(name, book)
    if not record:
        raise ValueError(f"Contact not found.")
    return f"Birthday of {record.name}: {record.birthday or 'is not set'}."


def display_upcoming_birthdays(upcoming_birthdays: List[Dict[str, Any]], days: int) -> None:
    if not upcoming_birthdays:
        print(f"No upcoming birthdays in the next {days} days.")
        return

    print("Upcoming birthdays:")
    for birthday in upcoming_birthdays:
        print(
            f"Name: {birthday['name']}, Birthday: {birthday['birthday']}, Days Left: {birthday['days_left']}"
        )


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            """
            close або exit: Close the program
            """
            print("Good bye!")
            break
        elif command == "hello":
            """
            hello
            Get a greeting from the bot
            """
            print("How can I help you?")
        elif command == "add":
            """
            add test 1234567890
            add test 1112223334
            add test2 2222222222
            add [name] [phone number]
            Add a new contact or a phone number to an existing contact
            """
            add_contact_result = add_contact(args, book)
            print(add_contact_result)
        elif command == "change":
            """
            change test 1234567890 5555555555
            change [name] [old phone number] [new phone number]
            Change a phone number for the specified contact
            """
            change_contact_result = change_contact(args, book)
            print(change_contact_result)
        elif command == "phone" and args:
            """
            phone test
            phone [name]
            Show phone numbers for the specified contact
            """
            name, *_ = args
            record = get_contact(name, book)
            display_phone_numbers(record, name)
        elif command == "all":
            """
            all
            Show the AddressBook
            """
            contacts = all_contacts(book)
            print(contacts)
        elif command == "add-birthday":
            """
            add-birthday test 30.12.2000
            add-birthday [name] [birthdate]
            Add a birthday date for the specified contact
            """
            add_birthday_result = add_birthday(args, book)
            print(add_birthday_result)
        elif command == "show-birthday":
            """
            show-birthday test
            show-birthday [name]
            Show the birthdate for the specified contact
            """
            show_birthday_result = show_birthday(args, book)
            print(show_birthday_result)
        elif command == "birthdays":
            """
            birthdays
            Show birthdays for the next 7 days with dates to wish
            """
            days = 7
            upcoming_birthdays = book.get_upcoming_birthdays(days)
            display_upcoming_birthdays(upcoming_birthdays, days)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
