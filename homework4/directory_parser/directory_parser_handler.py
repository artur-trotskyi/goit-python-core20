from pathlib import Path
from colorama import Fore, Style
import sys


def parser(directory: Path, indent: str = "") -> None:
    entries = list(directory.iterdir())
    entries_count = len(entries)

    for index, path in enumerate(entries):
        is_last = index == entries_count - 1
        connector = "└── " if is_last else "├── "
        if path.is_file():
            print(Fore.GREEN + f"{indent}{connector}{path.name}")
        elif path.is_dir():
            print(Fore.BLUE + f"{indent}{connector}{path.name}")
            new_indent = indent + ("    " if is_last else "│   ")
            parser(path, new_indent)

    print(Style.RESET_ALL, end="")


def directory_console_parser() -> None:
    if len(sys.argv) > 1:
        directory = Path(sys.argv[1])
        if not directory.exists():
            print(Fore.RED + f"Помилка: Директорія '{directory}' не існує." + Style.RESET_ALL)
            return
        if not directory.is_dir():
            print(Fore.RED + f"Помилка: '{directory}' не є директорією." + Style.RESET_ALL)
            return

        parser(directory)
    else:
        print(Fore.YELLOW + "Помилка: Будь ласка, вкажіть шлях до директорії як аргумент." + Style.RESET_ALL)
