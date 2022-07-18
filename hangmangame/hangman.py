import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word: #while there is a dash or space is in this word, keep choosing random words
        word = random.choice(words)

    return word #a word is return when there is no dash or space in this word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #keeps track of what has already been guessed in the word
    alphabet = set(string.ascii_uppercase) #imports predetermined lists of uppercase characters in the english dictionary
    used_letters = set() #keep track of what user has guessed

    lives = 6

    while len(word_letters)>0 and lives > 0:
        #letter used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))# ' '.join(['a','b', 'cd']) --> 'a b cd'

        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper() #getting user input
        if user_letter in alphabet - used_letters: #if the letter is not in the word
            used_letters.add(user_letter) #we add it
            if user_letter in word_letters: #if the letter is in the word
                word_letters.remove(user_letter) #we remove it

            else:
                lives = lives - 1 #takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')

    #gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')


hangman()
#user_input = input('Type Something:')
#print(user_input)
