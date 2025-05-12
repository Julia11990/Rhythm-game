#Model
import random

width, height = 600, 800  # Используется в контроллере и моделях

class Note:
    def init(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = 30

    def move(self):
        self.y += self.speed


class Bonus:
    def init(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = 20

    def move(self):
        self.y += self.speed


class GameState:
    def init(self):
        self.notes = []
        self.bonuses = []
        self.note_spawn_timer = 0
        self.bonus_spawn_timer = 0
        self.score = 0
        self.game_over = False

    def spawn_note(self):
        self.notes.append(Note(random.randint(50, width - 50), 0, 5))

    def spawn_bonus(self):
        self.bonuses.append(Bonus(random.randint(50, width - 50), 0, 5))
