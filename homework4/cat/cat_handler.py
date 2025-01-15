def get_cats_info(path: str) -> list[dict]:
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for cat_line in file:
                try:
                    cat_data = cat_line.split(',')
                    cat = {
                        "id": cat_data[0].strip(),
                        "name": cat_data[1].strip(),
                        "age": cat_data[2].strip()
                    }
                    cats_info.append(cat)
                except (IndexError, ValueError):
                    print(f"Має некоректний рядок: {cat_line.strip()}")
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
    return cats_info
