#For loop exercise question 4

M = int(input("Input a value for M: "))
N = int(input("Input a value for N: "))
for total in range(1, M+1, 1):
    if total % N == 0:
        print (total)
        if total % 2 == 0:
            print ("Even")
        else:
            print ("Odd")