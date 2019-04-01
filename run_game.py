from display_board import display_board
from first_chance import first_chance
# from check_existing_position import check_existing_position
# from check_win import check_win
def run_game(player1_choice, player2_choice):
    board_data = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    # board_filled = 0
    board_position_filled = []
    first_turn = first_chance()
    while True:
        print('Player 1 chance')
        # ask the player to select location and symbol to fill and take input
        location_p1 = int(input('Player 1 Enter location on board '))
        player_1_data = (player1_choice, location_p1)

        # check whether location to fill exists from previous step
        has_location = not board_data[location_p1 - 1] == ('X' or 'O')
        
        # if location exists take the input position and insert in the board data
        if has_location:
            board_data[location_p1 - 1] = player1_choice
            
        # after this check if the user has won, if yes break out and print result else continue 




















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

