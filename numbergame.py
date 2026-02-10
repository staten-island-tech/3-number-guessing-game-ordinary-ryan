import random

guess_history = []
random_int = random.randint(1,10)
guess = int(input("state a number from 1-10"))

while random_int != guess:
    guess_history.append(guess)
    if guess > random_int:
        print(guess_history)
        print("guess is too big")
        guess = int(input("state another number"))
    if guess < random_int:
        print(guess_history)
        print("guess is too small")
        guess = int(input("state another number"))
else:
    print(guess_history)
    print("correct")
