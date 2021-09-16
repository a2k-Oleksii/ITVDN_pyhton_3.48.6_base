class Cat:

    def __init__(self, color, cat_type):
        self.size = ''
        self.color = color
        self.cat_type = cat_type

    def set_size(self):
        if self.cat_type == 'indoor':
            self.size = 'small'
        else:
            self.size = 'underfined'


class Tiger(Cat):
    def __init__(self, color, cat_type):
        Cat.__init__(self, color, cat_type)

    def set_size(self):
        if self.cat_type == 'wild':
            self.size = 'big'
        else:
            self.size = 'underfined'


cat = Cat(color='white', cat_type='british')
cat2 = Cat(color='black', cat_type='indoor')
cat.set_size()
cat2.set_size()
print(cat.size)
print(cat2.size)
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
tiger = Tiger(color='white', cat_type='wild')
tiger2 = Tiger(color='black', cat_type='indoor')
tiger.set_size()
tiger2.set_size()
print(tiger.size)
print(tiger2.size)
