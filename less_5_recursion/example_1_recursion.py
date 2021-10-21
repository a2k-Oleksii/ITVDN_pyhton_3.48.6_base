a = [1, 4, 7, 2, 8]


def iter_arr(array):
    for elem in array:
        print(elem)

def iter_rec(array, index=0):
    if index < len(array):
        print(array[index])
        index += 1
        iter_rec(array, index)


iter_rec(a) 
