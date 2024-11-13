#for loop exercise 3

N = int(input("Enter an integer"))
for total in range(11, N+1, 1):
    if total % 3 == 0 and total % 7 != 0:
        print ("Tipsy")
    elif total % 7 == 0 and total % 3 != 0:
        print ("Topsy")
    elif total % 7 == 0 and total % 3 == 0:
        print ("Tipsy topsy")
    else:
        print (total)