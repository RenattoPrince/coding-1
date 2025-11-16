#Power of 8s
def power8(number):
    if number == 0:
        return False
    return (number & (number - 1)) == 0

number = int(input("Enter the number:"))
if power8(number):
    print(number, "is a power of 8")
else:
    print(number, "is not a power of 8")
