# --------------------------------
# CodingGears.io
# --------------------------------
# random Module
# This module implements pseudo-random number generators for various distributions.

import random

# TODO: Random
print(random.random())


# TODO: Random Range
choice = random.randrange(2)  # 0, 1
print(choice)

choice = random.randrange(0, 100, 5)
print(choice)

# TODO: Random Choice (one)
options = ["Olive Garden", "Pizza Hut", "Double Dave's", "Taj Mahal"]
print(random.choice(options))

# TODO: Random number in a range
rand1 = random.randint(50, 200)
print(rand1)

# TODO: Range
dice_choice = random.randrange(1, 7)
print("You have rolled : " + str(dice_choice) + "!")

# TODO: Random Sample
winners = random.sample(range(200), 10)
print(winners)

# TODO: Cards
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
color = ["Spade", "Diamond", "Hearts", "Clubs"]

card_pick = random.choice(cards)
color_pick = random.choice(color)
print(str(card_pick), str(color_pick))

# TODO: Shuffle
print(cards)
random.shuffle(cards)
print(cards)
