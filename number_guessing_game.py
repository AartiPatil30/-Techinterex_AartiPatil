import random

def play_game():
    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    # Step 2: Generate a Random Number
    target_number = random.randint(1, 100)

    # Step 6: Counter for number of attempts
    attempts = 0

    while True:
        try:
            # Step 3: Take Player Input
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Step 4: Compare Player Guess
            if guess < target_number:
                print("📉 Too low, try again!")
            elif guess > target_number:
                print("📈 Too high, try again!")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break  # Step 5: End loop if guessed
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

def main():
    while True:
        play_game()
        
        # Step 7: Play Again Option
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("🙏 Thanks for playing! Goodbye.")
            break

# Entry Point
if __name__ == "__main__":
    main()
