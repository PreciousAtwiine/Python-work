num1 = input("Input your number here:")
print("The number you input is:", num1)
#Here we're giving the user the allwance of putting a value in a memory location
    
name = input("Input your name here:")
print("Hello", name)
#input is a mechanism through which we can initialize values from the keyboard
#Program/code to interprete
num2 = int(input("Input your first number:"))
num3 = int(input("Input your second number:"))
# 
#operator = input("Choose the operator you want to use:")
if num2 >= num3:
    print(f"Error: The first number{num2} should be less than the second number{num3}")
if num2 % num3 ==0 :
    print(f"{num2} is divisible by {num3}")
# f is used to format the string and enables the use of variables in the string
if num2 != 0 : #This is used to check if the value is not 0
    num3 += num2
    print(num3) #here it will print the new num2
    
     
