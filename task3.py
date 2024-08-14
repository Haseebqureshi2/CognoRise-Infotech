import random

# Function to display choices and prompt the user
def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    print("Please choose one of the following: Rock, Paper, or Scissors.")
    user_choice = input("Your choice: ").strip().lower()
    while user_choice not in choices:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        user_choice = input("Your choice: ").strip().lower()
    return user_choice

# Function to randomly generate the computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to play the game
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"The computer chose: {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result.lower():
            user_score += 1
        elif "lose" in result.lower():
            computer_score += 1

        print(f"\nCurrent Scores - You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print("\nThanks for playing!")

# Call the function to start the game
play_game()
