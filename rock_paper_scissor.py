import random
print('Wlcome to Rock-Paer-Scissors Game!')
# Function to get the user choice
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

# Function to generate the computer choice
def generate_computer_choice():
    computer_choice_number = random.randint(1, 3)
    if computer_choice_number == 1:
        return "rock"
    elif computer_choice_number == 2:
        return "paper"
    else:
        return "scissors"

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
while True:
    user_choice = get_user_choice()
    computer_choice = generate_computer_choice()
    print(f"You chose {user_choice}, and the computer chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (Press any key to start again/'q' to quit): ")
    if play_again.lower() == 'q':
        break
