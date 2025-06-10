import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def show_drawn_cards():
    print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

def draw_card(card_list, num_cards=1):
    for card in range(num_cards):
        card_list.append(random.choice(cards))

def show_hands():
    print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")
    if sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

def calculate_result():
    ...


play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while play_blackjack == "y":
    my_cards = []
    computer_cards = []
    draw_card(computer_cards, 2)
    draw_card(my_cards,2)
    show_drawn_cards()
    while input("Type 'y' to get another card, type 'n' to pass").lower() == "y":
        draw_card(my_cards, 1)
        show_drawn_cards()
    show_hands()
    
#        play_blackjack = "n"
        
