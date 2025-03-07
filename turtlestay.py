import random
import turtle
turtle.title("TURTLE STAY!")
#function to check whether turtle is in screen or not
def isInScreen(win,turt):
    #getting the end points of turtle screen
    leftBound=-win.window_width()/2
    rightBound=win.window_width()/2
    topBound=win.window_height()/2
    bottomBound=-win.window_height()/2
    #getting the current position of the turtle
    turtleX=turt.xcor()
    turtleY=turt.ycor()
    #variable to store whether in screen or not
    stillIn=True
    #condition to check whether in screen or not
    if turtleX>rightBound or turtleX<leftBound:
        stillIn=False
    if turtleY>topBound or turtleY<bottomBound:
        stillIn=False
        #returning the result
        return stillIn
#function to check whether both turtles have different positions or not
def sameposition(Red,Blue):
    if Red.pos()==Blue.pos():
        return False
    else:
        return True
#main function
def main():
    #screen initialization
    wn=turtle.Screen()
    Red=turtle.Turtle()
    Red.pencolor("red")
    Red.pensize(5)
    Red.shape("turtle")
    pos=Red.pos()
    Blue=turtle.Turtle()
    Blue.pencolor("blue")
    Blue.pensize(5)
    Blue.shape("turtle")
    Blue.hideturtle()
    Blue.penup()
    #move turtles apart
    Blue.goto(pos[0]+50,pos[1]
    #Blue.showturtle()
    Blue.pendown()
    #variables to prove turtles are in screen or not
    mT=True
    jT=False
    #loop for the game
    while mT and jT and sameposition(Red,Blue):
        #coin flip for red
        coinRed=random.randrange(0,2)
        angleRed=90
        #condition for left or right based on coin
        if coinRed==0
            Red.left(angleRed)
        else:
            Red.right(angleRed)
        #coin flip for blue
        coinBlue=random.randrange(0,2)
        angleBlue=90
        #condition for left or right based on coin
        if coinBlue==0
            Blue.left(angleBlue)
        else:
            Blue.right(angleBlue)
        #draw for red
        Red.forward(50)
        #draw for blue
        Blue.forward(50)
        #checking whether turtles are on screen or not
        mT=isInScreen(wn,Blue)
        jT=isInScreen(wn,Red)
    #set pencolor for turtles
    Red.pencolor("black")
    Blue.pencolor("black")
    #condition check for draw or win
    if jT==True and mT==False:
        Red.write("RED WON!",True,align="center",font=("arial",15,"bold"))
    elif mT==True and jT==False:
        Blue.write("BLUE WON!",True,align="center",font("arial",15,"bold"))
    else:
        Red.write("DRAW", True,align="center",font=("arial",15,"bold"))
        Blue.write("DRAW",False,align="center",font=("arial",15,"bold"))
    #exit on close
    wn.exitonclick()
#calling main function
main()
