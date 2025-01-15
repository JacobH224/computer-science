#Question1
input1 = input("Enter a string")
for x in input1:
	print(x)

#Question1
input2 = input("Enter a string")
for y in range (0,len(input2)):
	print(input2[y])

#Question2
input3 = input("Enter a string")
for z in range (0,len(input3)):
	if input3[z].isupper():
		print(input3[z].lower())
	elif input3[z].islower():
		print(input3[z].upper())

#Question3
input4 = input("Enter a string")
string = ""
for a in range (0,len(input4)):
	string += input4[a] * 2
print(string)