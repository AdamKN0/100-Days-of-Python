print("Welcome to the auction")
bidders = {}
bidding_finished = False
while not bidding_finished:
	name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
	bidders[name] = bid
	more_bidders = input("Are there more bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == "no":
        bidding_finished = True
        highest_bid = max(bidders.values())
        for i in bidders:
            if bidders[i] == highest_bid:
                winner = i
        print(f"The winner is {winner} with a bid of ${highest_bid}")
    elif more_bidders not in ["yes", "no"]:
        print("Invalid input")
        break