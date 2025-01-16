import collections

# ********************************* Іменовані кортежі *********************************

Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

cat = Cat('Simon', 4, 'Krabat')

print(f'This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}')

# ********************************* Counter *********************************

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1

print(mark_counts)

mark_counts = collections.Counter(student_marks)
print(mark_counts)

print(mark_counts.most_common())
print(mark_counts.most_common(1))
print(mark_counts.most_common(2))

# Створення Counter з рядка
letter_count = collections.Counter("banana")
print(letter_count)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = collections.Counter(words)

# Виведення слова та його частоти
for word, count in word_count.items():
    print(f"{word}: {count}")

# ********************************* defaultdict *********************************


from collections import defaultdict

print('\n')

# Створення defaultdict з list як фабрикою за замовчуванням
d = defaultdict(list)
# Додавання елементів до списку для кожного ключа
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(int)
# Збільшення значення для кожного ключа
d['a'] += 1
d['b'] += 1
d['a'] += 1
print(d)

# Навіщо це потрібно і коли може знадобиться?
# Наприклад, у вас є список слів і ви хочете розбити його на декілька списків, залежно від першої літери слова.
words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = defaultdict(list)
for word in words:
    char = word[0]
    grouped_words[char].append(word)
print(dict(grouped_words))

# *********************************** Черга ***********************************

from collections import deque

# Створення черги
queue = deque()

# Enqueue: Додавання елементів
queue.append('a')
queue.append('b')
queue.append('c')

print('\n')
print("Черга після додавання елементів:", list(queue))

# Dequeue: Видалення елемента
print("Видалений елемент:", queue.popleft())

print("Черга після видалення елемента:", list(queue))

# Peek: Перегляд першого елемента
print("Перший елемент у черзі:", queue[0])

# IsEmpty: Перевірка на порожнечу
print("Чи черга порожня:", len(queue) == 0)

# Size: Розмір черги
print("Розмір черги:", len(queue))

from collections import deque

# Створення пустої двосторонньої черги
d = deque()

# Додаємо елементи в чергу
d.append('middle')  # Додаємо 'middle' в кінець черги
d.append('last')  # Додаємо 'last' в кінець черги
d.appendleft('first')  # Додаємо 'first' на початок черги

# Виведення поточного стану черги
print("Черга після додавання елементів:", list(d))

# Видалення та виведення останнього елемента (з правого кінця)
print("Видалений останній елемент:", d.pop())

# Видалення та виведення першого елемента (з лівого кінця)
print("Видалений перший елемент:", d.popleft())

# Виведення поточного стану черги після видалення елементів
print("Черга після видалення елементів:", list(d))

# Ще однією особливістю deque є можливість обмежити розмір Deque:

from collections import deque

d = deque(maxlen=5)
for i in range(10):
    d.append(i)

print(d)

# Мета цієї задачі — продемонструвати, як можна використовувати двосторонню чергу для контролю пріоритету завдань.

# Список завдань, де кожне завдання - це словник
tasks = [
    {"type": "fast", "name": "Помити посуд"},
    {"type": "slow", "name": "Подивитись серіал"},
    {"type": "fast", "name": "Вигуляти собаку"},
    {"type": "slow", "name": "Почитати книгу"}
]

# Ініціалізація черги завдань
task_queue = deque()

# Розподіл завдань у чергу відповідно до їх пріоритету
for task in tasks:
    if task["type"] == "fast":
        task_queue.appendleft(task)  # Додавання на високий пріоритет
        print(f"Додано швидке завдання: {task['name']}")
    else:
        task_queue.append(task)  # Додавання на низький пріоритет
        print(f"Додано повільне завдання: {task['name']}")

# Виконання завдань
while task_queue:
    task = task_queue.popleft()
    print(f"Виконується завдання: {task['name']}")

# *********************************** Decimal ***********************************

from decimal import Decimal, getcontext, ROUND_DOWN

print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print(Decimal("0.1") + Decimal("0.2"))

# Можна налаштувати загальну точність для всіх обчислень Decimal.
getcontext().prec = 6
print(Decimal("1000") / Decimal("7"))

getcontext().prec = 8
print(Decimal("1") / Decimal("7"))

