print (" Hello!!")
print (" I'm a virtual scientific calculator")
try:
    num1=float(input("Please enter the first number")
    operator=("Please choose the operator (+) for addition, (-) for subtraction (*) for multiplication, (%) for remainder and (/) for division")         

    num2= float(input("Please input the second number")

if sign =="+":
   result= num1 + num2
   print("The answer is ;" , result)
 elif operator=="-":
     result= num1 - num2
     print("The answer is ;" , result)
     elif operator =="*":
         result= num1 * num2
         print("The answer is ;", result)
         elif sign == "/":
             try:
                 if True:
                     result= num1 / num2
                     print(result)

                    elif operator == "%":
                        result = num1 % num2
                        print("The answer is;", result)
                        
                    else:
                        print(" Operator not unterstood!!")

finally:
    print("All Done")
