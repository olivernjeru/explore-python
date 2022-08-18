import random #importing the random package

#Computer where the user guesses the number hidden by the computer

def guess(x): #defining a function
    random_number = random.randint(1, x) #declaring the random number
    guess = 0 #declaring the variable guess
    while guess != random_number: #while loop used to enter the number to get the right guess
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again buddy, too low!")
        elif guess > random_number:
            print("Sorry, guess again buddy, too high!")

    print(f"Yaaaaaay,congrats. You have guessed the number {random_number} correctly!") #displaying the congratulatory message and the guessed random number


guess(20) #calling and running the function 20 times
