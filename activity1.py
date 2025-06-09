import random
number=random.randint(0,20)
print("I will generate a number between 0 to 20 and you have to guess it")
print("You have to guess the answer!")
while True:
    guess=int(input("enter your number"))
    if number==guess:
        print("you win the game!")
        print("the number was",number)
        break
    else:
        print("sorry! wrong guess! try again!")
        