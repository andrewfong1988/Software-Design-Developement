# Made by AFO
# 16/02/2022

import random
import time
import sys
import enchant


def import_words(FILE): # imports words from text file and adds them to array
    with open(FILE) as f:
        lines = f.readlines()
    return lines

def word_selection(WORD_LIST): # this chooses a random number between 1 and the length of the word list
    rand = random.randint(0, len(WORD_LIST)-1)
    return(WORD_LIST[rand])

def display_word(WORD):
    print(WORD)

def player_guess(WORD, ENGLISH_DICTIONARY):
    guess = input("Please enter your guess: ")
    if ENGLISH_DICTIONARY.check(guess) == True:
        global guess_count
        guess_count += 1
        guess_checker(WORD, guess)
    else:
        print("Please enter a word that appears in the English Dictionary")
        player_guess(WORD,ENGLISH_DICTIONARY)

def guess_checker(WORD,guess):
    global win
    global guess_count
    reviewed_word = ""

    if guess == WORD:
        print("You got it buddy")
        win = True
    else:
        if guess_count == 6:
            print("You have had too many guesses")
            pass 
        else:
            print("You have ", 6-guess_count, " guesses remaining")
            
            counter = 0
            correct_check = [False,False,False,False,False]
            incorrect_position_check = [False, False, False, False, False]
            
            for letter in guess:
            
                if guess[counter] == WORD[counter]:  #deal with whether the letters are CORRECT/in the right place
                    reviewed_word = reviewed_word + guess[counter]
                    correct_check[counter] = True
                elif guess[counter] in WORD: #deal with whether the letters are in the INCORRECT place
                    reviewed_word = reviewed_word +  guess[counter]
                    incorrect_position_check[counter] = True
                else:
                    reviewed_word = reviewed_word +  "_" #deal with incorrect values 
                counter+=1
            

            colour_counter = 0 
            print(correct_check)
            print(incorrect_position_check)   
            for letter in WORD:
                if correct_check[colour_counter] == True:
                    sys.stdout.write(COLOUR_CORRECT + reviewed_word[colour_counter]) #print green
                elif incorrect_position_check[colour_counter] == True:
                    sys.stdout.write(COLOUR_INCORRECT_POSITION + reviewed_word[colour_counter]) #print orange
                else:    
                    sys.stdout.write(COLOUR_UNDERSCORE + reviewed_word[colour_counter]) #print white underscore
                colour_counter+=1
                sys.stdout.flush()
                time.sleep(0.25)

# Game Loop
guess_count = 0 #at the start of the game, the guess count starts at 0
win = False # flag
ENGLISH_DICTIONARY = enchant.Dict("en_AU")
FILE = "C:/Users/fong.a/OneDrive - St Augustines College/Desktop/Wordle/words.txt" 
COLOUR_CORRECT = '\33[32m'
COLOUR_UNDERSCORE = '\33[37m'
COLOUR_INCORRECT_POSITION = '\33[33m'
WORD_LIST = import_words(FILE)
WORD = word_selection(WORD_LIST)
WORD = WORD[0:5]
print(WORD)


while guess_count <6 and win == False:
    print("\n")
    player_guess(WORD, ENGLISH_DICTIONARY)

    
    # display current status of word - e.g. _ _ _ _ _ / _ _ A _ _ 
    # allow the user to take a guess


