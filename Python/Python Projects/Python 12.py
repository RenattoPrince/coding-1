#First set bit
def FirstSetBit(n):
    return n & -n
number = int(input("Enter your number:"))
print(f"First set bit is: {FirstSetBit(number)}")
