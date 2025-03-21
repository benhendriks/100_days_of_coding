import random 
import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(users_guess, actuel_answer):
    if user_guess > actual_answer:
        print("To high.")
    elif user_guess < actual_answer:
        print("To low")
    else:
        print(f"You got it, the answer is {actual_answer}")

def set_difficulty():
    level = int(input("Choose a difficulty. 'easy' or 'hard'"))
    if level == easy:
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



    

print("WElcome to the Number Guessing Game!")
print("I'm thintking of a number between 1 and 100.")
answer = randint(1, 100)


guess = int(input("Make a hguess"))
turns = set_difficulty()
print(f"You have {turns} attemps remaining to guess the number.")


