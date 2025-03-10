class Fruit:
    def __init__(Precious,name,color,taste,price):
        Precious.name = name
        Precious.color = color
        Precious.taste = taste
        Precious.price = price
#Don't begin with capital letters when naming a variable        
mango = Fruit("Mango", "Yellow","Sweet",1000)
apple = Fruit("Apple","Green","Sweet",2500)

class Animal:
    def __init__(self,name,breed,age,size):
        self.name = name
        self.breed = breed
        self.age = age
        self.size = size
    def display_details(self):
        print(f"The animal name is {self.name}. The animal breed is {self.breed}.") 
#Dog class has inherited from Animal class .It now has 2 methods       
class Dog(Animal):
    def sound(self):
        print("Dogs bark")
dog = Dog("Simba","Bull dog",10,"Big")  
dog.display_details()

class Bulldog(Dog):
    def greet(self):
        print("Bull dog wags its tail")
"""
Use at least 5 classes to demonstrate inheritance in python, use a constuctor with at least 7 parameters with corresponding properties 
The last class should be taking at least 5 methods
"""        
    
    

      

        
        


        