def total_salary(path: str) -> tuple[float, float]:
    error_value = 0.0, 0.0

    try:
        with open(path, "r", encoding="utf-8") as file:
            salary_sum = 0
            employers_count = 0
            for salary_line in file:
                try:
                    salary_sum += float(salary_line.split(',')[1])
                    employers_count += 1
                except (IndexError, ValueError):
                    print(f"Файл {path} має помилки.")
                    return error_value

            if employers_count == 0:
                return error_value

            average_salary = round(salary_sum / employers_count, 2)
            return round(salary_sum, 2), average_salary

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return error_value
