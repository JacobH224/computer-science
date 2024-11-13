#for loop exercise 1

side_one = int(input("Enter the first side"))
side_two = int(input("Enter the second side"))
side_three = int(input("Enter the third side"))
if side_one == side_two == side_three:
    print ("equilateral", side_one, side_two, side_three)
elif side_one != side_two != side_three:
    print ("scalene", side_one, side_two, side_three)
elif side_one == side_two != side_three:
    print ("isoceles", side_one, side_two, side_three)
elif side_one != side_two == side_three:
    print ("isoceles", side_one, side_two, side_three)
elif side_one != side_three == side_two:
    print ("isoceles", side_one, side_two, side_three)
