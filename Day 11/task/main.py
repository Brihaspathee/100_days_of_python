import random

from art import logo

print(logo)

def deal_card() -> int:
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards) -> int:
    """
    Calculate the score of a given set of cards.

    This function computes the score for a hand of cards in a card game.
    If the total of the cards equals 21 with exactly two cards in hand, the
    function returns 0, indicating a 'Blackjack'. Additionally, if there
    is an Ace (valued as 11) in the hand while the total score exceeds 21,
    the Ace is adjusted to a value of 1 to prevent a bust. The function
    then returns the final sum of the cards in hand.

    :param cards: A list of integers representing the values of the cards in hand.
    :type cards: list[int]
    :return: The calculated score for the given hand of cards.
    :rtype: int
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            print("You went over. You lose 😤")
            is_game_over = True
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_choice == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

continue_playing = input("Do you want to play a game of blackjack? Type 'y' or 'n':")
while continue_playing == "y":
    print("\n" * 20)
    print(logo)
    play_game()
    continue_playing = input("Do you want to play a again? Type 'y' or 'n':")