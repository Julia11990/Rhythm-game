#Contrller
from Model import *
from View import *
from level1 import *

import flet as ft

def main(page: ft.Page):
    page.title = "Меню"
    input_fild = ft.TextFeld(label = "Введи номер действия")
    ouput_text = ft.Text()
    
    def on_button_click(e):
        output_text.value = f"Вы выбрали: { input_field.value}"
        page.updaete() 
        
    choice = output_text 
     if choice == "1":
        levels_list = levels_menu()
        show_levels(levels_list)
    elif choice =="2":
        level1 =  _init_(self)
        show_level1(level1)
    elif choice == "0":
        break
    else:
        print("Такого действия нет")
    page.add(input_field, button, output_text)
    label = ft.Text(actions)
ft.app(target=main)
