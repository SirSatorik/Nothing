import pygame

class Geometry:
    def __init__(self) -> None:
        """
        Инициализирует класс Geometry

        Args:

        Return:
        """
        pass

    def resize_image_proportionally(self,
                                    image : pygame.surface.Surface,
                                    width_height : tuple) -> pygame.surface.Surface:
        """
        Уменьшает изображение пропорционально, чтобы оно поместилось в заданные размеры

        Args:
            image - изображение
            width_height - кортеж (tuple) вида (ширина, высота)

        Returns:
            Новое уменьшенное изображение
        """

        width, height = image.get_size()

        # Вычисляем коэффициент масштабирования по ширине и высоте
        scale_x = width_height[0] / width
        scale_y = width_height[1] / height

        # Выбираем меньший коэффициент масштабирования, чтобы изображение не искажалось
        scale = min(scale_x, scale_y)

        # Масштабируем изображение
        new_width = int(width * scale)
        new_height = int(height * scale)
        resized_image = pygame.transform.scale(image, (new_width, new_height))

        return resized_image

    def calculate_width_height_from_radius(self,
                                           radius : int) -> tuple:
        """
        Вычисляет ширину и высоту квадрата, в который вписывается круг заданного радиуса

        Args:
            radius - радиус круга

        Return:
            Кортеж (tuple) в виде (ширина, высота)
        """

        # Диаметр круга
        diameter = radius * 2

        # Ширина и высота квадрата равны диаметру круга
        width = diameter
        height = diameter

        return (width, height)
