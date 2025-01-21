my_list = [1, 2, 3]

def square_list(x: list):
    for i, el in enumerate(x):
        x[i] = el**2
    return x

new_list = square_list(my_list)
print(new_list)
print(my_list)


my_dict = {"a": 1, "b": 2, "c": 3}

def square_dict_values(d: dict):
    for key in d:
        d[key] = d[key] ** 2
    return d

new_dict = square_dict_values(my_dict)
print(new_dict)  # {'a': 1, 'b': 4, 'c': 9}
print(my_dict)   # {'a': 1, 'b': 4, 'c': 9}