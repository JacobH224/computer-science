#Page 254 Strings
#Example 1

name = "superb"

for ch in name:
	print(ch, '- ', end = "")

#Example 2

string1 = input("Enter a string")
print("The", string1, "in reverse order is: ")
length = len(string1)
for a in range (-1, (-length -1), -1):
	print(string1[a] )

#Example 3

string2 = input("Enter a string")
length = len(string2)
i = 0
for a in range (-1, (length -1), -1):
	print (string2[i], "\t", string2[a])
	i += 1