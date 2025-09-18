new_file = open('new_File1.txt','x')
new_file.close()

import os
print("Checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
    print("File exists and is being deleted....")
    os.remove("my_file.txt")
    print("File deleted successfully...")
else:
    print("File does not exist...")

my_file = open("my_file.txt","w")
my_file.write("Hi I am Pemguin and i am 1yr old")
my_file.close()

os.remove('Images of 2024.txt')
os.rmidr('folder_Here')
