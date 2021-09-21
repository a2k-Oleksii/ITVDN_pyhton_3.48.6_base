# Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе
# издания и жанре. Создайте несколько разных книг. Определите для него операции проверки на
# равенство и неравенство, методы __repr__ и __str__.

class Book:   
    def __init__(self, author, name_book, year_of_publishing, genre):
        self.author = author
        self.name_book = name_book
        self.year_of_publishing = year_of_publishing
        self.genre = genre

    def __repr__(self) -> str:
        return "Book - {}, author - {}, year of publushed - {}, genre - {}".format(
            self.name_book, 
            self.author, 
            self.year_of_publishing, 
            self.genre
            )

    def __str__(self) -> str:
        return "Book - {}\n\tauthor - {}\n\tyear of publushed - {}\n\tgenre - {}".format(
            self.name_book, 
            self.author, 
            self.year_of_publishing, 
            self.genre
            )
    
    def __eq__(self, other):
        return (
                self.name_book == other.name_book 
            and self.author == other.author 
            and self.year_of_publishing == other.year_of_publishing
            and self.genre == other.genre
            )

    def __ne__(self, other):
            return (
                self.name_book != other.name_book 
            and self.author != other.author 
            and self.year_of_publishing != other.year_of_publishing
            and self.genre != other.genre
            )


class main:
    book_1 = Book('Lev Tolstoy', 'War and peace', 1898, 'Drama')
    book_2 = Book('Jhoan Rolling', 'Harry Potter', 2001, 'Fantasy')
    book_3 = Book('Boris Strugatskiy', 'Picknik in road', 1968, 'Fantasy')

    print(book_1)
    print(book_2)
    print(book_3)

    print(book_2 == book_2)
    print(book_1 == book_2)
    print(book_2 != book_2)
    print(book_1 != book_2)


if __name__ == '__main__':
    main()
    
