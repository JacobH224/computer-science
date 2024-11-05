#print all the multiples of 5 up to a limit input by the user
user_limit = int (input("Enter an integer limit on the multiples of 5"))

multiples = 5
while multiples < user_limit:
	print(multiples)
	multiples = multiples + 5
print()