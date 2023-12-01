import doctest


class TV:
    def __init__(self, brand: str, screen_size: float, is_smart: bool):
        """
        Создание объекта Телевизор

        :param brand: Марка телевизора
        :param screen_size: Размер экрана в дюймах
        :param is_smart: Флаг, указывающий, является ли телевизор умным

        Примеры:
        >>> tv = TV('Samsung', 55, True)
        """
        if not isinstance(brand, str):
            raise TypeError('Марка телевизора должна быть строкой')
        self.brand = brand

        if not isinstance(screen_size, (int, float)):
            raise TypeError('Размер экрана должен быть числом')
        if screen_size <= 0:
            raise ValueError('Размер экрана должен быть положительным числом')
        self.screen_size = screen_size

        if not isinstance(is_smart, bool):
            raise TypeError('Флаг "is_smart" должен быть типа bool')
        self.is_smart = is_smart

    def turn_on(self) -> str:
        """
        Включение телевизора.

        :return: Сообщение о включении

        Примеры:
        >>> tv = TV("Sony", 42, True)
        >>> tv.turn_on()
        """
        ...

    def change_channel(self, channel: int) -> None:
        """
        Смена канала на телевизоре.

        :param channel: Номер канала

        Примеры:
        >>> tv = TV("LG", 50, True)
        >>> tv.change_channel(5)
        """
        ...

    def adjust_volume(self, volume_level: int) -> None:
        """
        Регулировка громкости на телевизоре.

        :param volume_level: Уровень громкости

        Примеры:
        >>> tv = TV("Panasonic", 60, False)
        >>> tv.adjust_volume(25)
        """
        ...


class Book:
    def __init__(self, title: str, author: str, genre: str, num_pages: int):
        """
        Создание объекта Книга

        :param title: Название книги
        :param author: Автор книги
        :param genre: Жанр книги
        :param num_pages: Количество страниц в книге

        Примеры:
        >>> book = Book('Povest', 'A.S. Sukhov', 'Fiction', 99)
        """
        if not isinstance(title, str):
            raise TypeError('Название книги должно быть строкой')
        self.title = title

        if not isinstance(author, str):
            raise TypeError('Автор книги должен быть строкой')
        self.author = author

        if not isinstance(genre, str):
            raise TypeError('Жанр книги должен быть строкой')
        self.genre = genre

        if not isinstance(num_pages, int):
            raise TypeError('Количество страниц должно быть целым числом')
        if num_pages <= 0:
            raise ValueError('Количество страниц должно быть положительным числом')
        self.num_pages = num_pages

    def read(self, pages_to_read: int) -> str:
        """
        Чтение книги.

        :param pages_to_read: Количество страниц для чтения

        :return: Сообщение о прочитанных страницах

        Примеры:
        >>> book = Book('To Kill a Mockingbird', 'Harper Lee', 'Classic', 281)
        >>> book.read(50)
        """
        ...

    def get_book_info(self) -> str:
        """
        Получение информации о книге.

        :return: Информация о книге

        Примеры:
        >>> book = Book('1984', 'George Orwell', 'Dystopian', 328)
        >>> book.get_book_info()
        """
        ...


class Human:
    def __init__(self, name: str, age: int, gender: str):
        """
        Создание объекта Человек

        :param name: Имя человека
        :param age: Возраст человека в годах
        :param gender: Пол человека

        Примеры:
        >>> person = Human('John Doe', 30, 'Male')
        """
        if not isinstance(name, str):
            raise TypeError('Имя человека должно быть строкой')
        self.name = name

        if not isinstance(age, int):
            raise TypeError('Возраст человека должен быть целым числом')
        if age < 0:
            raise ValueError('Возраст человека не может быть отрицательным числом')
        self.age = age

        if not isinstance(gender, str):
            raise TypeError('Пол человека должен быть строкой')
        self.gender = gender

    def eat(self, food: str) -> str:
        """
        Функция, представляющая процесс приема пищи человеком.

        :param food: Пища, которую человек ест

        :return: Сообщение о приеме пищи

        Примеры:
        >>> person = Human('Alice', 25, 'Female')
        >>> person.eat('Pizza')
        """
        ...

    def sleep(self, hours: int) -> str:
        """
        Функция, представляющая процесс сна человека.

        :param hours: Количество часов сна

        :return: Сообщение о сне

        Примеры:
        >>> person = Human('Bob', 35, 'Male')
        >>> person.sleep(8)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
