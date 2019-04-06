from welcome_screen import welcome_screen
from player_choice import player_choice
from run_game import run_game
from replay import replay

def main_game():
    is_replay = True
    while is_replay:
        welcome_screen()
        player1, player2 = player_choice()
        winner = run_game(player1, player2)
        print('The winner is {}'.format(winner))
        is_replay = replay()
main_game()
