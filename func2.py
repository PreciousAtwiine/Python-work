number = int(input("Input the number of entries: "))
dict = {input("Enter key: "): input("Enter value: ") for _ in range(number)}
print(dict)
#the funtion must not have the same name as the variable above

def enter_data():
    enter_data = int(input("Input the number of entries: "))
    dict1 = {input("Enter key: "): input("Enter value: ") for _ in range(enter_data)}
    print(dict1)
enter_data()

#Using the notion of functions, capture the details of student:
#details, name,age ,gender, program,faculty,year of study,D.O.B
#Test1 marks, test2 marks, final exams, marks(summation)  

#A value within a function can never be accessed outside the function
#Local variables are variables that are limited within a particular block
#A function is a named block


num1 = int(input("The number of entries: ")) #global variable because it can be accessed inside the function
def enter():
    num2 = num1 #num2 is a local variable
    capture = {input("Enter key: "): input("enter value: ") for _ in range(num2)}
    print (capture)
enter()
   
    
    