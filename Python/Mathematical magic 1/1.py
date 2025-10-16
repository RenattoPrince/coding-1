def print_factors(numbers):
    print("The factors of", numbers,"are:")
    for i in range(1, numbers + 1):
        if numbers % i == 0:
            print(i)


numbers = int(input("Enter your number to find its factors:"))
print_factors(numbers)