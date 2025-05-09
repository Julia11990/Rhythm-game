#Contrller
import pygame
import sys
from Model import Note, Bonus
from View import Interface
import random

pygame.init()

width, height = 600, 800
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

note_sound = pygame.mixer.Sound('note_sound.wav')
bonus_sound = pygame.mixer.Sound('bonus_sound.wav')

interface = Interface()
notes = []
bonuses = []

note_spawn_time = 0
bonus_spawn_time = 0
score = 0
game_over = False

while True:
    clock.tick(60)
    window.fill((30, 30, 30))

    if not game_over:
        note_spawn_time += 1
        if note_spawn_time > 60:
            notes.append(Note(random.randint(50, width - 50), 0, 5))
            note_spawn_time = 0

        bonus_spawn_time += 1
        if bonus_spawn_time > 120:
            bonuses.append(Bonus(random.randint(50, width - 50), 0, 5))
            bonus_spawn_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for note in notes:
                        if 700 < note.y < 770:
                            score += 1
                            note_sound.play()
                            notes.remove(note)
                            break
                    for bonus in bonuses:
                        if 700 < bonus.y < 770:
                            score += 5
                            bonus_sound.play()
                            bonuses.remove(bonus)
                            break
                if event.key == pygame.K_r and game_over:
                    score = 0
                    game_over = False
                    notes.clear()
                    bonuses.clear()

        for note in notes:
            note.move()
            note.draw(window)
            if note.y > height:
                game_over = True

        for bonus in bonuses:
            bonus.move()
            bonus.draw(window)
            if bonus.y > height:
                game_over = True

        interface.draw_score(window, score)

    else:
        interface.draw_game_over(window)
        
