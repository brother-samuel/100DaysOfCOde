import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards = []
computer_cards = []

for card in range(2):
    my_cards.append(random.choice(cards))
for card in range(2):
    computer_cards.append(random.choice(cards))
if sum(computer_cards) < 17:
    computer_cards.append(random.choice(cards))

#print(my_cards)
#print(computer_cards)

play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while play_blackjack == "y":
    print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    another_my_card = input("Type 'y' to get another card, type 'n' to pass")
    if another_my_card == "y":
        my_cards.append(random.choice(cards))
        print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        another_my_card = input("Type 'y' to get another card, type 'n' to pass")
    elif another_my_card == "n":
        print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        