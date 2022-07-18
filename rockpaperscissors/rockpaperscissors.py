import random  # import random package

# defining playrockpaperscissors function
def playrockpaperscissors():  
    # getting user input for rock, r, paper, p, scissors, s.
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")  
    # declaring variable computer and making it a random choice to choose between r, p, s
    computer = random.choice(
        ["r", "p", "s"])  

    #if both the user and the computer guess the same thing, then it is a tie!
    if user == computer:
        return "Its a tie!"

    # rockpaperscissors rules: r>s, s>p, p>r
    if is_win(user, computer): #if the user beats the computer, literally specified by the if statement, then the message "You won!" will be returned
        return "You won!"
    #if the if statement above is not true, then the message "You Lost!" will be returned
    return "You Lost!"

# return true if player wins #r>s, s>p, p>r
def is_win(player, opponent):  
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True


print(playrockpaperscissors())
