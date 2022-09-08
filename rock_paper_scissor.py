# Single player and Computer:

import random

while True:
    player = input("Choose one ('rock','paper','scissors'):")
    pick = ['rock', 'paper', 'scissors']
    computer = random.choice(pick)

    print(f'You chose {player} and computer chose {computer}')

    if player == computer:
        print(f"Both players selected {player}, It's a Tie!")

    elif player == 'rock':
        if computer == 'scissors':
            print('Rock smashes Scissors!, You Win.')
        else:
            print('Paper covers Rock!, You Lose.')

    elif player == 'paper':
        if computer == 'rock':
            print('Paper covers Rock!, You Win.')
        else:
            print('Scissors cuts Paper!, You Lose.')

    elif player == 'scissors':
        if computer == 'paper':
            print('Scissor cuts Paper!, You Win.')
        else:
            print('Rock smashes Scissors!, You Lose.')

    option = input('You wanna play again? [Y|N]:')
    print()
    if option.lower() != 'y':
        break