# Наприклад, якщо ви хочете округлити число до двох знаків після коми,
# ви використовуєте Decimal об'єкт з двома нулями після коми як шаблон.

# Вихідне число Decimal
number = Decimal('3.14559')

# Встановлення точності до двох знаків після коми
rounded_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN)

print(rounded_number)

# За замовчуванням округлення описується константою ROUND_HALF_EVEN

import decimal
from decimal import Decimal

number = Decimal("1.45")

# Округлення за замовчуванням до одного десяткового знаку
print("Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0")))

# Округлення вверх при нічиї (ROUND_HALF_UP)
print("Округлення вгору ROUND_HALF_UP:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP))

# Округлення вниз (ROUND_FLOOR)
print("Округлення вниз ROUND_FLOOR:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR))

# Округлення вверх (ROUND_CEILING)
print("Округлення вгору ROUND_CEILING:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING))

# Округлення до трьох десяткових знаків за замовчуванням
print("Округлення до трьох десяткових знаків:", Decimal("3.14159").quantize(Decimal("0.000")))


# *********************************** Генератори ***********************************

def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()

# Використання next()
print(next(gen))  # Виведе 1
print(next(gen))  # Виведе 2
print(next(gen))  # Виведе 3


# *********************************** Замикання оптимізує кеш запиту ***********************************


def get_cache(initial_cache=None):
    cache = initial_cache or {}

    def inner(n):
        print(cache)
        if n not in cache:
            cache[n] = sum(range(1, n + 1))
            print(f'Hard work: {n}')
            return cache[n]
        else:
            print(f'Easy work: {n}')
            return cache[n]

    return inner


calc = get_cache()
print('\n***Cache Start***')
print(calc(5))
print(calc(5))
print(calc(10))
print(calc(10))
print(calc(15))
print(calc(55))
print('***Cache End***\n')

data = {5: 15, 10: 55, 15: 120}
calc = get_cache(data)
print('\n***Cache Start***')
print(calc(5))
print(calc(5))
print(calc(10))
print(calc(10))
print(calc(15))
print(calc(55))
print('***Cache End***\n')
# *********************************** Замикання, Каррінг ***********************************

from typing import Callable, Dict


def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)

    return apply_discount


# Створення словника з функціями знижок
discount_functions: Dict[str, Callable] = {
    "10%": discount(10),
    "20%": discount(20),
    "30%": discount(30)
}

# Використання функції зі словника
price = 500
discount_type = "20%"

discounted_price = discount_functions[discount_type](price)
print(f"Ціна зі знижкою {discount_type}: {discounted_price}")


# *********************************** Замикання, Каррінг ***********************************


def hello_male(name):
    print(f'Mr. {name}')


def hello_female(name):
    print(f'Mrs. {name}')


def hello_pan(name):
    print(f'Пан. {name}')


MODES = {
    'm': hello_male,
    'f': hello_female,
    'pan': hello_pan
}


def greeting(mode):
    return MODES[mode]


mr = greeting('m')
mrs = greeting('f')
pan = greeting('pan')

mr('Vlad')
mrs('Alona')
pan('Taras')

# *********************************** Декоратори ***********************************

# Наприклад, у нас є якась дуже складна і важлива функція complicated:
# І ми не хочемо міняти її код з якоїсь причини. Але нам потрібно додати логування до цієї функції, виводити в консоль щоразу,
# коли вона викликається, з якими аргументами її викликали і що вона повернула в результаті.
# Пам'ятаючи про те, що функція — це об'єкт першого класу, можна зробити щось подібне:
# Дуже важливо при створенні декораторів використовувати модуль functools, це необхідно для збереження метаданих
# оригінальної функції, яку ми декоруємо. Функція functools.wraps допомагає в цьому, зберігаючи інформацію про
# оригінальну функцію, як-от ім'я функції та документацію.

from functools import wraps


def logger(func):
    @wraps(func)
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner


@logger
def complicated(x: int, y: int) -> int:
    return x + y


print(complicated(2, 3))
print(complicated.__name__)


# *********************************** Декоратори 2 ***********************************

def args_logger(func):
    def inner(*args):
        if Debug:
            print(f'-------------------I am args logger. Args: {args}')
        result = func(*args)
        return result

    return inner


def result_logger(func):
    def inner(*args):
        result = func(*args)
        if Debug:
            print(f'---------------I am result logger. Result: {result}')
        return result

    return inner


from time import time


def timer(func):
    def inner(*args):
        start = time()
        result = func(*args)
        stop = time()
        if Debug:
            print(f'---------------I am timer logger. Run time: {stop - start}')
        return result

    return inner


@timer
@result_logger
@args_logger
def calc(x, y):
    result = x + y
    return result


Debug = True

print(calc(7, 9))


from decimal import Decimal

number = Decimal('1.45')
print(number.quantize(Decimal('1.0'), rounding=ROUND_DOWN))


# *********************************** List Comprehensions ***********************************

# List comprehensions використовуються для створення нових списків та мають наступний синтаксис:
# [new_item for item in iterable if condition]

sq = [x ** 2 for x in range(1, 6)]
print(sq)

even_squares = [x ** 2 for x in range(1, 10) if x % 2 == 0]
print(even_squares)

# *********************************** Set Comprehensions ***********************************

# Set comprehensions використовуються аналогічно list comprehensions, але для створення множин.
# {new_item for item in iterable if condition}

numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
print(sq)

odd_squares = {x ** 2 for x in range(1, 10) if x % 2 != 0}
print(odd_squares)

# *********************************** Dictionary Comprehensions ***********************************

# Dictionary comprehensions використовуються для створення нових словників.
# Для словників синтаксис comprehension трохи відрізняється, оскільки потрібно явно вказати ключ та значення
# {key: value for item in iterable if condition}

sq = {x: x ** 2 for x in range(1, 10)}
print(sq)

sq_dict = {x: x ** 2 for x in range(1, 10) if x > 5}
print(sq_dict)

# *********************************** Лямбда-функції ***********************************
# lambda arguments: expression

print((lambda x, y: x + y)(5, 3))  # Виведе 8

nums = [1, 2, 3, 4, 5]
nums_sorted = sorted(nums, key=lambda x: -x)
print(nums_sorted)

# *********************************** Функція map ***********************************

numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x ** 2, numbers):
    print(i)
squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = map(lambda x, y: x + y, nums1, nums2)
print(list(sum_nums))

# Замість використання функції map():
numbers = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums)

