#Model
import random

class Note:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = 30

    def move(self):
        self.y += self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 0), (self.x, int(self.y)), self.radius)


class Bonus:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = 20

    def move(self):
        self.y += self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, (0, 255, 0), (self.x, int(self.y)), self.radius)

