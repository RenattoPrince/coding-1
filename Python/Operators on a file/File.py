file = open("Images of 2025.txt", "r")
print(file.read())
file.close()

file = open("Images of 2025.txt", "r")
print("reading parts of a file")
print(file.read(9))
file.close()

file = open("Images of 2025.txt", "a")
file.write("\nI am viewing a file")
file.close()

print('\n\n')
file = open("images of 2025.txt", "r")
print("\nMultiple Lines in a file\n")
print(file.readline())
print(file.readline())
file.close()

file = open("images of 2025.txt", "r")
print("\All lines in a file\n")
print(file.readlines())
file.close()