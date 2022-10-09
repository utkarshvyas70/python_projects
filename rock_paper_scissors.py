from random import choice
t=["Rock", "Paper", "scissors"]
user_input=input("Type your move")
computer= choice(t)
if user_input=="Rock" and computer=="Paper":
    print("You win")
elif user_input=="Rock" and computer=="Scissors":
    print("You win")
elif user_input=="Rock" and computer=="Rock":
    print("It is a draw")
elif user_input=="Paper" and computer=="Scissors":
    print("You win")
elif user_input=="Paper" and computer=="Rock":
    print("You loose")
elif user_input=="Paper" and computer=="Paper":
    print("It is a draw")
elif user_input=="Scissors" and computer=="Rock":
    print("You loose")
elif user_input=="Scissors" and computer=="Paper":
    print("You win")
elif user_input=="Scissors" and computer=="Scissors":
    print("It is a draw")
else:
    print("Invalid move")