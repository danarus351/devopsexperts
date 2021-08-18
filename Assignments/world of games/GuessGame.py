import random

def generate_number(difficulty):
    secrete_number = random.randint(1,difficulty)

def get_guess_from_user(difficulty):
    return input(f"Enter number between 1 to {difficulty}")