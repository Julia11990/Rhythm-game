from Model import *
from View import *

def main():
    choice = display_menu()
    print(choice)
    if choice == "1":
        levels_list = get_levels()
        show_levels(levels_list)
    elif choice =="2":
        print("3...")
        print("2...")
        print("1...")
        print("start")
