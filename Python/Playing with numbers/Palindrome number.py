value= input("Enter a value too check for palidrome number:").upper()
reverse = value[::-1]
if value==reverse:
    print(f"{value} is a palindrome number")
else:
    print(f"{value} is not palindrome number")