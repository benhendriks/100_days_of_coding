from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(users_guess, actual_answer, turns):
    if users_guess > actual_answer:
        print("To high.")
        return turns - 1
    elif users_guess < actual_answer:
        print("To low")
        return turns - 1
    else:
        print(f"You got it, the answer is {actual_answer}")

def set_difficulty():
    level = input("Choose a difficulty. 'easy' or 'hard'")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thintking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} attemps remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()
