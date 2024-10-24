question_one = (input ("Are you 18?"))
if question_one.lower()=="yes":
	print ("You can vote")
else:
	question_two = int(input("Are you 17?"))
	if question_two.lower()=="yes":
		print ("You can learn to drive")
	else:
		question_three = (input("Are you 16?"))
		if question_three.lower()=="yes":
			print ("You can buy a lottery ticket")
		else:
			question_four = (input("Are you 15?"))
			if question_four.lower()=="yes":
				print ("You can go trick or treating")
