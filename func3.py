#These are functions that have hard coded values
def add():
    var1 = 22
    var2 = 41
    return var1 + var2
#return allows a value of a variable to be accessed out of the function

print(add())
my_num = add()
print(my_num)
     
def sub():
    var1 = 22
    var2 = 41
    return var2 - var1
print(sub())     

def both():
    return sub() + add()
print(both())

def add1():
    var3 = int(input("Enter first number: "))
    var4  = int(input("Enter second number: "))
    return var3 + var4
print(add1())

def sub1():
    var5 = int(input("Enter the first number: "))
    var6 = int(input("Enter second number: "))
    return var6 - var5
print(sub1())

def both1():
    return add1() + sub1()

print(both1())
