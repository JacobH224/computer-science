#Page 287 Q 5-9
#Question 5

string = input("Enter a string with multiple words ")
string = string.title()
print (string)

#Question 6

string1 = input("Insert a word")
length = len(string1)
string2 = string1[::-1]
if string2 == string1:
	print ("This is a palindrome")
else :
	print ("This is not a palindrome")

#Question 7

#Question 8

string4 = input("Input a word")
length3 = len(string4)
print (string4)
emptystring = ""
for b in range (0, length3, 2):
	emptystring += string4[b]
	if b < (length3-1):
		emptystring += string4[b+1].upper()
print (emptystring)