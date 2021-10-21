def generator_function():
    for x in range(5):
        for y in range(3):
            if (x + y) % 2 == 0:
                yield x * y


generator = (x * y for x in range(5) for y in range(3) if (x + y) % 2 == 0) # тоже самое что и - def generator_function():
for value in generator:
    print(value)
