import gallows
import words
import getpass
import random

mistakes = 0
win_score = 0
word = ""
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
    letter = input("\nenter a letter: ")
    if letter in word:
        win_score -= 1
        index = word.index(letter)
        guessing[index] = f" {letter} "
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