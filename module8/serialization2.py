########################################## Управління порядком серіалізації ##########################################

## ми хочемо серіалізувати лише певні атрибути.

import pickle


class Robot:
    def __init__(self, name, battery_life):
        self.name = name
        self.battery_life = battery_life
        # Цей атрибут ми не збираємось серіалізувати
        self.is_active = False

    def __getstate__(self):
        state = self.__dict__
        # Видаляємо is_active з серіалізованого стану
        del state['is_active']
        return state

    def __setstate__(self, state):
        # Відновлюємо об'єкт при десеріалізації
        self.__dict__.update(state)
        # Задаємо значення is_active за замовчуванням
        self.is_active = False


# Створення об'єкта Robot
robot = Robot("Robo1", 100)

# Серіалізація об'єкта
serialized_robot = pickle.dumps(robot)

# Десеріалізація об'єкта
deserialized_robot = pickle.loads(serialized_robot)

print(deserialized_robot.__dict__)

############# приклад серіалізації читання із файлу

import pickle


class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.fh = open(self.filename, "r", encoding="utf-8")

    def close(self):
        self.fh.close()

    def read(self):
        data = self.fh.read()
        return data

    def __getstate__(self):
        attributes = {**self.__dict__, "fh": None}
        return attributes

    def __setstate__(self, state):
        # Відновлюємо стан об'єкта
        self.__dict__ = state
        self.fh = open(state["filename"], "r", encoding="utf-8")


if __name__ == "__main__":
    reader = Reader("data.txt")
    data = reader.read()
    print(data)
    reader.close()

    # Приклад серіалізації об'єкта Reader
    with open("reader.pkl", "wb") as f:
        pickle.dump(reader, f)

    # Приклад десеріалізації об'єкта Reader
    with open("reader.pkl", "rb") as f:
        loaded_reader = pickle.load(f)
        print(loaded_reader.read())
        loaded_reader.close()

######################################### Створення копій об'єктів в Python #########################################

my_list = [1, 2, 3]
copy_list = my_list[:]
copy_list.append(4)
print(my_list, copy_list)

my_dict = {1: "a"}
copy_dict = {**my_dict}
copy_dict["new_key"] = "new_value"
print(my_dict, copy_dict)

##################################### Створення поверхневих копій об'єктів Python #####################################

import copy

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.copy(my_list)
copy_list.append(4)
print(my_list)
print(copy_list)

### Тому вкладені об'єкти, такі як словник в третьому елементі списку, будуть спільними між оригінальним та скопійованим списками.

import copy

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.copy(my_list)
copy_list[2]["age"] = 30
print(my_list)
print(copy_list)

# [1, 2, {'name': 'Gupalo Vasyl', 'age': 30}]
# [1, 2, {'name': 'Gupalo Vasyl', 'age': 30}]


##################################### Створення глибоких копій об'єктів Python #####################################

import copy

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.deepcopy(my_list)
copy_list[2]["age"] = 30
print(my_list)
print(copy_list)

#################################### Управління порядком копіювання об'єктів Python ####################################

import copy


class MyClass:
    def __init__(self, value):
        self.value = value

    def __copy__(self):
        print("Викликано __copy__")
        return MyClass(self.value)

    def __deepcopy__(self, memo=None):
        print("Викликано __deepcopy__")
        return MyClass(copy.deepcopy(self.value, memo))


# Поверхневе копіювання
obj = MyClass(5)
obj_copy = copy.copy(obj)
obj_copy.value = 10

# Глибоке копіювання
obj_deepcopy = copy.deepcopy(obj)
obj_deepcopy.value = 20
print(obj.value, obj_copy.value, obj_deepcopy.value)

#### Тепер розглянемо більш складний приклад з вкладеними об'єктами:

import copy


class SimpleObject:
    def __init__(self, greeting: str):
        self.greeting = greeting


class ComplexObject:
    def __init__(self, value: int, nested_obj: SimpleObject):
        self.value = value
        self.nested_obj = nested_obj

    def __copy__(self):
        print("Викликано __copy__ для ComplexObject")
        # Поверхневе копіювання не копіює вкладені об'єкти глибоко
        return ComplexObject(self.value, self.nested_obj)

    def __deepcopy__(self, memo=None):
        print("Викликано __deepcopy__ для ComplexObject")
        # Глибоке копіювання копіює вкладені об'єкти
        return ComplexObject(
            copy.deepcopy(self.value, memo), copy.deepcopy(self.nested_obj, memo)
        )


nested_obj = SimpleObject("Привіт")
complex_obj = ComplexObject(5, nested_obj)

# Створюємо копію та глибоку копію
complex_obj_copy = copy.copy(complex_obj)
complex_obj_deepcopy = copy.deepcopy(complex_obj)

# Змінюємо значення вкладеного об'єкту nested_obj
nested_obj.greeting = "Hello"

# Дивимось зміни у об'єктах
print(f"Copy object: {complex_obj_copy.nested_obj.greeting}")
print(f"Deepcopy object: {complex_obj_deepcopy.nested_obj.greeting}")

"""
Уявімо, що ми працюємо з класом, який представляє налаштування користувача, і ці налаштування включають в себе великий 
набір даних (гігабайти даних), який не потрібно дублювати при кожному копіюванні, але з яким потрібно працювати в 
ізольованому середовищі.
"""

import copy


class UserSettings:
    def __init__(self, preferences, large_data_reference):
        self.preferences = preferences
        self.large_data_reference = large_data_reference

    def __deepcopy__(self, memo):
        print("Кастомізоване глибоке копіювання для UserSettings")
        # Припустимо, що preferences - це невеликий словник, який можна безпечно скопіювати,
        # а large_data_reference - це посилання на великий об'єкт даних, яке ми не хочемо дублювати.
        new_preferences = copy.deepcopy(self.preferences, memo)
        # Передаємо посилання на ті ж великі дані замість їх копіювання
        new_obj = UserSettings(new_preferences, self.large_data_reference)
        return new_obj


# Створення екземпляра UserSettings
original_settings = UserSettings({"language": "uk"}, large_data_reference="LargeDataID")

# Глибоке копіювання з кастомізованою логікою
settings_copy = copy.deepcopy(original_settings)
