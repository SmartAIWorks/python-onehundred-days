"""
Higher Lower Game - Day 14 Project
A game where players guess which social media account has more followers.
"""

from random import choice
from game_data import data


def get_random_account(exclude_index=None):
    """Get a random account from the data, optionally excluding a specific index."""
    available_indices = [i for i in range(len(data)) if i != exclude_index]
    random_index = choice(available_indices)
    return data[random_index], random_index


def format_account_info(account, label):
    """Format account information for display."""
    return f"{label}: {account['name']}, a {account['description']}, from {account['country']}"


def get_user_choice():
    """Get and validate user's choice with proper error handling."""
    while True:
        choice = input("\nWho has more followers? Type 'A' or 'B': ").upper().strip()
        if choice in ['A', 'B']:
            return choice
        print("❌ Invalid input! Please type 'A' or 'B' only.")


def check_answer(account_a, account_b, user_choice):
    """Check if the user's answer is correct."""
    follower_a = account_a['follower_count']
    follower_b = account_b['follower_count']
    
    if follower_a > follower_b:
        correct_answer = 'A'
    else:
        correct_answer = 'B'
    
    return user_choice == correct_answer, correct_answer


def display_comparison(account_a, account_b):
    """Display the comparison between two accounts."""
    print("\n" + "=" * 60)
    print(format_account_info(account_a, "Compare A"))
    print("\n" + " " * 20 + "VS" + " " * 20)
    print(format_account_info(account_b, "Compare B"))
    print("=" * 60)


def display_result(is_correct, account_a, account_b, correct_answer):
    """Display the result of the comparison."""
    follower_a = account_a['follower_count']
    follower_b = account_b['follower_count']
    
    print(f"\n📊 Results:")
    print(f"   {account_a['name']}: {follower_a:,} followers")
    print(f"   {account_b['name']}: {follower_b:,} followers")
    
    if is_correct:
        print("🎉 Correct! You got it right!")
    else:
        print(f"❌ Wrong! The correct answer was '{correct_answer}'")


def play_game():
    """Main game logic."""
    score = 0
    game_over = False
    
    print("🎮 Welcome to the Higher Lower Game!")
    print("📱 Guess which social media account has more followers!")
    print("-" * 60)
    
    # Get first account
    current_account, current_index = get_random_account()
    
    while not game_over:
        # Get next account to compare
        next_account, next_index = get_random_account(current_index)
        
        # Display comparison
        display_comparison(current_account, next_account)
        
        # Get user's guess
        user_choice = get_user_choice()
        
        # Check answer
        is_correct, correct_answer = check_answer(current_account, next_account, user_choice)
        
        # Display result
        display_result(is_correct, current_account, next_account, correct_answer)
        
        if is_correct:
            score += 1
            print(f"🏆 Current Score: {score}")
            # Move to next comparison
            current_account = next_account
            current_index = next_index
        else:
            game_over = True
    
    # Game over
    print(f"\n💀 Game Over!")
    print(f"🎯 Final Score: {score}")
    
    if score == 0:
        print("😅 Better luck next time!")
    elif score < 5:
        print("👍 Not bad! Keep practicing!")
    elif score < 10:
        print("🔥 Great job! You're getting good at this!")
    else:
        print("🏆 Amazing! You're a social media expert!")


def main():
    """Main function to run the game."""
    play_again = True
    
    while play_again:
        play_game()
        
        # Ask if user wants to play again
        while True:
            response = input("\n🔄 Would you like to play again? (y/n): ").lower().strip()
            if response in ['y', 'yes', 'n', 'no']:
                play_again = response in ['y', 'yes']
                break
            print("Please enter 'y' for yes or 'n' for no.")
        
        if play_again:
            print("\n" + "=" * 60)
    
    print("👋 Thanks for playing Higher Lower!")


if __name__ == "__main__":
    main()