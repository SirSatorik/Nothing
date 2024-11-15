class Vector2:
    def __init__(self,
                 x : int,
                 y : int) -> None:
        """
        Инициализирует класс вектора 2 (Vector2)

        Args:
            x - позиция вектора по x

            y - позиция вектора по y

        Return:
        """
        self.x = x
        self.y = y

    def __len__(self) -> int:
        return self.x + self.y
