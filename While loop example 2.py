start_value = int (input("Enter a start number"))
end_value = int (input("Enter an end number"))

while start_value <= end_value:
	if start_value % 2 == 0:
		print (start_value)
	start_value = start_value+1
print()