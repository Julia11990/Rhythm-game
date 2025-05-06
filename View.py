#View
from Model import *
from View import *
import flet as ft

def levels_menu():
    label2 = ft.Text(levels)
    input_fild2 = ft.TextFeld(label = "Введи номер уровня")
    ouput_text = ft.Text()
    
    def on_button_click(e):
        output_text.value = f"Вы выбрали: { input_field2.value}"
        page.updaete() 