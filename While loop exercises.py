#While loop exercises

#While loop exercise 1

total = 0
amount = 0
integer = input("Enter a number")
while integer != "":
    integer = int(integer)
    total += integer
    amount += 1
    integer = input("Enter a number")
print(total / amount)

#While loop exercise 2

totaltwo = 0
amounttwo = 0
userInput = int(input("Enter an integer: "))
while userInput >= 0:
    totaltwo += userInput
    amounttwo += 1
    userInput = int(input("Enter an integer: "))
print (totaltwo / amounttwo)

#While loop example 3

totalthree = 0
amountthree = 0
grade = int(input("Enter your grade"))
while grade > 0:
    totalthree += grade
    amountthree += 1
    grade = int(input("Enter your grade"))
average = totalthree / amountthree
if average >= 90:
    print ("A")
elif average <= 89 and average >= 80:
    print ("B")
elif average <= 79 and average >= 70:
    print ("C")
elif average <= 69 and average >= 60:
    print ("D")
elif average <= 59:
    print ("F")
print ("Your average grade is: ", average)

#While loop exercise 4

userInputTwo = int(input("Enter a number"))
while userInputTwo > 0:
    print (userInputTwo)
    userInputTwo -= 1
print (userInputTwo)

##While loop exercise 5

start = 0
number = int(input("Enter a number: "))
while start < number:
    print (start)
    start += 1
print (start)