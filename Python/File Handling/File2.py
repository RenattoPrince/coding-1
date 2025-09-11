file = open("Images of 2025.txt", "r" )

Counter = 0

Content = file.read()

CoList = Content.split("\n")
for i in CoList:
    if i.strip():
        Counter += 1
file.close()

print("This is the number of lines in the file:")
print(Counter)

