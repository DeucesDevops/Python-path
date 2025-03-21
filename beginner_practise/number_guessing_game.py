import random

def number_guessing_game():
    guess = 0
    min_number = 1
    max_number = 100
    attempts = 0
    game_running = True

    random_number = random.randint(min_number, max_number)

    print("Welcome to Guess the Number!")
    print(f"Guess a number between {min_number} and {max_number}.")

    while game_running:
        guess = input("Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)
            attempts += 1

            if guess < min_number or guess > max_number:
                print(f"Please enter a number between {min_number} and {max_number}.")
            elif guess < random_number:
                print("Too Low!, Try again.")
            elif guess > random_number:
                print("Too High!, Try again.")
            else:
                print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
                game_running = False

        else:
            print(f"Invalid input. Please enter a number between {min_number} and {max_number}.")







