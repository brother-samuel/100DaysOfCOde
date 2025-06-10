import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def show_drawn_cards():
    print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

def draw_card(card_list, num_cards=1):
    for card in range(num_cards):
        card_list.append(random.choice(cards))

def check_computer_score():
    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))

def show_hands():
    print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")
    check_computer_score()
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

def calculate_result():
    my_score = sum(my_cards)
    computer_score = sum(computer_cards)
    if my_score == 21:
        print("Blackjack! You win :)")
    elif computer_score == 21:
        print("Opponent got Blackjack! Opponent wins :(")
    elif my_score == 21 and computer_score == 21:
        print("Both got Blackjack! Draw!")
    elif my_score > 21 and computer_score > 21:
        print("Both went over. Draw!")
    elif computer_score > 21:
        print("Opponent went over. You win :)")
    elif my_score > 21:
        print("You went over. Opponent wins :(")
    elif my_score > computer_score:
        print("You win!")
    elif my_score == computer_score:
        print("Draw!")
    elif computer_score > my_score:
        print("Opponent wins :(")


play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while play_blackjack == "y":
    my_cards = []
    computer_cards = []
    draw_card(computer_cards, 2)
    draw_card(my_cards,2)
    show_drawn_cards()
    while input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
        draw_card(my_cards, 1)
        show_drawn_cards()
    show_hands()
    calculate_result()

    play_blackjack = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()  
    if play_blackjack == "n":
        print("Thanks for playing!")
    else:
        print("\n" * 40)
    
