import turtle
answer=input("Would you like me to draw an emoji for you? Type \'yes or \'no' \n")
if answer =="yes":
    #screen=turtle.getscreen()
    turtle.bgcolor("yellow")
    turtle=turtle.Turtle()
    
    #pen size
    turtle.pensize(10)
    #pen color
    turtle.pencolor("brown")
    
    #Face
    turtle.fillcolor("brown")
    turtle.penup()
    turtle.goto(0,-200)
    turtle.pendown()
    turtle.circle(200)
    turtle.penup()

    #Eyes

    #First eye
    turtle.goto(-100,50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.penup()

    #Second eye
    turtle.goto(100,50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()


    #Nose
    turtle.penup()
    turtle.goto(0,50)
    turtle.pendown()
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.circle(-70,steps=3)
    turtle.end_fill()

    #Smile
    turtle.penup()
    turtle.goto(-100,-70)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(100,180)

elif answer=="no":
    print("Okay")

else:
    print("Invalid Reply")


