file1 = open("images of 2025.txt", "r")
file2 = open("Images of 2024.txt", "a")

for line in file1.readlines():
    if not (line.startswith(" I am")):
        print(line)

        file2.write(line)
    
file2.close()
file1.close()