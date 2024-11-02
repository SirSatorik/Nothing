import pygame
from colors import Colors
from player import Player
from geometry import Geometry
from config import *

class Worlds:
    def __init__(self,
                 screen : pygame.surface.Surface,
                 virtual_screen : pygame.surface.Surface,
                 current_screen_size : tuple,
                 last_screen_size : tuple,
                 fullscreen_size : tuple,
                 is_fullscreen : bool,
                 set_scene_def : object) -> None:
        """
        Инициализирует класс Game

        Args:
            screen - основной экран

            virtual_screen - виртуальный экран

            current_screen_size - текущий размер экрана

            last_screen_size - предыдущий размер экрана

            fullscreen_size - размер экрана при фулл скрине

            is_fullscreen - сейчас фулл скрин или нет

            set_scene_def - функция смены сцены


        Return:
            Ничего
        """

        self.screen = screen
        self.virtual_screen = virtual_screen
        self.is_fullscreen = is_fullscreen

        self.current_screen_size = current_screen_size
        self.last_screen_size = last_screen_size
        self.fullscreen_size = fullscreen_size

        self.geometry = Geometry()
        self.resources = Resources()
        self.textures = self.resources.textures
        self.colors = Colors()

    def home_scene(self) -> None:
        """
        Основная сцена игры

        Args:
             Ничего

        Return:
            Ничего
        """

        player = Player(300, 250, (60, 60), self.geometry, self.textures)

        running = True
        while running:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

                # Изменение размера окна
                if event.type == pygame.VIDEORESIZE:
                    self.current_screen_size = event.size

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        self.is_fullscreen = not self.is_fullscreen
                        if self.is_fullscreen:
                            self.last_screen_size = self.current_screen_size
                            self.current_screen_size = self.fullscreen_size
                            self.screen = pygame.display.set_mode(self.current_screen_size, pygame.FULLSCREEN)
                        else:
                            self.current_screen_size = self.last_screen_size
                            self.screen = pygame.display.set_mode(self.current_screen_size, pygame.RESIZABLE)

                player.new_event(event)
            self.current_screen_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)

            scaled_screen_surface = pygame.transform.scale(self.virtual_screen, self.current_screen_size)
            self.screen.blit(scaled_screen_surface, (0, 0))

            self.virtual_screen.fill((113, 146, 118))

            player.draw(self.virtual_screen)
            player.move()

            # Обновление экрана
            pygame.display.flip()
