from random import randint
def first_chance():
    return "Player1" if randint(1,2) == 1 else "Player2"