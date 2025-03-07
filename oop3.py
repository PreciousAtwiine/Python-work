#Properties/Principles of OOP
#Abstractions:Things that are not clear
#Encapsulation :Ability to hide or control some of the internal functionality of its data
#Polymorphism : The ability to take in more than one form
#All objects have a level of abstraction
#Inheritance is two individual classes sharong the same properties
#inheritance is the ability of a sub/child/derived-class to take on one or more attributes of a super/parent/base class
class Animal():
    name = ""
    color = ""
    weight = 0
    owner = ""
#A method is a function within a class-the statement you write in a method are referred to as behaviours   
    def sound(self):
        print("I bark")
        
dog = Animal()
dog.sound()
        
    
    


