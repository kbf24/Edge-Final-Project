# Guess The Word
# Khadija Al-Majid
# 23 July 2020

import random

class Game:
    def __init__(self):
        clue = word[0] + word[(len(word)-1):(len(word))]

        guesses = ''
        chance = 6
        tries = 0

        while chance > 0:
            failed = 0
            for char in word:
                if char in guesses:
                    print(char, end=" ")

                else:
                    print("_", end=" ")
                    failed += 1

            if failed == 0:
                print("\nYOU WIN :)")
                print("The word is: " + word)
                break

            guess = input("Guess a letter!:")
            guesses += guess
            if guess not in word:
                chance -= 1
                print("\nIncorrect")
                print("\nYou have", + chance, 'more guesses left')
                tries = tries + 1
                if tries == 3:
                    clue_request = input('Would you like a clue?')
                    if clue_request == 'yes':
                        print('\n')
                        print('CLUE: The first and last letter of the word is: ', clue)
                    if clue_request == 'no':
                        print('You are a genius!')
                if chance == 0:
                    print("You LOOSE :(")
                    print("The word is: " + word)
                    print("Better luck next time")

print("** Welcome to Guess The Word Game **")

fridge_list = ('milk', 'cheese', 'yoghurt', 'egg', 'olives', 'pickles', 'sauces', 'vegetables', 'fruits', 'water', 'pepsi', 'juice', 'leftovers', 'sprite')

word = random.choice(fridge_list)

player_name = input("What's your name?\n")

print("\nBest of luck!! " + player_name)
print('\n')
print(f"Let me give you a hint before you start {player_name}, the hint is items in the fridge..")
print('\n')
print("You have 6 guesses in total")
print('\n')

game = Game()
