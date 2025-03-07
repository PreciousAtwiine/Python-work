fruits = ["apple", "mango", "orange", "banana", "grapes"]
#for item in fruits:
    #print(item)
    #if item == "banana":
       # break #this will stop the loop when the item is banana and you can also use continue to skip the item plus "pass" can also be used to break
 
numbers = [10,20,30,40,50,60,70,80]  
#A function is a named block of code that performs a specific task
#name of this block is called evens. When creating a function, we start with the keyword def followed by the name of the function 
def evens():
    for item in numbers:
        if item % 2 == 0:
            print(item)

def fruit():
    for item in fruits:
        print(item)            
        
fruit()
evens() #this will call the function evens
#A function can be called as many times as you want     
#print()
#type() #this is a built-in function in python that returns the type of the object   