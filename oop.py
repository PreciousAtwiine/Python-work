#Object oriented programming
#We'll be looking at ;
#Classes,objects, properties(attributes,characteristics,features)
#Methods , constructors
#Principles of object oriented programming(abstruction,encapsulation,inheritance and polymorphism)
#Overloading and over-riding
#Oop is a programming concept that advocates writing software based on real world objects.
#Classes are identified in singular
#Objects are gotten from classes or they're classified
#A class is a blueprint of an object
#An object is an instance of a class 
#Classes defines the attributes,features , characteristics of objects.
#A blueprint means the original copy of something
#Date,time,venue,name of guest,contacts-features of invitation card
#name,type,color,price,origin-defining class onion
#A phrase= "is a" is used to identify a phrase/a class of a particular object
#An object should fulfill all the properties of a class

student = ["Precious", "Pearl" , "Priscilla"]
student1 = {"name":"Precious","Gender":"Female","School":"Refactory Academy"}

class Laptop():
    pass

class Food():
    name = ""   #Properties
    taste = ""
    calories = 0
    price = 0
    food_value = ""
#creating objects out of class food
matooke = Food()
matooke.name = "Matooke"  
matooke.taste = "Sweet"
matooke.calories = 100
matooke.price = 12,000
matooke.food_value = "Carbohydrates"  

rice = Food()
rice.name = "Rice"
rice.taste = "Sweet"
rice.calories = 200
rice.price = 8000
rice.food_value = "Carbs"

beans = Food()
beans.name = "Beans"
beans.taste = "Salty"

print(matooke.name)

    



