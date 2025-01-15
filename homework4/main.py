import sys
from salary import total_salary
from cat import get_cats_info
from directory_parser import directory_console_parser


def main():
    # 1
    print(f"******* Завдання №1. Заробітня плата *******")

    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    total, average = total_salary("salary_file")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    # 2
    print(f"\n******* Завдання №2. Коти *******")

    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)

    cats_info = get_cats_info("cats_file")
    print(cats_info)

    # 3
    # please note the startup instruction (Приклад використання) at the end of the directory_parser/readme.md file
    if len(sys.argv) > 1:
        print(f"\n******* Завдання №3. Парсер каталогу '{sys.argv[1]}' *******")
        directory_console_parser()


if __name__ == "__main__":
    main()
