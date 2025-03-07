#import turtle
import turtle

#function for moving the object
move=turtle.Turtle()
#move.fillcolor('orange')

def moving_object(move):
    # to fill thr color in ball
    move.fillcolor('orange')

    # start color filliing
    move.begin_fill()

    #draw circle
    move.circle(20)

    #end color filling
move.end_fill()
# driver code    
if __name__=="__main__":

    #create a screen object
    screen= turtle.Screen()

    #set screen size
    screen.setup(600,600)

    #background color
    screen.bgcolor('grey')

    #screen hides the screen
    screen.tracer(0)

    #create a turtle object object
    #move= turtle.Turtle()

    #set a turtle object color
    move.color('orange')

    #set turtle object speed
    move.speed(0)

    #set turtle object width
    move.width(2)

    #hide turtle object
    move.hideturtle()

    #Stop pen
    move.penup()

    #Set intial position
    move.goto(-250,0)

    #Move turtle object to surface
    move.pendown()

    #infinite loop

    while True:

        #Clear turtle work
        move.clear()

        #draw ball
        moving_object(move)

        # update screen(Show the screen)
        screen.update()

        #Forward motion by turtle object
        move.forward(1)
        
        
