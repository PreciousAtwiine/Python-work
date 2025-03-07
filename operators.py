num1 = 100
#the equal sign is the operator
#the variable num1 is the operand
#100 is the value
#An operator is a character or a special symbol that tells a computer what to do with the operands
#Types of operators;
#Arithmetic operators
#Assignment operators
#Bitwise operators
#Logical operators
#Comparison operators

#Arithmetic operators
#Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, division, etc.
num1,num2= 30,200
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2) #the answer will have a decimal point
print(num1//num2) #floor division eliminates the decimal point
print(num2**num1) #exponentiation(raise to the power)
print(num2 % num1) #modulo(remainder)
print(num1%num2)



#Assignment operators
#Assignment operators are used to assign values to variables
num3 = 100
num3 += 10 #num3 = num3 + 10
print(num3)
num3 -= 10 #num3 = num3 - 10
print(num3)
num3 *= 10 #num3 = num3 * 10
print(num3)
num3 /= 10 #num3 = num3 / 10
print(num3)
num3 //= 10 #num3 = num3 // 10
print(num3)
num3 **= 10 #num3 = num3 ** 10
print(num3)
num3 %= 10 #num3 = num3 % 10
print(num3)


#25th Feb
#Comparison operators
#These operators are used to compare two values and return a boolean
#In mathematics we have operators like >,<,>=,<=,==,!=

#Let's declare some variables
comp1 = 20
comp2 = 40

print(comp1<comp2) #less than
print(comp1>comp2) #greater than
print(comp1<=comp2) #less than or equal to
print(comp1>=comp2) #greater than or equal to
print(comp1==comp2) #equal to
print(comp1!=comp2) #not equal to

#Logical operators
#These operators are used to combine conditional statements i.e. and, or(||), not(! )
log1 = 5
log2 = 6
print(log1 > log2) and (log1 < log2) #and operator (Gives you trues when everthing is true)
print(log1 > log2) or (log1 < log2) #or operator (Gives you true when atleast one is true)
print(not(log1 > log2)) #not operator #SHould not be inbetween the statements...it only starts the statements
print(not(log1 < log2)) #not operator
print(True and True) #Prints true
print(True and False) #Prints false
print(not True) #Prints false
print(True or True) #Prints true
print(False or False) #Prints false
print(True or False) #Prints true


#Membership operators
#These operators are used to test if a sequence is presented in an object
#In python we have two membership operators; in, not in
#They return a boolean value
numbers = {20,30,40,50,60}
print(20 in numbers)
print (20 not in numbers)

name = "Precious"
print("p" not in name)

#Identity operators
#These operators are used to compare the objects, not if they are equal but if they are actually the same object with the same memory location
#In python we have two identity operators; is, is not 
#They return a boolean value
print (20 is not numbers)
print (20 is numbers) 
print (20 is 20)
