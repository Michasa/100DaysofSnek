# pre-installed package that allows you to generate random variable
import random
from pathlib import Path

# for i in range(3):
#     print(random.randint(5, 50))

# harijuku_girls = ['Love 💗', 'Angel 👼', "Music 🎵", 'Baby 👶', 'Gwen']
# choice = random.choice(harijuku_girls)
# print(choice)

# Exercise
# You don't need to add paranthesis for tupples when you return them


# class Dice_Roller:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second


# dice = Dice_Roller()
# print(dice.roll())

########
# Path is a really cool standard library package that allows you to access other files
# You instaniate the object with a string you can check exists or not.
path = Path("test_file")
if path.exists():
    path.rmdir()
else:
    path.mkdir()

path2 = Path('')
for file in path2.glob('*'):
    print(file)
