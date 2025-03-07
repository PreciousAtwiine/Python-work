test1 = int(input("Enter first test marks: ")) 
test2 = int(input("Enter second test marks: "))
course_work = int(input("Enter your course work marks: "))
def student_details():
    name = input("Enter student's name: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    school = input("Enter school: ")
    course = input("Enter course: ")
    yearofstudy = input("Enter your year of study: ")
    num1 = test1 #Local variable
    num2 = test2  
    work = course_work
    return{"Name":name,"age":age,"Gender":gender, "School": school,"course": course, "Year of study":yearofstudy,"Test 1":num1, "Test2":num2, "Course work":work}
for _ in range(3):
    details = student_details()
    print(details)
def calc():
    return (test1 + test2 + course_work)/2 *0.4   
print(calc())

num3 =(input("Best done: "))    