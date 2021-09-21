# Задание 1. Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе
# издания и жанре. Создайте несколько разных книг. Определите для него операции проверки на
# равенство и неравенство, методы __repr__ и __str__.
# Задание 2. Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
# так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.

class Book:

    def __init__(self, author, name_book, year_of_publishing, genre):
        self.author = author
        self.name_book = name_book
        self.year_of_publishing = year_of_publishing
        self.genre = genre
        self.list_review = []

    def __repr__(self) -> str:
        return "Book - {}, author - {}, year of publushed - {}, genre - {}".format(
            self.name_book, 
            self.author, 
            self.year_of_publishing, 
            self.genre
            )

    def __str__(self) -> str:
        return "Book - {}\n\tauthor - {}\n\tyear of publushed - {}\n\tgenre - {}\n\treview - {}".format(
            self.name_book, 
            self.author, 
            self.year_of_publishing, 
            self.genre,
            self.get_review()
            )
    
    def get_review(self):
        all_review = ''
        for element in self.list_review:
            all_review += '{}\n\t\t'.format(element)
        return all_review
 
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

    def add_review(self, review):
        self.list_review.append(review)


class Review:
    def __init__(self, text_review):        
        self.text_review = text_review

    def __repr__(self):
        return self.text_review


class main:
    book_1 = Book('Lev Tolstoy', 'War and peace', 1898, 'Drama')
    book_2 = Book('Jhoan Rolling', 'Harry Potter', 2001, 'Fantasy')
    book_3 = Book('Boris Strugatskiy', 'Picknik in road', 1968, 'Fantasy')
    review_1 = Review("This is very good book")
    review_2 = Review("WoW !")
    book_1.add_review(review_2)
    book_1.add_review(review_1)

    print(book_1)
    print(book_2)
    print(book_3)


if __name__ == '__main__':
    main()
    