def parse_input(user_input):
    if not user_input:
        return '', []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name and phone."
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return inner


@input_error
def add_contact(args, contacts: dict[str, str]):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts: dict[str, str]):
    name, phone = args
    is_changed = False
    if name in contacts:
        contacts.update({name: phone})
        is_changed = True
    return "Contact updated." if is_changed else "Contact not found."


def get_contact(name: str, contacts: dict[str, str]) -> dict[str, str]:
    return {name: contacts[name]} if name in contacts else {}


def all_contacts(contacts: dict[str, str]) -> dict[str, str]:
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            added_result = add_contact(args, contacts)
            print(added_result)
        elif command == "change":
            changed_result = change_contact(args, contacts)
            print(changed_result)
        elif command == "phone" and args:
            contact_name = args[0]
            result = get_contact(contact_name, contacts)
            print(f"Phone number for contact {contact_name}: {result[contact_name]}") if result else print(
                f"Contact {contact_name} not found.")
        elif command == "all":
            print("All contacts:")
            print(
                "\n".join(
                    f"{name}: {phone}" for name, phone in all_contacts(contacts).items()) or "No contacts available.")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
