import pygame

from worlds import Worlds
from config import *

class Game:
    def __init__(self) -> None:
        """
        Инициализирует класс Game

        Args:
            Ничего

        Return:
            Ничего
        """

        pass

    def set_scene(self,
                  scene : object) -> None:
        """
        Производит смену сцены

        Args:
            scene - сцена на которую идёт переход

        Return:
            Ничего
        """
        scene()

    def start(self) -> None:
        """
        Запускает игру

        Args:
            Ничего

        Return:
            Ничего
        """

        resources = Resources()

        file_check_result = resources.check_files()
        print(file_check_result[1])
        if not file_check_result[0]:
            exit(FileNotFoundError)

        # Инициализация Pygame
        pygame.init()

        display_info = pygame.display.Info()

        # Создание окна с начальным размером
        screen = pygame.display.set_mode((display_info.current_w / 2, display_info.current_h / 2), pygame.RESIZABLE)


        current_screen_size = screen.get_size()
        fullscreen_size = (display_info.current_w, display_info.current_h)
        is_fullscreen = False
        last_screen_size = current_screen_size

        virtual_screen = pygame.Surface((display_info.current_w / 2, display_info.current_h / 2))

        worlds = Worlds(screen,
                        virtual_screen,
                        current_screen_size,
                        last_screen_size,
                        fullscreen_size,
                        is_fullscreen,
                        self.set_scene
                        )

        self.set_scene(worlds.home_scene())

        # Завершение Pygame
        pygame.quit()

if __name__ == "__main__":
    new_game = Game()
    new_game.start()
