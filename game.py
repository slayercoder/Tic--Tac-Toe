from welcome_screen import welcome_screen
from player_choice import player_choice
from run_game import run_game

def main_game():
    welcome_screen()
    player1, player2 = player_choice()
    run_game(player1, player2)
main_game()
