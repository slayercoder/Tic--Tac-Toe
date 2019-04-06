from display_board import display_board
from first_chance import first_chance
from make_move import make_move
# from check_existing_position import check_existing_position
from check_win import check_win
def run_game(player1_choice, player2_choice):
    board_data = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    # positions_filled = [0]
    # board_position_filed = []
    winner = ''
    current_player = first_chance()
    current_player_choice = player1_choice if current_player == 'Player 1' else player2_choice
    while True:
        current_player_choice, locations_filled = make_move(current_player, board_data, current_player_choice)
        display_board(board_data)

        if locations_filled == 9:
            print('Math is drawn !!')
            break
        # after this, check if the user has won, if yes break out and print result else continue        
        if check_win(board_data, current_player_choice):
            winner = current_player
            break
        else:
            # toggle player
            current_player = "Player 2" if current_player == 'Player 1' else "Player 1"
            current_player_choice = player1_choice if current_player == 'Player 1' else player2_choice
            continue
    if winner:
        return winner
    


















    #     print('Player 1 chance \n')
    #     board_position_p1 = int(input('Enter board position: '))
    #     # check_existing_position(board_position_p1, board_position_filled)
    #     while board_position_p1 in board_position_filled:

    #     board_data[board_position_p1 - 1] = player1_choice
    #     display_board(board_data)
    #     check_win(board_data, player1_choice)
    #     print('Player 2 chance \n')
    #     board_position_p2 = int(input('Enter board position: '))
    #     board_data[board_position_p2 - 1] = player2_choice
    #     display_board(board_data)
    #     check_win(board_data, player2_choice)

