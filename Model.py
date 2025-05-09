#Model
import random

class Note:
    def __init__(self, x, y, speed):
        self.x = x  # Позиция по оси X
        self.y = y  # Позиция по оси Y
        self.speed = speed  # Скорость падения
        self.radius = 30  # Радиус ноты

    def move(self):
        self.y += self.speed  # Перемещение вниз по Y

    def draw(self, surface):
        # Рисование ноты 
        pygame.draw.circle(surface, (255, 255, 0), (self.x, int(self.y)), self.radius)


class Bonus:
    def __init__(self, x, y, speed):
        self.x = x  # Позиция по оси X
        self.y = y  # Позиция по оси Y
        self.speed = speed  # Скорость падения
        self.radius = 20  # Радиус бонуса

    def move(self):
        self.y += self.speed  # Перемещение вниз по Y

    def draw(self, surface):
        # Рисование бонуса
        pygame.draw.circle(surface, (0, 255, 0), (self.x, int(self.y)), self.radius)
