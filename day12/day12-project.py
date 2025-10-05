

"""
Number Guessing Game - Day 12 Project
A game where the player tries to guess a random number between 1 and 100.
"""

import random


def get_difficulty():
    """Get difficulty level from user with validation."""
    while True:
        level = input("Please choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
        if level in ['easy', 'hard']:
            return level
        print("Invalid input! Please type 'easy' or 'hard'.")


def get_attempts(difficulty):
    """Return number of attempts based on difficulty level."""
    return 10 if difficulty == 'easy' else 5


def get_user_guess():
    """Get and validate user's guess."""
    while True:
        try:
            guess = int(input("Make a guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def play_game():
    """Main game logic."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("-" * 50)
    
    # Get difficulty and set attempts
    difficulty = get_difficulty()
    attempts = get_attempts(difficulty)
    
    print(f"You have {attempts} attempts remaining to guess the number.")
    print("-" * 50)
    
    # Generate random number
    number_to_guess = random.randint(1, 100)
    
    # Game loop
    while attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        guess = get_user_guess()
        
        if guess == number_to_guess:
            print(f"🎉 Congratulations! You got it! The answer was {number_to_guess}.")
            return True
        
        elif guess < number_to_guess:
            print("📈 Too low.")
        else:
            print("📉 Too high.")
        
        attempts -= 1
        
        if attempts > 0:
            print("-" * 30)
    
    # Game over
    print(f"💀 Game Over! You've run out of attempts.")
    print(f"The number was {number_to_guess}.")
    return False


def main():
    """Main function to run the game."""
    play_again = True
    
    while play_again:
        play_game()
        
        # Ask if user wants to play again
        while True:
            response = input("\nWould you like to play again? (y/n): ").lower().strip()
            if response in ['y', 'yes', 'n', 'no']:
                play_again = response in ['y', 'yes']
                break
            print("Please enter 'y' for yes or 'n' for no.")
        
        if play_again:
            print("\n" + "=" * 50)
    
    print("Thanks for playing! 👋")


if __name__ == "__main__":
    main()
