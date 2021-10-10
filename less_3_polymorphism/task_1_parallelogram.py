class Parallelogram:
    def __init__(self, width, length):
        self._width = width
        self._length = length
    
    def get_area(self):
        return self._width * self._length


class Square(Parallelogram):
    def get_area(self):
        return self._width * self._length
