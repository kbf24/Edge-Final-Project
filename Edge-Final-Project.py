import random

print("Welcome to Guess The Word Game")
player_name = input("What's your name? ")

print("Best of luck!! " + player_name)
print('\n')
print("Let me give you a hint before you start " + player_name + ", the hint is things you'd find in the FRIDGE..")
print('\n')
print("You have 6 guesses in total")

fridge_list = ('milk', 'cheese', 'yoghurt', 'egg', 'olives', 'mayonise', 'sauces', 'vegetables', 'fruits', 'water', 'pepsi', 'juice', 'leftovers')

word = random.choice(fridge_list)
print("Guess the word!")

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
        print("You have", + chance, 'more guesses left')
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

