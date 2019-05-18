def make_move(current_player, board_data, current_player_choice):
    player_name = 'Player 1' if current_player == 'Player 1' else 'Player 2'
    print('{} ({}) chance'.format(player_name, current_player_choice))
    while True:
        # ask the player to select location and symbol to fill and take input
        try:
            location_entered = int(input('{} ({}) please enter location on board (1 to 9) '.format(player_name, current_player_choice)))
        except ValueError:
            print('This is not a valid board position value, please enter again')
            continue
        except (KeyboardInterrupt, EOFError):
            break
        # check whether location to fill exists from previous step        
        if not (board_data[location_entered - 1] == 'X' or board_data[location_entered - 1] == 'O'):
        # if location exists take the input position and insert in the board data
            board_data[location_entered - 1] = current_player_choice
            break
        else:
            print('Location already filled, please enter different location (1 to 9)')
            continue
    return current_player_choice