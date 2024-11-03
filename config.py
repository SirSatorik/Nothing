import os
import json

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

        self.textures = self.read_data("config.json")["textures"]

    def read_data(self,
                  file_path : str) -> dict:
        """
        Считывает json файл и возвращает его дпнные

        Args:
            file_path - путь к json

        Return:
            Данные json файла типа dict
        """

        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return {}

    # Запись данных в JSON файл
    def write_data(self,
                   data : dict,
                   file_path : str) -> None:
        """
        Записывает json файл

        Args:
            data - данные для записи типа dict

            file_path - путь к json

        Return:
            Ничего
        """

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

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
