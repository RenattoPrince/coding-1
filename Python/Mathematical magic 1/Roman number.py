def romanToInt(romanInput):
    roman = {'M': 1000, 'D': 500, 'C': 100,
             'L': 50, 'X': 10, 'V': 5, '1': 1}
    resultInteger = 0
    for i in range(len(romanInput) - 1):
        if roman [romanInput[i] ]< roman[romanInput[i+1]]:
            resultInteger -= roman[romanInput[i]]
        else:
            resultInteger += roman[romanInput[i]]
    resultInteger += roman[romanInput[-1]]
    return resultInteger

roman = input("Input Roman numereal:").upper()
print("Integer equivalant:", romanToInt(roman))