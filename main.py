import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low. Try again!")
            elif guess > number:
                print("Too high. Try again!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

def menu():
    while True:
        print("\n--- Number Guessing Game ---")
        print("1. Play Game")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()