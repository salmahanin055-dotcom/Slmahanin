import random

def play_game():
    number_to_guess = random.randint(1, 50)
    attempts = 0
    max_attempts = 7

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 50.")
    print("You have 7 tries to guess the correct number.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 50:
                print("Please guess a number between 1 and 50.")
                continue

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

while True:
    play_game()
    replay = input("Do you want to play again? (yes/no): ").strip().lower()
    if replay != 'yes':
        print("Thank you for playing! Goodbye!")
        break
