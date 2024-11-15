import pygame
import math

from Vector2 import Vector2
import geometry

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

        Return:

        """

        self.position = Vector2(x, y)
        self.angle = 0

        self.event : pygame.event = pygame.event

        self.size = size

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        self.is_move = True

        self.geometry = geometry
        self.textures = textures

        self.speed = 0.5

        raw_texture = pygame.image.load(self.textures["player"])

        self.texture = self.geometry.resize_image_proportionally(
            raw_texture,
            self.size)

    def look_at(self,
                target_x : int,
                target_y : int) -> None:
        """Поворачивает игрока в сторону целевых координат.

        Args:
            target_x - позиция куда надо посмотреть по x

            target_y - позиция куда надо посмотреть по y
        Return:
        """

        # Вычисляем разницу координат
        dx = target_x - self.position.x
        dy = target_y - self.position.y

        # Вычисляем угол в радианах
        angle_rad = math.atan2(dy, dx)

        # Преобразуем угол в градусы
        angle_deg = math.degrees(angle_rad)

        # Корректируем угол, чтобы он был в диапазоне 0-360 градусов
        angle_deg = (angle_deg + 360) % 360

        # Плавный поворот (можно настроить скорость поворота)
        rotation_speed = 5  # Градусов в кадре
        if self.angle != angle_deg:
            if abs(self.angle - angle_deg) <= rotation_speed:
                self.angle = angle_deg
            elif self.angle < angle_deg:
                self.angle = min(self.angle + rotation_speed, angle_deg)
            else:
                self.angle = max(self.angle - rotation_speed, angle_deg)

    def draw(self,
             screen: pygame.surface.Surface) -> None:
        """
        Отрисовывает игрока

        Args:
            screen - экран для отрисовки

        Return:
        """

        texture = pygame.transform.flip(self.texture, self.moving_right, False)

        screen.blit(texture, (self.position.x, self.position.y))

    def new_event(self,
                  event : pygame.event) -> None:
        """
        Обрабатывает эвенты

        Args:
            event - эвент

        Return:
        """

        self.event = event

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

        Return:
        """

        if self.is_move:
            if self.moving_left:
                self.position.x -= self.speed
            if self.moving_right:
                self.position.x += self.speed
            if self.moving_up:
                self.position.y -= self.speed
            if self.moving_down:
                self.position.y += self.speed
