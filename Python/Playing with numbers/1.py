# Enter the numbers
largestnum=int(input("Enter Largest number: "))
smallestnum=int(input("Enter smallest number: "))
print(f"HCF/GCF of {largestnum}) and {smallestnum} is:")
# Eucleads algorthims
while (smallestnum):
    numstore=smallestnum
    smallestnum=largestnum%smallestnum
    largestnum=numstore
print(largestnum)