from utils.welcome_screen import welcome_screen
from utils.player_choice import player_choice
from utils.run_game import run_game
from utils.replay import replay

def main_game():
    is_replay = True
    while is_replay:
        welcome_screen()
        player1, player2 = player_choice()
        match_status = run_game(player1, player2)
        print('The match is {}'.format(match_status))
        is_replay = replay()
main_game()
