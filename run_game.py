from display_board import display_board
# from check_win import check_win
def run_game(player1_choice, player2_choice):
    board_data = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    board_filled = 0
    while board_filled < 10:
        print('Player 1 chance \n')
        board_position_p1 = int(input('Enter board position: '))
        board_data[board_position_p1 - 1] = player1_choice
        display_board(board_data)
        check_win(board_data, player1_choice)
        print('Player 2 chance \n')
        board_position_p2 = int(input('Enter board position: '))
        board_data[board_position_p2 - 1] = player2_choice
        display_board(board_data)
        check_win(board_data, player2_choice)
        
