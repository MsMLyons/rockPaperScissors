# import library to access more features without writing more code
import random

# function - watch indentation
def get_choices():
    # create variables
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    # lists - store multiple items in a single variable  
    options = ["rock", "paper", "scissors"]
    # use random library to call random option from list
    computer_choice = random.choice(options)
    # dictionary - stores data in key/value pairs
    choices = {"player": player_choice, "computer": computer_choice}
    # what will the function return
    return choices

# add arguments so the function receives data when called
# can create new variables as arguments
def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")    
    # if statement - conditions to do specific things
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":      
            return "Rock smashes scissors! You win!"
        else: 
            return "Paper covers rock! Computer wins!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! Computer wins!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else: 
            return "Rock smashes scissors! Computer wins!"     

# error message = <function get_choices at 0x7f7cd546a3a0>
# reason = forgot parentheses after function get_choices()
# add parentheses to resolve    
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)