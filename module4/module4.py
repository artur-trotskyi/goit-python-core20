from pathlib import Path
import sys
import os

print(sys.modules["pathlib"])
print(sys.modules.keys())

with open("test.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("test.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)

with open('raw_data.bin', 'wb') as fh:
    fh.write(b'Hello world!')

p = Path("example.txt")
p.write_text("Hello, world!")
print(p.read_text())
print("Exists:", p.exists())

# Початковий шлях
base_path = Path("/usr/bin")

# Додавання додаткових частин до шляху
full_path = base_path / "subdir" / "script.py"
print(full_path)  # Виведе: /usr/bin/subdir/script.py

# Початковий шлях до файлу
original_path = Path("example.txt")

# Зміна імені файлу
new_path = original_path.with_name("report.txt")
original_path.rename(new_path)
print(new_path)
