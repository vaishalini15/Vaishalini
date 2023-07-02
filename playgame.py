import art
from game_data import data
import random

print(art.logo)
is_continue = True
score = 0
account_b = random.choice(data)

# data - random
while is_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    # structure
    def gamedata(account):
        """To return the random choices of name, designation, country of A and B"""
        account_name = account["name"]
        account_description = account["description"]
        account_country = account["country"]
        return f"{account_name}, {account_description}, from {account_country}"


    def calculate(user_guess, a_followers, b_followers):
        """To find that user guess is correct or not"""
        if a_followers > b_followers:
            # returns true if user_guess matches the condition else false
            return user_guess == "A"
        else:
            # returns true if user_guess matches the condition else false
            return user_guess == "B"


    print(f"Compare A: {gamedata(account_a)}")
    print(art.vs)
    print(f"Compare B: {gamedata(account_b)}")

    user_guess = input("Who has more followers? A or B: ").upper()
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_correct = calculate(user_guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You're Right! Your Score is: {score}")
    else:
        print(f"Better guesses next time! Your Score is: {score}")
        is_continue = False