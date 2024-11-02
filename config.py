import os

class Resources:
    def __init__(self) -> None:
        """
        Инициализирует класс Resources

        Args:
            Ничего

        Return:
            Ничего
        """

        self.start_path = os.path.dirname(os.path.abspath(__file__))

        self.textures = {
            "player": "content/new_images/player.png"
        }

    def check_files(self) -> tuple:
        """
        Проверяет существуют ли файлы в словаре textures

        Args:
            Ничего

        Return:
            Ничего
        """

        for key in self.textures:
            if os.path.exists(self.textures[key]):
                return (True, f"Complete textures {key} : {self.textures[key]}")
            else:
                return (False, f"Error textures! {key} : {self.textures[key]}")
