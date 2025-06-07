auction = {}
bidding = True

while bidding == True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction[name] = bid

    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if continue_bidding == "no":
        bidding = False
    elif continue_bidding == "yes":
        print("\n" * 40)

highest_bid = 0
winner = ""

for name in auction:
    if auction[name] > highest_bid:
        highest_bid = auction[name]
        winner = name
print(f"The winner is {winner} with a bid of ${highest_bid}")
