#View
import pygame
from model import width, height

class Interface:
    def init(self):
        self.font = pygame.font.SysFont(None, 36)

    def draw_score(self, surface, score):
        text = self.font.render(f'Счет: {score}', True, (255, 255, 255))
        surface.blit(text, (10, 10))

    def draw_game_over(self, surface):
        game_over_text = self.font.render('Игра окончена!', True, (255, 0, 0))
        restart_text = self.font.render('Нажмите R, чтобы перезапустить', True, (255, 255, 255))
        surface.blit(game_over_text, (width // 2 - 100, height // 2 - 20))
        surface.blit(restart_text, (width // 2 - 200, height // 2 + 20))

def draw_note(surface, note):
    pygame.draw.circle(surface, (255, 255, 0), (note.x, int(note.y)), note.radius)

def draw_bonus(surface, bonus):
    pygame.draw.circle(surface, (0, 255, 0), (bonus.x, int(bonus.y)), bonus.radius)