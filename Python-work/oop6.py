class House:
    def __init__(self,color,size,type):
        self.color = color
        self.size = size
        self._type = type #Any property of a class that starts with _is a private property
    def house_cleaning(self): 
        print(f"type {self._type} needs to be cleaned twice in a week") 
house1 = House("grey","big","Flat house")
print(house1._type)
print(house1.size)
#Type is a private document.
class Hat(House):
    def roofing(self):
        print("It is usually grass thatched")  
class Tent(Hat):
    def strength(self):
        print("This property is weak hence can be blown by wind")
        
                  
        
         
        