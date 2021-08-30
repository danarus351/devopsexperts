from Live import welcome, load_game

print(welcome('Guy'))
game = load_game()
if game[0] == 1:
    import MemoryGame

    MemoryGame.Memory_Game(game[1])
elif game[0] == 2:
    import GuessGame

    GuessGame.GuessGame(game[1])
elif game[0] == 3:
    import CurrencyRouletteGame

    CurrencyRouletteGame.currency_roulette_game(game[1])
else:
    print('goodbye')
