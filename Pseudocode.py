#Question 1
a77 = int(input("Input a value for A"))
b = int(input("Input a value for B"))
c = int(input("Input a value for C"))
sum1 = (-b+(b**2-(4*a*c))**0.5)/2*a
sum2 = (-b-(b**2-(4*a*c))**0.5)/2*a
print(sum1)
print(sum2)

#Question 2
a1 = int(input("Input a value for A"))
b1 = int(input("Input a value for B"))
c1 = int(input("Input a value for C"))
if a1 > b1 and a1 > c1:
	print (a1, "is the biggest number")
elif b1 > a1 and b1 > c1:
	print (b1, "is the biggest number")
elif c1 > a1 and c1 > b1:
	print (c1, "is the biggest number")

#Question 3

for i in range (1, 51):
	if i% 2==0:
		print (i)

#Question 4
total = 0
total1 = 1
N = int(input("Enter a value for N"))
for o in range (0, N, 1):
	total += total1
	total1 += 1
print(total)

#Question 5
