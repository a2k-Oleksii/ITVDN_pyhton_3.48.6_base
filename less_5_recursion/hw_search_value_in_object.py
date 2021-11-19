# Напишите функцию, которая рекурсивно ищет в сложном объекте значение. 
# Сложный объект — это будет список списков списков и т.д. Например, [1, 2, [3, 4, [5, [6, []]]]]. 
# Функция должна рекурсивно заходить внутрь вложенных массивов, а если это другой тип данных 
# игнорировать его.


def search_varieble(object, variable):
    if type(object) is list:
        for element in object:
            if type(element) is list:
                search_varieble(element, variable)
            elif element == variable:
                print("Searching element is find :)")
                break  


list_value = [1, 2, [3, 4, [5, [6, []]]], 8]
search_varieble(list_value, 8)
