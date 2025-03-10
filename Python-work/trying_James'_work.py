import os
def write_to_file():
    with open("myfile.txt","w") as file:
        file.write("This is the file I intend to write in my file. \n")
        file.write("This is the second line.\n")
        file.write("This text overrides what has been found there")
    print("Data written to 'myfile.txt' successfully.")    

def append_to_file():
    with open("myfile.txt","a") as file:
        file.write("Writing to a Text File in Python provides built-in functions to handle file operations like reading and writing. Below is a well-explained example of how to write to a .txt file in Python.\n")
    print("New data appended to 'myfile.txt'.")
    
def read_file():
    if os.path.exists("myfile.txt"):
        with open("myfile.txt" , "r") as file:
            content = file.read()
            print("\n FILE CONTENTS") 
            print (content)  
    else:
        print("Error ! 'myfile.txt' does not exist")          
    
    