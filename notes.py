print("Hello there !!")
#What is your name?
Name=input("What is your name?")

Age=input("How old you?")

School=input("Which school do you go to?")

Class=input("Which class are you in?")

Home=input("Where do you stay?")

print("Thank you for the information",Name,Age,School,Class,Home)

#More variables
Int=-4

Str="house"

Flo=4.7

print("This is an integer,",Int)

print("This is a string,",Str)

print("This is a float,",Flo)

print(type(Int))#Data types

print(type(Str))#data types

print(type(Flo))#data types

#Rules of variables
Precious_Atwiine="girl"

print("This is a,",Precious_Atwiine)

#many values to multiple variables
x,y,z="oranges","bananas","apples"
print(x)

print(y)

print(z)

#operators
x="awesome"

y=" and nice"

z=x + y

print("Python is " + z)

#variables of two integers
a=3

b=5

c=a + b

print(c)

#GLOBAL VARIABLES:Are variables created outside a function.

#local variable:created inside a function

#notifying python about a global function, you say "global variable like x"

X=" awesome."

def jerry ():
    global X # notifying python about the global function.
    print("Python is" + X)
     

jerry()# called function
#Data types
#str
#int
#float
#complex
#list
#turples
#dictionaries
#boolean
#data type=method type()

x=5
y = float(x)
print (y)

#modules
#random
#date and time
#turtle
#math


#import math
#import turtle


import random
print(random.randrange(1,5))

#strings are like sentences in python surrounded by quotations. single and double.

#multi- line string
#If the sentences are very long, use three quotations
a="""They are many
 they are girls
 they are two
 I don't remember their names
 and classes"""
# if you want to find the position of a letter. Use square brackets to identify the position of the letters

y="Hello, World"
print(a[3])

#looping "for" loop

for x in "banana":
    print(x) # writes the letters alone

#length of a string

y= "Hello World"
print(len(y))
print("lo" in y) # If you want to find a letter in a word

#finding text that is not
print("le" not in y)

#If statement
if "lo" in y:
    print("Yes, it is")
    
if "wo" not in y:
    print("Hello")
else:
    print("It is there")





   #second week- Indexing is counting from 0

 #Slicing strings
    
b="Hello World"
print(b[2:5])

#include a blank space to represent zero or put a zero eg.(b[space:5]) or (b[0:5])

#including the first character
b="Hello World"
print(b[ :5])


#including the last character
print(b[0: ])# leave a space for the last number.

#Methods- Usually come with brackets. Exaples of methods; Upper and lower


#Upper()= telling a computer to put your sentence in upper case= - Don't include sentences in the brackets.

#Lower()= Make sentence small leters

#Upper
print(b.upper())


#lower
print(b.lower())


#Remove white space(Remove all white spaces from string)
print(b.strip())

#Negative indexes
print(b[-5:-2]) #Worl


