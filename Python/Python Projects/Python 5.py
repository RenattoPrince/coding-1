print("This is a code which calculates the input of an armstrong number to check if its right or wrong")
num = int(input("Enter a number: "))
length = len(str(num))

sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10

if num == sum:
    print(f"{num} is an Armstrong number!")
else:
    print(f"{num} is not an Armstrong number:(")