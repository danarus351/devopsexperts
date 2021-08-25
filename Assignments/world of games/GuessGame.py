def GuessGame(difficulty):
    import random
    def generate_number():
        secret_number = int(random.randint(1, difficulty))
        return secret_number

    def get_guess_from_user():
        return int(input(f'Enter number between 1 to 4:\n'))

    def compare_results(secret_number, guess):
        return secret_number == guess

    def play():
        if compare_results(generate_number(), get_guess_from_user()):
            print('congratulations !! you have won :)')
        else:
            print('You have lost, try again :(')

    play()
