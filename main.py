import random

print("welcome to the virtual dice flipper")
a = int(input("what's your choice: "))

flip_coin = random.randint(1, 6)

print(flip_coin)

if flip_coin == a:
    print("hurray! you won")
else:
    print("sorry you lost, better luck next time")
