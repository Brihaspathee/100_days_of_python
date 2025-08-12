# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


from art import logo

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

print(logo)
print("Welcome to the secret auction program.")
is_more_bidders = True
bidding_record = {}
while is_more_bidders:
    bidder_name: str = input("Enter your name: ")
    user_bid:int = int(input("Enter your bid: "))
    bidding_record[bidder_name] = user_bid
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        is_more_bidders = False
        find_highest_bidder(bidding_record)
    elif should_continue == "yes":
        print("\n" * 20)
        print(bidding_record)

