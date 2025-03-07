import turtle
print(" Don't let a bad day make you feel like you have a bad life!!")
print('''
Have you ever had a bad day?

Of course you have. We all have.

We have all had those days where it feels like you can't do anything right.

As the day passes, your mood declines and at times it feels like the day can't get any worse, and then it does.

THE HARDEST PART OF THESE DAYS IS TRYING TO TURN YOUR DAY / MOOD AROUND.

I find that quotes always help me with this.

Maybe because it helps me realize others have felt similarily and that things can get better.

I THINK THESE QUOTES WILL HELP YOU FEEL BETTER , MORE HOPEFUL AND LESS ALONE.

  Hello and welcome to BE A WARRIOR NOT A WORRIER !!
         
         VISION
  To see people get the strength to fight all the negative energy and thoughts around them

         Let's get started!!

 ''')          

ask=input("How has your day been so far?\n")
#How has your day been
if ask  == "Good":
    print('''I'm glad to know that you have had a blast \n Don't forget to MAKE TODAY COUNT BEACUSE YESTERDAY IS GONE AND TOMORROW ISN'T GURANTEED!!

You should always keep in mind that:\n SOMETIMES BAD DAYS ARE THERE TO REMIND US THAT WE HAVE GOOD ONES TO LOOK FORWARD TO

''')

elif ask=="Not good":
    print('''Take a minute and place your hand over your heart. Feel that? \n That\'s called purpose. \n Your alive for a reason. Don\'t give up!!
          
I hope you enjoy the rest of your day!
          
Keep in mind that...\n TOUGH TIMES DON\'T LAST. TOUGH PEOPLE DO

          ''')
    
elif ask=="Very bad":
    print('''Take a deep breath. It\'s just a bad day, not a bad life

One small crack does not mean that you are broken, it means that you were put to the test and you didn\'t fall apart.

Remember to always give your best in everything you do.. That is always enough.

''')
else:
    print('''Invalid response

''')
    
# Have the quotes helped?    
yes_no = input('''Please share your thoughts...

Did these quotes help you? \n
''')
if yes_no=="Yes":
    print('''Thank you and have a great day and week ahead

See you next time!!
''')
elif yes_no=="No":
    print('''It's a pity we didn't meet your expectations

We shall try our level best to meet them next time
''')
    
else:
    print('''Invalid response
''')
    
print("Here is a small gift to brighten your day...")

#turtle object
turtle.title("GIFT")
pen=turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("grey")
def ring(col, rad):
    pen.fillcolor(col)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()

# Ears
#First ear
pen.up()
pen.setpos(-35,95)
pen.down()
ring("black",15)
pen.up()


#First ear
pen.setpos(35,95)
pen.down()
ring("black",15)
pen.up()


#Drwaing face/head
pen.setpos(0,35)
pen.down()
ring("white",40)
pen.up()
    
#Eyes
#First eye
pen.setpos(-18,75)
pen.down()
ring("black",8)
pen.up()


#Second eye
pen.setpos(18,75)
pen.down()
ring("black",8)
pen.up()


#White things in eye
#First eye

pen.setpos(-18,77)
pen.down()
ring("white",4)
pen.up()

#Second eye
pen.setpos(18,77)
pen.down()
ring("white",4)
pen.up()


#Nose
pen.setpos(0,55)
pen.down()
ring("black",5)
pen.up()


# Mouth
pen.setpos(0,55)
pen.down()
pen.right(90)
pen.circle(5,180)
pen.up()
pen.setpos(0,55)
pen.down()
pen.left(360)
pen.circle(5,-180)
pen.hideturtle()
turtle.done()

    

    
    
    
    
    
    
    
    

