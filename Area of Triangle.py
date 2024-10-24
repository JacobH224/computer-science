side_one = int(input("Enter the length of the first side in cm "))
side_two = int(input("Enter the length of the second side in cm "))
side_three = int(input("Enter the length of the third side in cm "))
answer = (side_one + side_two + side_three) / 2
area = (answer * (answer - side_one) * (answer - side_two) * (answer - side_three))
print (area **0.5)