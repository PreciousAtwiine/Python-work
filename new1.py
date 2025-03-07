def student_details():
    name = input("Enter student's name: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    school = input("Enter school: ")
    course = input("Enter course: ")
    yearofstudy = input("Enter your year of study: ")
    return{"name":name,"age":age,"Gender":gender, "School": school,"course": course, "Year of study":yearofstudy}
for _ in range(3):
    details = student_details()
    print(details)
 
#Global variables
test1 = int(input("Enter first test marks: ")) 
test2 = int(input("Enter second test marks: "))
course_work = int(input("Enter your course work marks: "))
def tests():
    num1 = test1 #Local variable
    num2 = test2  
    work = course_work
    return (num1,num2,work)
print(tests())    

def calc():
    return (test1 + test2)/2 *0.4   
print(calc())

num3 =(input("Best done: "))
num4 = input("Enter final mark: ")
def final_exam():
    num5 = num4
    return num4*0.6
print(final_exam())

def final():
    num4 + num3
    return(final())
print(final())
  