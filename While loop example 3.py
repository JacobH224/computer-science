user_input = int(input("Enter a positive number: "))
running_total = 0
if user_input > 0:
	while user_input > 0:
		running_total = running_total + user_input
		user_input = int(input("Enter a positive number"))
	else:
		print("The total of the positive numbers entered was", running_total )
else:
	print("The total of the positive numbers entered was", running_total )