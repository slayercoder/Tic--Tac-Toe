def check_existing_position(input_position, board_positions):
    has_existing_position = True
    while has_existing_position:
        if input_position in board_positions:
            print('Position is already filled, please enter different position')
            new_position = int(input('Enter position: '))
        else:
            has_existing_position = False
            
check_existing_position(2, [2, 3])
