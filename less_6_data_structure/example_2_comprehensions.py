chars = []

for char in "abcde":
    chars.append(char)
print(chars)

chars2 = [char.upper() for char in "abcde"]
print(chars2)

names = ["don", 'tom', 'sally']
names = [name.capitalize() for name in names]
print(names)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_num = [num for num in numbers if num % 2 == 0]
print(even_num)

unique_values = {num for num in [1, 1, 2, 2, 5, 8, 3, 4, 21, 4, 45, 5]}
print(unique_values)

unique_values2 = {num ** 2 for num in [1, 1, 2, 2, 5, 8, 3, 4, 21, 4, 45, 5]}
print(unique_values2)

data = ['Jhon_25', 'Sally_19', 'Susan_35', 'Jack_16']
name_age_dict = {v for v in data}
print(name_age_dict)
name_age_dict = {v.split('_')[0]: v.split('_')[1] for v in data}
print(name_age_dict)

value_squares = {val: val ** 2 for val in range(10)}
print(value_squares)
