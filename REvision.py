#Q1

temp = int(input("Enter a temperature"))
if temp < 32:
	print("ice")
elif temp < 212:
	print("water")
else:
	print("steam")

#Q2

x = 1
if x > 3:
	if x > 4:
		print ("A", end= '')
	else:
		print ("B", end= '')
elif x < 2:
	if (x != 0):
		print ("C", end= '')
print ("D")

#Q3

weather = 'raining'
if weather == 'sunny':
	print ("wear sunblock")
elif weather == "snow":
	print ("going skiing")
else:
	print (weather)

#Q4

zero = 0
if int(zero) == 0:
	print ("zero")
elif str(0) == "zero":
	print (0)
elif str(0) == '0':
	print (str(0))
else:
	print ("none of the above")

#Q5

n = int(input("Enter a value"))
if n == 0:
	print ("zero")
elif n == 1:
	print ("one")
elif n == 2:
	print ("two")
elif n == 3:
	print ("three")
else:
	print ("invalid")

#Q6

n = int(input("Enter an integer: "))
if n < 1:
	print ("invalid input")
else:
	for i in range (1, n + 1):
		print (i * i)



#Q7(b)

n = int(input("Enter an integer"))
if n > 0:
	for a in range(1, n + n):
		print (a/(n/2))
	else:
		print ("Now quiting")