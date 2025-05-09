#View
import pygame

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
