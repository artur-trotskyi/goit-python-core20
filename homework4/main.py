from salary import total_salary

# 1

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

total, average = total_salary("salary_file")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
