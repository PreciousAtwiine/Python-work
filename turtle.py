import turtle
t=turtle.Pen()
#get screen
s=turtle.getscreen()
#Changing screen title
turtle.title("My Turtle Program")
#Changing pen size
turtle.pensize(10)
#Changing screen colour
turtle.bgcolor("blue")
#Code for square or rectangle
t.forward(180)
t.right(90)
t.forward(100)
t.right(90)
t.forward(180)
t.right(90)
t.forward(100)
#Size of turtle(strength, length, width, outlinw width)
turtle.shapesize(1,5,1)

#Changing pen colour
turtle.pencolor("red")

#Changing fill color
turtle.fillcolor("yellow")

#changing both colors in the same line(for pen, for fill)
turtle.colour("brown", "orange")











