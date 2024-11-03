import pygame

import geometry
from colors import Colors

class Player:
    def __init__(self,
                 x : int,
                 y : int,
                 size : tuple,
                 geometry : geometry.Geometry,
                 textures : dict) -> None:
        """
        Инициализирует класс Player

        Args:
            Ничего

        Return:
            Ничего
        """

        self.x = x
        self.y = y

        self.size = size

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        self.is_move = True

        self.geometry = geometry
        self.textures = textures

        self.speed = 0.5

    def draw(self,
             screen: pygame.surface.Surface) -> None:
        """
        Отрисовывает игрока

        Args:
            screen - экран для отрисовки

        Return:
            Ничего
        """

        raw_texture = pygame.image.load(self.textures["player"])
        texture = self.geometry.resize_image_proportionally(
            raw_texture,
            self.size)

        if self.moving_right:
            texture = pygame.transform.flip(texture, True, False)

        screen.blit(texture, (self.x, self.y))

    def new_event(self,
                  event : pygame.event) -> None:
        """
        Обрабатывает эвенты

        Args:
            event - эвент

        Return:
            Ничего
        """

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.moving_left = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.moving_right = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.moving_up = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.moving_left = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.moving_right = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.moving_up = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.moving_down = False

    def move(self) -> None:
        """
        Перемещает игрока

        Args:
            Ничего

        Return:
            Ничего
        """

        if self.is_move:
            if self.moving_left:
                self.x -= self.speed
            if self.moving_right:
                self.x += self.speed
            if self.moving_up:
                self.y -= self.speed
            if self.moving_down:
                self.y += self.speed
