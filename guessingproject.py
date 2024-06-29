def result_fun(secret):
    attempts = 0
    while True:
        player_guess = input("Enter your guess: ")
        attempts += 1
        if player_guess == secret:
            print(f"Correct, You guessed the number in {attempts} attempts.")
            break
        else:
            set_guess = set(str(player_guess)) #converting player into set
            set_secret = set(str(secret)) #converting secret value into set
            if set_guess & set_secret: #intersection between guess and secret to find the number of correct values
                print("Hint: 1 correct")
            else:
                print("Hint: 0 correct")
    return attempts 

print("Player 1, set a multi-digit number for Player 2 to guess.")
player1_secret = input("Enter the number: ")
print("Player 2, try to guess the number set by Player 1.")
player1_result = result_fun(player1_secret)
   
print("Now, it's Player 2's turn to set a number for Player 1.")
player2_secret = input("Enter the number: ")
print("Player 1, try to guess the number set by Player 2.")
player2_result = result_fun(player2_secret)


if player1_result < player2_result:
    print("Player 2 wins and is crowned Mastermind.")
elif player1_result > player2_result:
    print("Player 1 wins and is crowned Mastermind.")
else:
    print("It's a tie, Both players are Masterminds.")
