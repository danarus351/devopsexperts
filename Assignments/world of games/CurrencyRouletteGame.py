def currency_roulette_game(difficulty: int):
    from currency_converter import CurrencyConverter
    def get_money_interval():
        c = CurrencyConverter()
        total = c.convert(1, 'USD', 'ILS')
        total = float(format(total, '.2f'))
        interval = ((total - (5 - difficulty)), (total + (5 - difficulty)))
        return interval

    def get_guess_from_user():
        return float(input('enter a guess of value to a given amount of USD:\n'))

    def play():
        inter = tuple(get_money_interval())
        if (inter[0] <= get_guess_from_user() <= inter[1]):
            print('congratulations !! you have won :)')
        else:
            print('You have lost, try again :(')

    play()