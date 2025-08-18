# Display art
from art import logo, vs

# Import the game data
from game_data import data

# Import the random function
import random

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

# Set the score to 0
score = 0

# Set the game to active
is_game_active = True

# Generate a random account from the game data
account_a = random.choice(data)
while is_game_active:
    account_b = random.choice(data)
    print(logo)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B':").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    if check_answer(guess, a_follower_count, b_follower_count):
        score += 1
        print(f"You're right! Current score: {score}.")
        account_a = account_b
    else:
        is_game_active = False
        print(f"Sorry, that's wrong. Final score: {score}.")
