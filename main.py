import gallows
import words
import getpass
import random
from art import *

mistakes = 0
win_score = 0
word = ""

tprint("Hangman")

command = input("type 'y' if you want the computer to pick a random word, and 'n' if you want a real player to write the word: ")
if command == "y":
    word = words.words['data'][random.randint(0, len(words.words["data"])-1)]
elif command == "n":
    word = getpass.getpass("Player2 must write a secret word: ")


guessing = [' _ '] * len(word)
win_score = len(word)

def show_gallow(i):
    print(gallows.gallows[i])
    show_guessing(guessing)


def show_guessing(guessing):
    print("word:  ", end="")
    for l in guessing:
        print(l, end="")


show_gallow(mistakes)

while True:
    while True:
        letter = input("\nenter a letter: ")
        if len(letter) == 1:
            break
        else:
            print("It's gotta be just one letter")
        
    if letter in word:
        index = word.index(letter)
        cur_multiple_letter_index = 0
        if guessing[index] == " _ ":
            win_score -= 1
            guessing[index] = f" {letter} "
        else:
            indexes_of_all_duplicates_of_this_letter = []
            for i in range(len(word)):
                if(word[i] == letter):
                    indexes_of_all_duplicates_of_this_letter.append(i)
            
            while True:
                if guessing[indexes_of_all_duplicates_of_this_letter[cur_multiple_letter_index]] == " _ ":
                    guessing[indexes_of_all_duplicates_of_this_letter[cur_multiple_letter_index]] = f" {letter} "
                    win_score -= 1
                    break
                else:
                    if cur_multiple_letter_index == (len(indexes_of_all_duplicates_of_this_letter)-1):
                        break
                    cur_multiple_letter_index += 1

        show_gallow(mistakes)
    else:
        mistakes += 1
        show_gallow(mistakes)

    if win_score == 0:
        print("\nYOu won, bitch")
        break
    if mistakes == 6:
        print("\nYou lost, motherfuckr")
        print(f"The word was: {word}")
        break