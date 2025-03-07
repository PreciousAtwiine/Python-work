#Static functions have static values/fixed in their variables
def add():
    num = 5
    num1 = 10
    return num +num1
print(add())

#Dynamic functions expect values on the call of function
def add1(num, num1):
    return num + num1 

print(add1(20,50))
print(add1(49,70))
print(add1(65,15))

#Dynamic functions and static functions
#A variable within the brackets is called a parameter
#Values for parameters are called arguments

#Assignment ; using dynamic functions together with input fuctions,create a program that can capture student details one student details per time ; name,age,gender,program,course,year of study, 1st tests mark,2nd,course work mark and exam mark
#Calculate the 2 best term among tests 1,2 and course work
#The 2 best done average is marked out of 40. Exam mark is marked out of 60
    
#Both static and dynamic functions return a value
#Arguments must fulfill the parameter list
#a return statement marks the end of execution in the function
 