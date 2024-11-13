#For loop example questions

#for loop exercise 1

side_one = int(input("Enter the first side"))
side_two = int(input("Enter the second side"))
side_three = int(input("Enter the third side"))
if side_one == side_two == side_three:
    print ("equilateral", side_one, side_two, side_three)
elif side_one != side_two != side_three:
    print ("scalene", side_one, side_two, side_three)
elif side_one == side_two != side_three:
    print ("isoceles", side_one, side_two, side_three)
elif side_one != side_two == side_three:
    print ("isoceles", side_one, side_two, side_three)
elif side_one != side_three == side_two:
    print ("isoceles", side_one, side_two, side_three)

#for loop exercise 2

num = int(input("Enter an integer"))
if num % 10 == 4:
    print ("Ends with 4")
elif num % 10 == 8:
    print ("Ends with 8")
else:
    print ("Ends with neither")
    
#for loop exercise 3

Nn = int(input("Enter an integer"))
for total in range(11, N+1, 1):
    if total % 3 == 0 and total % 7 != 0:
        print ("Tipsy")
    elif total % 7 == 0 and total % 3 != 0:
        print ("Topsy")
    elif total % 7 == 0 and total % 3 == 0:
        print ("Tipsy topsy")
    else:
        print (total)
        
#For loop exercise 4

M = int(input("Input a value for M: "))
N = int(input("Input a value for N: "))
for total in range(1, M+1, 1):
    if total % N == 0:
        print (total)
        if total % 2 == 0:
            print ("Even")
        else:
            print ("Odd")
            
#For loop exercise 5
total = 0
n = int(input("Input a value for n: "))
for x in range(1, n+1, 2):
    total += x**2
print (total)

#For loop exercise 6

absolute = -273.15
Temp = int(input("Enter the temperature: "))
Unit = (input("Enter the unit: "))
if Unit == "celcius":

elif Unit == "fahrenheit":
