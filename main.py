import random

print("welcome to the virtual dice flipper")
a = input("what's your choice: ")

flip = random.randint(1, 6)

print(flip)

if flip == a:
    print("hurray! you won")
else:
    print("sorry you lost, better luck next time")