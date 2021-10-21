print('CALCULATOR')

try:
    a = float(input('a = '))
    b = float(input('b = '))
    print(a / b)

except (ValueError, ZeroDivisionError) as ex:
    print(ex)

print("Stopping calculate")
