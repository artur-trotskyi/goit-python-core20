from salary import total_salary
from cat import get_cats_info

# 1
print(f"******* Завдання №1. Заробітня плата. *******")

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

total, average = total_salary("salary_file")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# 2
print(f"\n******* Завдання №2. Коти. *******")

cats_info = get_cats_info("cats_file.txt")
print(cats_info)

cats_info = get_cats_info("cats_file")
print(cats_info)
