import pygame
import sys

pygame.init()
width, height = 600, 800
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

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


notes = []
note_spawn_time = 0
score = 0

running = True
while running:
    clock.tick(60)
    window.fill((30, 30, 30))

    # Добавление нот
    note_spawn_time += 1
    if note_spawn_time > 60:  # Нота появляется каждую секунду
        notes.append(Note(300, 0, 5))
        note_spawn_time = 0

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Нажатие клавиши для "удара"
                for note in notes:
                    if 700 < note.y < 770:  # Зона попадания по ноте
                        score += 1
                        notes.remove(note)
                        break

    # Движение и отрисовка нот
    for note in notes:
        note.move()
        note.draw(window)
        if note.y > height:
            notes.remove(note)  # Нота пропущена

    # Отображение счета
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f'Счет: {score}', True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
