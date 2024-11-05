result = int(input("What is your result?"))
total = 0
amount = 0
while result >= 0:
	total += result
	amount += 1
	result = int(input("What is your other result?"))
average = total/amount
if average >= 90:
	print("A", average)
elif average >= 80:
	print("B", average)
elif average >= 70:
	print("C", average)
elif average >= 60:
	print("D", average, "jamb making")
print(average)