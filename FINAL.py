import random

print("Welcome to Guess The Word Game")
player_name = input("What's your name? ")

print("Best of luck!! " + player_name)
print("Let me give you a hint before you start " + player_name + ", the hint is things you'd find in the FRIDGE..")

fridge_list = ('milk', 'cheese', 'yoghurt', 'egg', 'olives', 'mayonise', 'sauces', 'vegetables', 'fruits', 'water', 'pepsi', 'juice', 'leftovers')

word = random.choice(fridge_list)
print("Guess the letters!")

guesses = '..'
chance = 5
while chance > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("YOU WIN :)")
        print("The word is: " + word)
        break

    guess = input("guess a letter!:")
    guesses += guess
    if guess not in word:
        chance -= 1
        print("Incorrect")
        print("You have", + chance, 'more guesses left')
        if chance == 0:
            print("You LOOSE :(")
            print("The word is: " + word)
            print("Better luck next time")

