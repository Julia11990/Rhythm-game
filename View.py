from Model import *
from View import *
def display_menu():
    print("\nВыбери действие: 1-выбрать уровень, 2-начать игру, 0-выйти")
    choise = input("Выбери номер действия:")

    return choise

def show_levels(levels_list):
    print("\nВыбери уровень:")
    print("Уровни:")
    for i, levels in enumerate(levels_list):
        print(f"{i}. {levels}")
