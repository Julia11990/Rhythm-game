#Model
levels = ["1"]

actions ["1-выбрать уровень", "2-начать игру", "0-выйти"]

def add_levels(title):
    levels.append(title)
    
def add_actions(title):
    actions.append(title)

def get_levels():
    return levels
    
def get_actions():
    return actions