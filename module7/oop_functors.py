class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, other):
        return self.factor * other


# Створення екземпляра функтора
double = Multiplier(2)
triple = Multiplier(3)

# Виклик функтора
print(double(5))  # Виведе: 10
print(triple(3))  # Виведе: 9


#####################

class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1


counter = Counter()
counter()
counter()
print(f"Викликано {counter.count} разів")


#####################

class SmartCalculator:
    def __init__(self, operation='add'):
        self.operation = operation

    def __call__(self, a, b):
        if self.operation == 'add':
            return a + b
        elif self.operation == 'subtract':
            return a - b
        else:
            raise ValueError("Невідома операція")


add = SmartCalculator('add')
print(add(5, 3))  # 8

subtract = SmartCalculator('subtract')
print(subtract(10, 7))  # 3


################################ Створення об'єкта ітератора/генератора ################################

class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 0:
            raise StopIteration
        self.current -= 1
        return self.current


if __name__ == '__main__':
    counter = CountDown(5)
    for count in counter:
        print(count)


### Але це можна реалізувати через генератор

def count_down(start):
    current = start
    current -= 1
    while current >= 0:
        yield current
        current -= 1


# Використання генератора
for count in count_down(5):
    print(count)

"""
Розглянемо наступний приклад. Створимо клас RandIterator, який використовується для генерації обмеженої кількості 
випадкових чисел в заданому діапазоні. Коли ми створимо екземпляр цього класу, ми вкажемо початкове та кінцеве значення 
діапазону start і end та кількість чисел quantity, які ми хочемо згенерувати.
"""

from random import randint


class RandIterator:
    def __init__(self, start, end, quantity):
        self.start = start
        self.end = end
        self.quantity = quantity
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.quantity:
            raise StopIteration
        else:
            return randint(self.start, self.end)


if __name__ == '__main__':
    my_random_list = RandIterator(1, 20, 5)

    for rn in my_random_list:
        print(rn, end=' ')  # 14 8 15 13 16

"""
Крутий приклад із автоперевірок

"""

from random import randrange


class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        return (
                self.coordinates.x * vector.coordinates.x
                + self.coordinates.y * vector.coordinates.y
        )

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

    def __eq__(self, vector):
        return self.len() == vector.len()

    def __ne__(self, vector):
        return self.len() != vector.len()

    def __lt__(self, vector):
        return self.len() < vector.len()

    def __gt__(self, vector):
        return self.len() > vector.len()

    def __le__(self, vector):
        return self.len() <= vector.len()

    def __ge__(self, vector):
        return self.len() >= vector.len()


class Iterable:
    def __init__(self, max_vectors, max_points):
        self.max_vectors = max_vectors
        self.max_points = max_points
        self.current_index = 0
        self.vectors = [
            Vector(Point(randrange(0, max_points), randrange(0, max_points)))
            for _ in range(max_vectors)
        ]

    def __next__(self):
        if self.current_index < self.max_vectors:
            vector = self.vectors[self.current_index]
            self.current_index += 1
            return vector
        raise StopIteration


class RandomVectors:
    def __init__(self, max_vectors=10, max_points=50):
        self.max_vectors = max_vectors
        self.max_points = max_points

    def __iter__(self):
        return Iterable(self.max_vectors, self.max_points)


vectors = RandomVectors(5, 10)

for vector in vectors:
    print(vector)


########

class MultIterator:
    def __init__(self, seq, stop=1):
        self.seq = seq
        self.stop = stop
        self.loop = 0
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.loop >= self.stop:
            raise StopIteration
        value = self.seq[self.idx]
        self.idx += 1
        if self.idx == len(self.seq):
            self.idx = 0
            self.loop += 1
        return value


seq = [1, 2, 3, 4, True, None, 'test', 23]

my_iterator = MultIterator(seq, 10)
for value in my_iterator:
    print(value, end='\t')


################################ Передача значень у генератор ################################

def my_generator():
    received = yield "Ready"
    yield f"Received: {received}"


gen = my_generator()
print(next(gen))  # Ready
print(gen.send("Hello"))  # Received: Hello


####

def my_generator():
    try:
        yield "Working"
    except GeneratorExit:
        print("Generator is being closed")


gen = my_generator()
print(next(gen))  # Отримуємо "Working"
gen.close()  # Викликаємо закриття генератора

"""
Спочатку розглянемо простий приклад. Створимо генератор square_numbers() , який буде приймати числа через метод send() 
та виконувати обчислення, візьмемо просту операцію піднесення до квадрату, та повертати результат через yield.
"""


def square_numbers():
    try:
        while True:  # Безкінечний цикл для прийому чисел
            number = yield  # Отримання числа через send()
            square = number ** 2  # Піднесення до квадрата
            yield square  # Повернення результату
    except GeneratorExit:
        print("Generator closed")


# Створення і старт генератора
gen = square_numbers()

# Ініціалізація генератора
next(gen)  # Або gen.send(None), щоб стартувати

# Відправлення числа в генератор і отримання результату
result = gen.send(10)  # Повинно повернути 100
print(f"Square of 10: {result}")

