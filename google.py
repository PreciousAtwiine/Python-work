import random
print ("HELLO AND WELCOME TO Google Assistant")
print("PLEASE NOTE THAT YOU HAVE TO ANSWER THE QUESTIONS WITH LOWER CASE LETTERS")

print("Fill in the information below to create your google account!!")
first=input("First name;")
second=input("Second name;")
 
sec=random.choice(second)
num=random.randrange(0,9)
gmail="@gmail.com"
email=sec + first + str(num)
txt="Your email is {0}{1}"
print(txt.format(email,gmail))
print("GOOD LUCK!!")

    
    

