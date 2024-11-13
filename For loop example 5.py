#For loop exercise 5
total = 0
n = int(input("Input a value for n: "))
for x in range(1, n+1, 2):
    total += x**2
print (total)