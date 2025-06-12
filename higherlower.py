import random
from game_data import data

def pick_next_account(account_a):
    account_B = random.choice(data)
    while account_B == account_a:
        account_B = random.choice(data)
    return account_B

def make_choice(account_a, account_b):
    choice = input("Who has more followers? Type 'A' or 'B':  ").upper()
    a_followers = int(data[account_a]['follower_count'])
    b_followers = int(data[account_b]['follower_count'])
    return ((choice == "A" and a_followers >= b_followers) or
            (choice == "B" and b_followers >= a_followers))


def main():
    playing = True
    account_a = random.choice(data)
    score = 0
    #current choice (A)
    while playing:
        print(f"Compare A: {data[account_a]['name']}, {data[account_a]['description']} from {data[account_a]['country']}")
        print("vs.")
        #pick next choice (B)
        account_b = pick_next_account(account_a)
        print(f"Against B: {data[account_b]['name']}, {data[account_b]['description']} from {data[account_b]['country']}")
        if make_choice(account_a,account_b):
            score += 1
            account_a = account_b
            print(f"You're right! Current score: {score}.")
        else:
            playing = False
            print(f"Sorry, that's wrong. Final score: {score}.")

if __name__ == "__main__":
    main()