# TODO Написать 3 класса с документацией и аннотацией типов
class Table:
    """
    Class representing a table.

    Attributes:
    material (str): Материал стола (например, дерево, металл).
    legs (int): Количество ножек у стола.

    Methods:
    set_up(self) -> str:
    Подготовьте стол к использованию.

    clean_surface(self) -> str:
    Очистите поверхность стола.

    adjust_legs(self) -> str:
    Отрегулируйте ножки стола для устойчивости.

    """

    def __init__(self, material: str, legs: int) -> None:
        """
        Инициализируйте стол, указав материал и количество ножек.
        Например:
        >>> table = Table("wood", 4)

        Args:
        material (str): Материал, из которого изготовлен стол.
        legs (int): Количество ножек у стола.

        Raises:
        ValueError: Если кол-во ножек не является положительным целым числом.

        """

        self.material = material
        self.legs = legs
        ...
        # Initialization of attributes


class Door:
    """
    Class representing a door.

    Attributes:
    material (str): Материал двери (например, дерево, металл).
    height (float): Высота двери в метрах.

    Methods:
    open(self) -> str:
    Открыть дверь.

    close(self) -> str:
    Закрыть дверь.

    lock(self) -> str:
    Запереть дверь.

    """

    def __init__(self, material: str, height: float) -> None:
        """
        Initialize a Door with material and height.
        Например:
        >>> door = Door("wood", 2.7)

        Args:
        material (str): Материал двери.
        height (float): Высота двери в метрах.

        Raises:
        ValueError: Если высота не является положительным числом.

        """

        self.material = material
        self.height = height
        ...
        # Initialization of attributes


class Keyboard:
    """
    Class representing a keyboard.

    Attributes:
    layout (str): Раскладка клавиатуры (например, QWERTY).
    keys (int): Количество клавиш на клавиатуре.

    Methods:
    type_text(self, text: str) -> str:
    Введите указанный текст с клавиатуры.

    clean_keys(self) -> str:
    Очистите клавиши клавиатуры.

    change_layout(self, new_layout: str) -> str:
    Измените раскладку клавиатуры.

    """

    def __init__(self, layout: str, keys: int) -> None:
        """
        Инициализируйте клавиатуру с помощью раскладки и количества клавиш.
        Например:
        >>> keyboard = Keyboard("QWERTY", 110)

        Args:
        layout (str): Раскладка клавиатуры.
        keys (int): Количество клавиш на клавиатуре.

        Raises:
        ValueError: Если количество клавиш не является положительным целым числом.
        """

        self.layout = layout
        self.keys = keys
        ...
        # Initialization of attributes


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest

    doctest.testmod()
