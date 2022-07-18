import random #importing the random package

# User where the user has a random number and lets the computer guess it until the computer finds the number

def computer_guess(x): #defining the guess function
    low = 1 #defining the low variable to be 1
    high = x #defining the high variable to be x
    feedback = '' #defining the feedback variable and setting it to be nothing for now
    while feedback != 'c': #while loop used to enter whether it is high, low until the computer gets the right guess and then the user enters correct
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high because low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct(C) ?? '.lower()) #making the feedback input to be lowercase so that it can match the if statement below values
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay, the computer guessed your number {guess} correctly!") #displaying the message that the computer guessed the random number


computer_guess(10) #calling and running the function
