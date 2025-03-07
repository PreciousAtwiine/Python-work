import random
from random import randint
#List of play options
t=["Rock", "Paper", "Scissors"]

#Random play to the computer
comput=t[randint(0,2)]

#Set player to false
player=False

while player== False:
    player=input("Rock, Paper, Scissors?\n")
    if player== comput:
        print ("Tie!")
    elif player== "Rock":
        if comput== "Paper":
            print("You lose !", comput, "covers", player)
        else:
             print("You win !", player, "smashes", comput)
    elif player=="Paper":
        if comput=="Scissors":
             print("You lose!", comput, "cut", player)
        else:
             print("You win", player, "covers", comput)
             
    elif player=="Scissors":
        if comput== "Rock":
             print("You lose...", comput, "smashes", player)
             
        else:
             print("That's not a valid play. Check your spelling!")

             #Player was set to true, but we want it to be false so the loop continues
             player= False # it resets the player so that the while loop begins again
             comput= t[randint(0,2)]

             #Randint is random integer
             #Comput is the computer or python playing
             
