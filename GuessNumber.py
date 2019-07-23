import random
number=random.randint(0,15)
print("Guess a magic number between 0 and 100 ")
guess=eval(input("Enter your guess:"))
while guess!=number:
    guess = eval(input("Enter your guess:"))
    if guess==number:
        print("Yes, the number is ",number)
    elif guess>number:
        print("Your guess is too High")
    else:
        print("Your guess is too low")
