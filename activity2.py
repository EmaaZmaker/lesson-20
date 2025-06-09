import random
while True:
    user=input("enter a choice between rock,paper and scissor")
    possible_actions=["rock","paper","scissor"]
    computer_input=random.choice(possible_actions)
    print(f"you have chosen {user} and the computer has chosen{computer_input}")
    if user==computer_input:
        print("Tie!")
    elif user=="rock":
        if computer_input=="paper":
            print("you lost!")
        else:
            print("you win")
    elif user=="paper":
        if computer_input=="scissor":
            print("you lost!")
        else:
            print("you win")
    elif user=="scissor":
        if computer_input=="rock":
            print("you lost!")
        else:
            print("you win")

    