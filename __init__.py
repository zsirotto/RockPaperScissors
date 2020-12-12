from random import randint


# Used to map random ints to Rock, Paper, Scissors.
rps = {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors'
}

# Rock beats scissors, paper beats rock, scissors beats paper.
priority = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}


def whoWon(computer, player):
    '''Returns winner of the game.'''
    if priority[player] == computer:
        return 'Player wins!'
    elif priority[computer] == player:
        return 'Player loses!'
    elif computer == player:
        return 'It\'s a tie!'


def playerChoice():
    '''Reads input for user's choice.'''
    i = int(input('- 1 for Rock\n- 2 for Paper\n- 3 for Scissors\n\nSelection: '))
    if i not in rps:
        print('Incorrect input. Must choose 1, 2, or 3.\n')
        return playerChoice()
    else:
        return rps[i]


def main():
    '''Runs main game loop.'''
    wins, losses, ties = 0, 0, 0
    print('Welcome to tic tac toe!\n')
    while True:
        player = playerChoice()
        cpu = rps[randint(1, 3)]
        result = whoWon(cpu, player)
        print('\nPlayer choice:', player)
        print('Computer choice:', cpu)
        print(result)
        if result == 'Player wins!':
            wins += 1
        elif result == 'Player loses!':
            losses += 1
        elif result == 'It\'s a tie!':
            ties += 1
        print(' ______________________')
        print('| Wins | Losses | Ties |')
        # uses f string mini language
        # see https://docs.python.org/2/library/string.html#formatstrings
        print('|{: ^6}|{: ^8}|{: ^6}|'.format(wins, losses, ties))
        print(' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        if input('Play again? (Y/N) ').upper() == 'N':
            break


if __name__ == '__main__':
    main()
