import random

player_choice = input("Enter your choice from (rock, paper, scissors): ")
option = ["rock", "paper", "scissors"]
computer_choice = random.choice(option) #here it takes the random choice from option

def result_fun(player_choice,option):
    if player_choice == computer_choice:
        return f"It's a Tie, Both players selected {player_choice}."
    elif player_choice == "rock":
        if computer_choice == "scissors":
            return "You Win, Rock smashes scissors."
        else:
            return "You Lose, Paper covers rock."
    elif player_choice == "paper":
        if computer_choice == "rock":
            return "You Win, Paper covers rock."
        else:
            return "You Lose, Scissors cuts paper."
    elif player_choice == "scissors":
        if computer_choice == "paper":
            return "You Win, Scissors cuts paper."
        else:
            return "You Lose, Rock smashes scissors."

if player_choice in option:
    print(f"You chose {player_choice}, computer chose {computer_choice}.")
    result = result_fun(player_choice,option)
    print(result)
        
else:
    print("You entered a wrong value, please enter a correct value")
    player_choice = input("Enter your choice from (rock, paper, scissors): ")
    print(f"You chose {player_choice}, computer chose {computer_choice}.")
    result = result_fun(player_choice,option)
    print(result)
        
        
        
        
    
