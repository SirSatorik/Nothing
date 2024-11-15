import random

class Colors:
    def __init__(self) -> None:
        """
        Инициализирует класс Colors

        Args:

        Return:
        """

        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

    def create_random_color_rgb(self,
                                min : tuple,
                                max : tuple) -> tuple:
        """
        Генерирует рандомный цвет

        Args:
            min - минимальное значение
            max - максимальное значение

        Return:
            цвет в виде tuple (RGB)
        """

        color = (
            random.randint(min[0], max[0]),
            random.randint(min[1], max[1]),
            random.randint(min[2], max[2])
        )

        return color
