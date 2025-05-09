#Contrller
import pygame
import sys
from Model import Note, Bonus
from View import Interface
import random

pygame.init()  # Инициализация Pygame

width, height = 600, 800  # Размеры окна
window = pygame.display.set_mode((width, height))  # Создание окна
clock = pygame.time.Clock()  # Часы для контроля FPS

# Загрузка музыки и звуков
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

note_sound = pygame.mixer.Sound('zvuk-notyi-do-vo-vtoroy-oktave.wav')
bonus_sound = pygame.mixer.Sound('zvuk-notyi-si.wav')

interface = Interface()  # Создание интерфейса
notes = []  # Список нот
bonuses = []  # Список бонусов

note_spawn_time = 0  # Таймер для спавна нот
bonus_spawn_time = 0  # Таймер для спавна бонусов
score = 0  # Счет
game_over = False  # Флаг окончания игры

while True:
    clock.tick(60)  # Ограничение FPS до 60
    window.fill((30, 30, 30))  # Фон окна

    if not game_over:
        note_spawn_time += 1  # Увеличение таймера спавна нот
        if note_spawn_time > 60:
            # Спавн новой ноты
            notes.append(Note(random.randint(50, width - 50), 0, 5))
            note_spawn_time = 0  # Сброс таймера

        bonus_spawn_time += 1  # Увеличение таймера спавна бонусов
        if bonus_spawn_time > 120:
            # Спавн нового бонуса
            bonuses.append(Bonus(random.randint(50, width - 50), 0, 5))
            bonus_spawn_time = 0  # Сброс таймера

        for event in pygame.event.get():  # Обработка событий
            if event.type == pygame.QUIT:
                pygame.quit()  # Закрытие игры
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Проверка нажатия пробела для захвата нот и бонусов
                    for note in notes:
                        if 700 < note.y < 770:  # Если нота достигла определенной высоты
                            score += 1
                            note_sound.play()  # Проигрывание звука
                            notes.remove(note)  # Удаление ноты
                            break
                    for bonus in bonuses:
                        if 700 < bonus.y < 770:  # Если бонус достиг определенной высоты
                            
                            score += 5
                            bonus_sound.play()  # Проигрывание звука
                            bonuses.remove(bonus)  # Удаление бонуса
                            break
                if event.key == pygame.K_r and game_over:
                    # Перезапуск игры
                    score = 0
                    game_over = False
                    notes.clear()  # Очистка нот
                    bonuses.clear()  # Очистка бонусов

        # Движение и отрисовка нот
        for note in notes:
            note.move()
            note.draw(window)
            if note.y > height:  # Проверка на выход за экран
                game_over = True

        # Движение и отрисовка бонусов
        for bonus in bonuses:
            bonus.move()
            bonus.draw(window)
            if bonus.y > height:  # Проверка на выход за экран
                game_over = True

        interface.draw_score(window, score)  # Отображение счета

    else:
        interface.draw_game_over(window)  # Отображение сообщения об окончании игры

    pygame.display.flip()  # Обновление экрана
 





