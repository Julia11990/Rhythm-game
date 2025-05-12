#Contrller
import pygame
import sys
from model import GameState, width, height
from view import Interface, draw_note, draw_bonus

pygame.init()

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ритм игра")
clock = pygame.time.Clock()

# Музыка и звуки
# pygame.mixer.music.load('assets/music.mp3')
# pygame.mixer.music.play(-1)
# note_sound = pygame.mixer.Sound('assets/note.wav')
# bonus_sound = pygame.mixer.Sound('assets/bonus.wav')

interface = Interface()
state = GameState()

# Игровой цикл
while True:
    clock.tick(60)
    window.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not state.game_over:
                for note in state.notes:
                    if 700 < note.y < 770:
                        state.score += 1
                        # note_sound.play()
                        state.notes.remove(note)
                        break
                for bonus in state.bonuses:
                    if 700 < bonus.y < 770:
                        state.score += 5
                        # bonus_sound.play()
                        state.bonuses.remove(bonus)
                        break

            if event.key == pygame.K_r and state.game_over:
                state.init()  # Сброс состояния игры

    if not state.game_over:
        # Спавн
        state.note_spawn_timer += 1
        state.bonus_spawn_timer += 1
        if state.note_spawn_timer > 60:
            state.spawn_note()
            state.note_spawn_timer = 0
        if state.bonus_spawn_timer > 120:
            state.spawn_bonus()
            state.bonus_spawn_timer = 0

        # Движение и отрисовка нот
        for note in state.notes[:]:
            note.move()
            draw_note(window, note)
            if note.y > height:
                state.game_over = True
            for bonus in state.bonuses[:]:
            bonus.move()
            draw_bonus(window, bonus)
            if bonus.y > height:
                state.game_over = True

            interface.draw_score(window, state.score)
        else:
            interface.draw_game_over(window)

            pygame.display.flip()