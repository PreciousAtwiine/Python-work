def add():
    a ,b = 20,40
    print(a + b)
add()

def add1():
    a = int(input("Please input your first number:\n "))
    b = int(input("Please input your second number:\n "))
    print(a + b)
add1()
#\n are escape characters   

def add2():
    a = int(input("Please input your first number:\n "))
    b = int(input("Please input your second number:\n "))
    if a % 2 ==0:
        print(f"{a}is an even number and doesn't give a remainder")
    else:
        print(f"{a} is an odd number and gives a remainder")
            
add2()    
    
    