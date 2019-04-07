def player_choice():
    available_choice = 'OX'
    has_correct_input = False
    while not has_correct_input:
        player1 = input('Enter Player1\'s choice: ').upper()
        if player1 in available_choice:
            has_correct_input = True
        else:
            print('Incorrect input please enter again !!')
    player2 = 'O' if player1 == 'X' else 'X'
    print('''Player1 has chosen \'{0}\' 
Player2 is \'{1}\''''.format(player1, player2))
    return player1, player2