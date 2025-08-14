# Choosing a random number between 1 and 100.
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Track the number of turns and reduce by 1 if they get it wrong.
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return -1

# Function to set difficulty
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Let the user guess a number 10 times.
def guess_number(difficulty, answer):
    from art import logo
    print(logo)
    while difficulty > 0:
        guess = int(input("Make a guess: "))
        remaining_turns = check_answer(guess, answer, difficulty)
        if remaining_turns == -1:
            return
        elif remaining_turns > 0:
            difficulty = remaining_turns
            print(f"You have {remaining_turns} attempts remaining to guess the number.")
        else:
            print("You've run out of guesses, you lose.")
            return

answer = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess the number.")
guess_number(turns, answer)





