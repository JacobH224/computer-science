#Strings Questions C
#Question 1

number = 0
number = input("Enter a valid phone number")
length = len(number)

if length == 12 and number[3] == "-" and number[7] == "-" and :
    print (number, ":", "valid number")
else:
    print (number, ":", "invalid number")
    
#Question 2

total = 0
emptyString = ""
userInput = input("Enter a string")
length2 = len(userInput)
for a in range (0, length2, 1):
    if userInput[a].isDigit() == True:
        total += int(userInput[a])
        emptyString += userInput[a]
if total != 0 and emptyString != "":
    print (userInput, total, emptyString)
else:
    print ()
        
        