def welcome(name):
    return f'\n' \
           f'Hello {name} and welcome to the World of Games (WoG).\n' \
           f'Here you can find many cool games to play.\n'


def load_game():
    game = int(input(
        'Please choose a game to play:\n'
        '   1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n'
        '   2. Guess Game - guess a number and see if you chose like the computer\n'
        '   3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n'
        'please enter the game number(1-3):'))

    if game < 1 or game > 3:
        return print('no game was  choosen')

    diff = int(input('Please choose game difficulty from 1 to 5:'))
    if diff < 1 or diff > 5:
        return print('no difficulty was  choosen')
    print(f"You have chosen to play with {game} with difficulty level {diff}")
    return game, diff
