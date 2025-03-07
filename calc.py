#Simple calculator

#Add
def add(x,y):
    return x + y

#subtract
def subtract(x,y):
    return x - y

# multiply
def multiply(x,y):
    return x * y

#Divide
def divide(x,y):
    return x / y

#Printing
print("Select operator of your choice.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

#input
sign = input(" Enter numbers (1/2/3/4) respectively for your choices: ")

#numbers
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

if sign == "1":
   print(a, "+", b,"=", add(a,b))

elif sign == "2":
     print(a,"-", b,"=", subtract(a,b))
     
elif sign == "3":
      print(a, "*", b,"=", multiply(a,b))
            
elif sign == "4":
      print(a,"/", b,"=", divide(a,b))

else:
      print("Invalid answer")
  
            
 
