import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess the number (1-100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\n-- Menu --")
        print("1. Play Number Guessing Game")
        print("2. Exit")

        try:
            choice = int(input("Enter your choice (1-2): "))
            if choice == 1:
                play_game()
            elif choice == 2:
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

if __name__ == "__main__":
    main()
