from game_data import data
import random

def format_data(account):
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']

    return f'{account_name}, a {account_desc}, from, {account_country}'

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

score = 0
game_player = True
account_b = random.choice(data)
account_a = random.choice(data)

while game_player:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)


    print(f'Compare A: {format_data(account_a)}.')

    print(f'Compare B: {format_data(account_b)}.')

    guess = input("Who has more follower? Type 'A' or 'B': ").lower()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1 
        print(f'You are right! Your current Score is {score}')
    else:
        score -=1
        print(f'Sorry, that is wrong! Your final score is {score}')
        game_player = False