# Ми використаємо list comprehensions:
nums = [1, 2, 3, 4, 5]
squared_nums = [x * x for x in nums]
print(squared_nums)

# Для двох списків ми теж можемо використати list comprehensions допомоги функції zip
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = [x + y for x, y in zip(nums1, nums2)]
print(sum_nums)

# *********************************** Функція filter ***********************************

even_nums = filter(lambda x: x % 2 == 0, range(1, 11))
print(list(even_nums))


def is_positive(x):
    return x > 0


nums = [-2, -1, 0, 1, 2]
positive_nums = filter(is_positive, nums)
print(list(positive_nums))

some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'
new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))
print(new_str)

# Розглянемо, як можна замінити filter() на list comprehensions:
nums = [1, 2, 3, 4, 5, 6]
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums)

# Для рядка літер:
some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'
new_str = ''.join([x for x in some_str if x.islower()])
print(new_str)

# *********************************** Функція any ***********************************

# Функція any() є вбудованою функцією, яка повертає True, якщо хоча б один елемент із заданого об'єкта ітерації є істинним.
# Якщо об'єкт ітерації порожній або всі його елементи є хибними, то any() повертає False.

nums = [0, False, 5, 0]
result = any(nums)
print(result)

# В функцію можна передавати генератор або list comprehension. Наприклад перевіримо чи є в списку парні числа?
nums = [1, 3, 5, 7, 9]
result = any(x % 2 == 0 for x in nums)
print(result)

# *********************************** Функція all ***********************************

# Функція all() є вбудованою функцією, яка повертає True, якщо всі елементи в переданому їй об'єкті ітерації є
# істинними - тобто не False, 0, "", None або будь-яке інше значення, яке Python оцінює як хибне.
# Але будьте уважні, якщо об'єкт ітерації порожній, функція all() повертає True.

nums = [1, 2, 3, 4]
result = all(nums)
print(result)

nums = [1, 2, 3, 4]
is_all_even = all(x % 2 == 0 for x in nums)
print(is_all_even)

words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case)
