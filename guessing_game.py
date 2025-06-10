import random

number = random.randint(1, 101)
attempts = 0
def make_guess(number, attempts):
    while attempts > 0:
        guess = int(input("Make a guess:  "))
        if guess != number:
            attempts -= 1
            if attempts > 0:
                direction = "Too high" if guess > number else "Too low"
                print(f"{direction}.\nGuess again. \n"
                    f"You have {attempts} attempts remaining to guess the number.  ")
        elif guess == number:
            print(f"You have won! The answer was {number}")
            return
    print("You have run out of guesses. Refresh the page to run again.")

def main():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    #print(number)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    print(f"You have {attempts} attempts to guess the number")
    make_guess(number, attempts)

if __name__ == "__main__":
    main()