#AllSubString
def printAllSubString(all, SubString):

    if len(all) == 0:
        print(SubString)
        return
    firstChar = all[0]
    restOfString = all[1:]
    
    printAllSubString(restOfString, SubString + firstChar)
    
    printAllSubString(restOfString, SubString)

string = input("Enter a string: ")
printAllSubString(string, "")
