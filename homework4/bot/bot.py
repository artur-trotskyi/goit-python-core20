def parse_input(user_input):
    if not user_input:
        return '', []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts: dict[str, str]) -> str | bool:
    if len(args) != 2:
        return False
    name, phone = args
    contacts[name] = phone
    return contacts[name]


def change_contact(args, contacts: dict[str, str]) -> bool:
    if len(args) != 2:
        return False
    name, phone = args
    return contacts.update({name: phone}) or True if name in contacts else False


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
            is_added = add_contact(args, contacts)
            print("Contact added.") if is_added else print("Invalid command.")
        elif command == "change":
            is_changed = change_contact(args, contacts)
            print("Contact updated.") if is_changed else print("Contact not found or Invalid command.")
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
