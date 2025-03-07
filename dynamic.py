#An algorithm is a step by step process of solving a particular problem
#Still on oop's
class Animal:
#This is a constructor always defined with two underscores
#A constructor is used to initialise/give a value of an object of a class    
    def __init__(self,name,size , type, color, sound):
        self.animalname = name
        self.animalsize = size
        self.animaltype = type
        self.animalcolor = color
        self.animalsound = sound
cat = Animal("cat","small","domestic","black","meow")        
        
        
        
    