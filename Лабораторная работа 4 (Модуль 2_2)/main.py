
class Animal:
    """Базовый класс для животных"""
    def __init__(self, name: str, age: int):
        """Инициализация атрибутов объекта"""
        self.name = name  # Имя животного
        self.age = age  # Возраст животного
        self.format_age()  # Форматированный возраст

    def make_sound(self) -> str:
        """Метод для издания звука"""
        pass

    def format_age(self) -> str:
        """Метод для форматирования возраста с правильной формой."""
        age = self.age
        if age % 10 == 1 and age % 100 != 11:
            suffix = "год"
        elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
            suffix = "года"
        else:
            suffix = "лет"
        return f"{age} {suffix}"

    def __str__(self) -> str:
        """Возвращает строковое представление объекта"""
        return f"{self.name}, {self.format_age()}"

    def __repr__(self) -> str:
        """Возвращает представление объекта"""
        return f"Animal('{self.name}', {self.age})"


class Cat(Animal):
    """Дочерний класс для кошек"""

    def __init__(self, name: str, age: int, color: str):
        """
        Инициализация атрибутов объекта.
        Args:
        name: Имя кошки.
        age: Возраст кошки.
        color: Цвет шерсти.
        """
        super().__init__(name, age)
        self.color = color  # Цвет шерсти

    def make_sound(self) -> str:
        """Переопределение метода родительского класса"""
        return "Meow!"

    def hunt(self, prey: str) -> str:
        """
        Метод для охоты на добычу.
        Args:
        prey: Добыча, на которую охотится кошка.
        Returns:
        Результат охоты.
        """
        return f"{self.name} поймала {prey}!"

    def __str__(self) -> str:
        """Возвращает строковое представление объекта"""
        return f"{self.name}, {self.format_age()}, {self.color}"

    def __repr__(self) -> str:
        """Возвращает представление объекта"""
        return f"Cat('{self.name}', {self.age}, '{self.color}')"


class Dog(Animal):
    """Дочерний класс для собак"""

    def __init__(self, name: str, age: int, breed: str):
        """
        Инициализация атрибутов объекта.
        Args:
        name: Имя собаки.
        age: Возраст собаки.
        breed: Порода собаки.
        """
        super().__init__(name, age,)
        self.breed = breed  # Порода собаки

    def make_sound(self) -> str:
        """Переопределение метода родительского класса"""
        return "Woof!"

    def fetch(self, item: str) -> str:
        """
        Метод для приношения предмета.
        Args:
        item: Предмет, который приносит собака.
        Returns:
        Результат приношения.
        """
        return f"{self.name} принёс {item}!"

    def __str__(self) -> str:
        """Возвращает строковое представление объекта"""
        return f"{self.name}, {self.format_age()}, {self.breed}"

    def __repr__(self) -> str:
        """Возвращает представление объекта"""
        return f"Dog('{self.name}', {self.age}, '{self.breed}')"


if __name__ == "__main__":
    # Создаем экземпляр класса Animal
    animal = Animal("Тайга", 3)
    print(animal)  # Выводит: Тайга, 3 года

    # Создаем экземпляр класса Cat
    cat = Cat("Феликс", 5, "чёрный")
    print(cat)  # Выводит: Феликс, 5 лет, чёрный
    print(cat.make_sound())  # Вызываем метод издания звука
    print(cat.hunt("мышь"))  # Вызываем метод охоты

    # Создаем экземпляр класса Dog
    dog = Dog("Голди", 1, "Золотой ретривер")
    print(dog)  # Выводит: Голди, 1 год, Золотой ретривер
    print(dog.make_sound())  # Вызываем метод издания звука
    print(dog.fetch("мяч"))  # Вызываем метод для приношения предмета