#split= Puts commas after a word eg. hello,world
print(b.split(",")
      

# Replacing a character
 print(b.replace("H" ,"J")
       

 #concactenation Joining sentences
a="Atwiine"
       
b="Precious"
       
c=a+b
    
 #To add space, type a+" "+b
d=a+" "+b
       
print(c)
print(d)


#Using format method- Changes or adjusts anything in a string  {}- place holders

age=16
home="Najera"
School="Kjs"       
txt="My name is Precious and I am {0} I stay in {1} and my school is {2}"
print(txt.format(age, home, School))       
      
txt=' I am Precious, my school\'s name is Kjs and my parent\'s name is Atwiine' 

#escape character= "\" put is before every character in the string which has quotations and ain't meant to be a sentence
       

#new line= \n eg. "My name is Precious \n I am in F3"
       

#Boolean values

a = 20
       
b = 30
    
print (a>b)

print (b>a)

if b>a:
       print (" Yes, b is greater than a")
elif b<a:
    print (" B is less")
    
 else:
     print("No it isn't")


#OPERATORS

#Addition
 x= 3+5
 x+=3 # x = x+ 3

 #Subtraction
x-=5 # x = x-5


#DIVISION
x/=1


#MODULUS= Giving the remainder of the number

x%=5 #x= x% 5

5%2 # Divide 5/2 and it gives the remainder as the answer

#EXPONENTIAL

x**=5 # x = x**3

#COMPARISON OPERATORS

#Equals ==
# Not equal !=
# Greater than >
# Less than <


# LOGICAL OPERATORS

#And: 2 >1 and 3 < 1: Returns true when only both of them are true
#Or: Returns true when one of them is true
#Not: reverses the result




#LISTS they create lists using square brackets
thislist=["apples","bannanas"]
print(thislist)

#finding the length of a list
print(len(thislist))

list1=["girl","school","home"]
#list2= you can't change the order


#you can put strings, floats, integers...

#type of list= print(type(thislist))


#list constructor= thislist=list(("a","v","e","w","r")) #note the double round brackets
#print(thislist)



#print second item of list
#print(this list[indexeg.1,2])

#negative index means start from the end or last letter.

#How to know if something is in the list

#If "applae" in thislist:
#print("Yes, \"apple\" in list")

#Changing the second item

#thislist=['apple','banana','juice']
#thislist[1]=Blackcurrant


#Changing using ratios; thislist[1:4]


#Inserting list items
#thislist.insert(2,"Watermelon")
#print(thislist)

#extending lists; adding another type of array into the list

#this list[ "apple","grape"]
#tropical["kiwi","mango"]
#thislist.extend(tropical) # it will get items from tropical to thislist
#print(this list)



#removing items from the list

#thislist.remove("banana")

#removing specified index

#thislist.pop(1) --- If you don't specify the index, it will remove the last item





#to clear a list, type thislist.clear()

#Using a While Loop

#You can loop through the list items by using a while loop.

#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.

#Remember to increase the index by 1 after each iteration.
#Example

#Print all items, using a while loop to go through all the index numbers
#thislist = ["apple", "banana", "cherry"]
#i = 0
#while i < len(thislist):
  #print(thislist[i])
 # i = i + 1 


#List Comprehension

#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Example:

#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

#Without list comprehension you will have to write a for statement with a conditional test inside:
#Example
#fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#newlist = []

#for x in fruits:
 # if "a" in x:
 #   newlist.append(x)

#print(newlist) 

#The Syntax
#newlist = [expression for item in iterable if condition == True]

#The return value is a new list, leaving the old list unchanged.
#Condition

#The condition is like a filter that only accepts the items that valuate to True.
#Example

#Only accept items that are not "apple":
#newlist = [x for x in fruits if x != "apple"]




#PYTHON TUPLES
#Tuple

#Tuples are used to store multiple items in a single variable.

#Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

#A tuple is a collection which is ordered and unchangeable.

#Tuples are written with round brackets.
#Example

#Create a Tuple:
#thistuple = ("apple", "banana", "cherry")
#print(thistuple)
       
#Tuple Items

#Tuple items are ordered, unchangeable, and allow duplicate values.

#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
#Ordered

#When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#Unchangeable

#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#Allow Duplicates

#Since tuples are indexed, they can have items with the same value:       
       
#Example

#Tuples allow duplicate values:
#thistuple = ("apple", "banana", "cherry", "apple", "cherry")
#print(thistuple)
     
#Tuple Length

#To determine how many items a tuple has, use the len() function:
#Example

#Print the number of items in the tuple:
#thistuple = ("apple", "banana", "cherry")
#print(len(thistuple))

#    Create Tuple With One Item

#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
#Example

#One item tuple, remember the comma:
#thistuple = ("apple",)
#print(type(thistuple))

#NOT a tuple
#thistuple = ("apple")
#print(type(thistuple))


#A tuple can contain different data types:
#Example

#A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")

#type()

#From Python's perspective, tuples are defined as objects with the data type 'tuple':
<class 'tuple'>
#Example

#What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#The tuple() Constructor

It is also possible to use the tuple() constructor to make a tuple.
Example

Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


#Python Collections (Arrays)

There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered and unindexed. No duplicate members.
    Dictionary is a collection which is ordered* and changeable. No duplicate members.


#Set

Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is both unordered and unindexed.

Sets are written with curly brackets.
Example

Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset) 


Duplicates Not Allowed

Sets cannot have two items with the same value.
Example

Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


#Set Items - Data Types

#Set items can be of any data type:



#DICTIONARIES

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:
Example

Create and print a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
Dictionary Items

Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
Example

Print the "brand" value of the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
Ordered or Unordered?

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
Changeable

Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
Duplicates Not Allowed

Dictionaries cannot have two items with the same key:
Example

Duplicate values will overwrite existing values:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
Dictionary Length

To determine how many items a dictionary has, use the len() function:
Example

Print the number of items in the dictionary:
print(len(thisdict))
Dictionary Items - Data Types

The values in dictionary items can be of any data type:
Example

String, int, boolean, and list data types:
thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
type()

From Python's perspective, dictionaries are defined as objects with the data type 'dict':
<class 'dict'>
Example

Print the data type of a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
Python Collections (Arrays)

There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered and unindexed. No duplicate members.
    Dictionary is a collection which is ordered and changeable. No duplicate members.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.


#break means stop
       

#Read about while loops
       




















       


       

       
