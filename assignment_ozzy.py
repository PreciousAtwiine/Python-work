#some_string is a variable
some_string = 'Python is fun' 
#Sequence datatypes
a, b, c = 5, 3.2, 'Hello'

print(a)  #is an integer
print(b)  #is a float
print(c)  #is a string

#this is an integer
num1 = 5
#this is command will print the type of the variable num1 which is an integer
print(num1, 'is of type', type(num1))
#this is a float
num2 = 2.0
#this command will print the type of the variable num2 which is a float
print(num2, 'is of type', type(num2))
#this is a complex number
num3 = 1+2j
#this command will print the type of the variable num3 which is a complex number
print(num3, 'is of type', type(num3))
#this is a list with 3 string elements
languages = ["Swift", "Java", "Python"]

#this will return the first element in the list
print(languages[0])   #The output will be Swift since it is the first element in the list

#this will return the second element in the list
print(languages[2])   #The output will be Python since it is the second element in the list

#This is a tuple since it is represented by round brackets
product = ('Microsoft', 'Xbox', 499.99)

#This will return the first element in the tuple
print(product[0])   #Microsoft

#This will return the second element in the tuple
print(product[1])   #Xbox


#This is a dictionary
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
#Will print the dictionary
print(capital_city)


#This is a set since it is represented by curly brackets
student_id = {112, 114, 116, 118, 115}

#will print the set
print(student_id)

#will print the type of the variable student_id which is a set
print(type(student_id))

#this is a list since it is represented by square brackets
fruits = ["apple", "mango", "orange"] 
#expected output is list
print(fruits)

#this is a tuple since it is represented by round brackets
numbers = (1, 2, 3) 
#will print out all the elements
print(numbers)

#this is a dictionary since it is represented by curly brackets
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
#will print out the dictionary
print(alphabets)

#this is a set
vowels = {'a', 'e', 'i' , 'o', 'u'} 
print(vowels) 


#this is a set
student_id = {112, 114, 116, 118, 115}

#will return all the elements in the set
print(student_id)

#display type of student_id
print(type(student_id))
#this is a atuple
product = ('Microsoft', 'Xbox', 499.99)

#displays the element in position 0
print(product[0])   #Microsoft

#displays the element in position 1
print(product[1])   #Xbox




#assigning values to variables
a = 7
b = 2

#Arithmetic Operators
print ('Sum: ', a + b)  

#Displays difference between the 2 variables
print ('Subtraction: ', a - b)   

#Multiplies the 2 variables
print ('Multiplication: ', a * b)  

#Divides the 2 variables - the answer will have a decimal point
print ('Division: ', a / b) 

#Eliminates the decimal point
print ('Floor Division: ', a // b)

#Shows the remainder
print ('Modulo: ', a % b)  

#Exponentiation(raise to the power)
print ('Power: ', a ** b)   


#Assigned 10 to variable a
a = 10

# assigned 5 to variable b
b = 5 

#Assignment Operators
a += b      #a = a + b
print(a)
#Output: 15


#equal to
print('a == b =', a == b) #will return false since a is not equal to b

#Not equal to
print('a != b =', a != b)

#Greater than
print('a > b =', a > b)

#Less than
print('a < b =', a < b)

#Greater than or equal to
print('a >= b =', a >= b)

#Less than or equal to
print('a <= b =', a <= b)
#And operator - returns true if both conditions are true
print((a > 2) and (b >= 6))  #Will return true since both conditions are true

#And operator
print(True and True)     # True
print(True and False)    # False

#logical OR boolean operator
print(True or False)     #Prints true

#logical NOT boolean operator(!)
print(not True)          #Prints false

#Assigning values to variables
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
#Identity Operators
#These operators are used to compare the memory locations of two objects
print(x1 is not y1)  #Will only return true if the memory locations of x1 and y1 are not the same

#Comparing the 2 memory locations
print(x2 is y2)  #Displays true since the memory locations of x2 and y2 are the same

#False
print(x3 is y3)  #REturns false since the memory locations of x3 and y3 are not the same

#String
message = 'Hello world'

#Dictionary
dict1 = {1:'a', 2:'b'}
#Membership Operators
#These operators are used to test if a sequence is presented in an object
print('H' in message)  #Will only return true if the letter H is in the message

#true
print('hello' not in message)  #Will return true since hello is not in the message

# true
print(1 in dict1)  #Will return true since 1 is in the dictionary

#false 
print('a' in dict1)  #will return false since a is not in the dictionary
