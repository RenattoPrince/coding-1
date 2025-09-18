with open('Images of 2024.txt', 'w') as file:
    file.write("\nHi! I am Pemguin and i am 1yr old")
file.close()


with open('Images of 2024.txt', 'r') as file:
    data = file.readlines()
    print("words in theis file are....")
    for line in data:
        word = line.split()
        print (word)
file.close()        