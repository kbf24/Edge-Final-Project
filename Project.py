
import random

player_name = input("What's Your name?")
print("Best of luck!!! " + player_name)

fridge_list = ['milk', 'cheese', 'yoghurt', 'egg', 'olives', 'mayonise', 'sauces', 'vegetables', 'fruits', 'water', 'pepsi', 'juice', 'leftovers']


lists = random.choice(fridge_list)
print("Guess the letters!!")

guesses = ''
chances = 4

while chances > 0:
    failed = 0

for lis in lists:
    if lis in guesses:
        print(lis)
    else:
        print("...")
        failed += 1
    if failed == 0:
        print("You Win!!")
        print("The word is: " + lists)
        break

guess = input("guess a letter:")
guesses += guess

if guess not in lists:
    chances -= 1
    print("Incorrect")
    print("YOU HAVE" + chances, 'LEFT!')

    if chances == 0:
        print("YOU LOOSE :(")




