file = open("Images of 2025.txt", "r" )
print(file.read())
file.close()
file = open("Images of 2025.txt", "w" )
file.write("File 1 march 2025")
file.close()

file = open("Images of 2025.txt", "a" )
file.write("\n Folder 2 september 2025")
file.close()


