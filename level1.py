import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Задаем размеры окна
width, height = 600, 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Музыкальная игра")
clock = pygame.time.Clock()

# Аудио (временно закомментировано, раскомментируйте при наличии файлов)
# pygame.mixer.music.load('music.mp3')
# pygame.mixer.music.play(-1)
# note_sound = pygame.mixer.Sound('note_sound.wav')
# bonus_sound = pygame.mixer.Sound('bonus_sound.wav')

# Классы

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


class Interface:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 36)

    def draw_score(self, surface, score):
        score_text = self.font.render(f'Счет: {score}', True, (255, 255, 255))
        surface.blit(score_text, (10, 10))

    def draw_game_over(self, surface):
        game_over_text = self.font.render('Игра окончена!', True, (255, 0, 0))
        restart_text = self.font.render('Нажмите R, чтобы перезапустить', True, (255, 255, 255))
        surface.blit(game_over_text, (width // 2 - 100, height // 2 - 20))
        surface.blit(restart_text, (width // 2 - 200, height // 2 + 20))


# Переменные

interface = Interface()
notes = []
bonuses = []

note_spawn_time = 0
bonus_spawn_time = 0

score = 0
game_over = False

# Основной цикл игры

while True:
    clock.tick(60)
    window.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                for note in notes[:]:
                    if 700 < note.y < 770:
                        score += 1
                        # note_sound.play()
                        notes.remove(note)
                        break
                for bonus in bonuses[:]:
                    if 700 < bonus.y < 770:
                        score += 5
                        # bonus_sound.play()
                        bonuses.remove(bonus)
                        break

            if event.key == pygame.K_r and game_over:
                score = 0
                game_over = False
                notes.clear()
                bonuses.clear()

    if not game_over:
        # Спавн нот
        note_spawn_time += 1
        if note_spawn_time > 60:
            notes.append(Note(random.randint(50, width - 50), 0, 5))
            note_spawn_time = 0

        # Спавн бонусов
        bonus_spawn_time += 1
        if bonus_spawn_time > 120:
            bonuses.append(Bonus(random.randint(50, width - 50), 0, 5))
            bonus_spawn_time = 0

        # Обработка нот
        for note in notes[:]:
            note.move()
            note.draw(window)
            if note.y > height:
                game_over = True

        # Обработка бонусов
        for bonus in bonuses[:]:
            bonus.move()
            bonus.draw(window)
            if bonus.y > height:
                game_over = True

        # Отображение счета
        interface.draw_score(window, score)

    else:
        interface.draw_game_over(window)

    pygame.display.flip()