# Перехід до наступного очікування
next(gen)

# Відправлення іншого числа
result = gen.send(5)  # Повинно повернути 25
print(f"Square of 5: {result}")

# Закриття генератора
gen.close()

"""
Тепер розглянемо більш складний приклад. Створимо генератор filter_lines(), який чекатиме на вхідні рядки через метод 
send(). Всередині генератора буде перевірка: якщо рядок містить певне слово, він буде повернутий через yield.
"""
print('--------------------')


def filter_lines(keyword):
    print(f"Looking for {keyword}")
    try:
        while True:  # Нескінченний цикл, де генератор чекає на вхідні дані
            line = yield  # Отримання рядка через send()
            if keyword in line:  # Перевірка на наявність ключового слова
                yield f"Line accepted: {line}"
            else:
                yield None
    except GeneratorExit:
        print("Generator closed")


if __name__ == "__main__":
    # Створення і старт генератора
    gen = filter_lines("hello")
    next(gen)  # Потрібно для старту генератора
    messages = ["this is a test", "hello world", "another hello world line", "hello again", "goodbye"]
    hello_messages = []
    # Відправлення даних у генератор
    for message in messages:
        result = gen.send(message)  # Відправляємо повідомлення в генератор
        if result:  # Додаємо результат тільки якщо він не None
            hello_messages.append(result)
        next(gen)  # Продовжуємо до наступного yield: інструкція line = yield

    # Закриття генератора
    gen.close()
    print(hello_messages)

####################################### Створення власних менеджерів контексту #######################################

"""
Створення власного менеджера контексту в Python - це спосіб керування ресурсами, такими як файли, з'єднання з базою 
даних та інше, забезпечуючи їх автоматичне відкриття та закриття. Менеджер контексту гарантує, що ресурси будуть 
коректно звільнені після завершення блоку коду, навіть якщо в процесі виконання виникне виключення.

Для створення власного менеджера контексту необхідно реалізувати клас з магічними методами __enter__ та __exit__. 
Метод __enter__ викликається на початку блоку with, коли інтерпретатор заходить у контекст і те, що він поверне, буде 
записано в змінну після as. Метод __exit__ викликається після завершення виконання блоку with, незалежно від того, 
виникло виключення чи ні.
"""
print('--------------------')


class MyContextManager:
    def __enter__(self):
        # Ініціалізація ресурсу
        print("Enter the block")
        return self  # Може повертати об'єкт

    def __exit__(self, exc_type, exc_value, traceback):
        # Звільнення ресурсу
        print("Exit the block")
        if exc_type:
            print(f"Error detected: {exc_value}")
        # Повернення False передає виключення далі, True - поглинає виключення.
        return False


# Використання власного менеджера контексту
with MyContextManager() as my_resource:
    print("Inside the block")
    # raise Exception("Something went wrong") # разкоментуй для тесту

###############
print('--------------------')


class FileManager:
    def __init__(self, filename, mode='w', encoding='utf-8'):
        self.file = None
        self.opened = False
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        self.opened = True
        print("Відкриваємо файл", self.filename)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Завершення блоку with")
        if self.opened:
            print("Закриваємо файл", self.filename)
            self.file.close()
        self.opened = False
        if exc_val is not None:
            print('On No !!!')


if __name__ == '__main__':
    with FileManager('new_file.txt') as f:
        f.write('Hello world!\n')
        f.write('The end\n')

"""
Відкриваємо файл new_file.txt
Завершення блоку with
Закриваємо файл new_file.txt
"""

"""
Декоратор @contextmanager дозволяє нам створити контекстний менеджер за допомогою генератора, та спростити написання 
коду порівняно з класом FileManager, який використовує методи __enter__ та __exit__.
"""

from contextlib import contextmanager


@contextmanager
def file_manager(filename, mode='w', encoding='utf-8'):
    print("Відкриваємо файл", filename)
    file = open(filename, mode, encoding=encoding)
    try:
        yield file
    finally:
        print("Закриваємо файл", filename)
        file.close()
        print("Завершення блоку with")


if __name__ == '__main__':
    with file_manager('new_file.txt') as f:
        f.write('Hello world!\n')
        f.write('The end\n')

##########

"""
Створимо контекстний менеджер, який буде управляти відкриттям та закриттям файлу з додатковим логуванням. 
Наш контекстний менеджер managed_resource буде вимірювати час виконання операцій з файлом та логувати дії 
відкриття і закриття файлу разом з тривалістю їх виконання.
"""

from contextlib import contextmanager
from datetime import datetime


@contextmanager
def managed_resource(*args, **kwargs):
    log = ''
    timestamp = datetime.now().timestamp()
    msg = f'{timestamp:<20}|{args[0]:^15}| open \n'
    log += msg
    file_handler = open(*args, **kwargs)
    try:
        yield file_handler
    finally:
        diff = datetime.now().timestamp() - timestamp
        msg = f'{timestamp:<20}|{args[0]:^15}| closed {round(diff, 6):>15}s \n'
        log += msg
        file_handler.close()
        print(log)


with managed_resource('new_file.txt', 'r') as f:
    print(f.read())
