#Noughts and crosses
moves = 0
turn = 1
player1 = input("Enter a name for player x: ")
player2 = input("Enter a name for player o: ")
Row1 = ["-", "-", "-"]
Row2 = ["-", "-", "-"]
Row3 = ["-", "-", "-"]
print(*Row1)
print(*Row2)
print(*Row3)
while turn == 1:
    xmove = int(input("Enter a number from 1-9"))
    if xmove >= 1 and xmove <= 3:
        Row1[xmove-1] = "X"
        print(*Row1)
        print(*Row2)
        print(*Row3)
        turn += 1
    elif xmove >= 4 and xmove <= 6:
        Row2[xmove-1] = "X"
        print(*Row1)
        print(*Row2)
        print(*Row3)
        turn += 1
    elif xmove >= 7 and xmove <= 9:
        Row2[xmove-1] = "X"
        print(*Row1)
        print(*Row2)
        print(*Row3)
        turn += 1
    while turn == 2:
        ymove = int(input("Enter a number from 1-9"))
        if ymove >= 1 and ymove <= 3:
            Row1[ymove-1] = "O"
            print(*Row1)
            print(*Row2)
            print(*Row3)
            turn -= 1
        elif xmove >= 4 and xmove <= 6:
            Row2[xmove-1] = "X"
            print(*Row1)
            print(*Row2)
            print(*Row3)
            turn -= 1
        elif xmove >= 7 and xmove <= 9:
            Row2[xmove-1] = "X"
            print(*Row1)
            print(*Row2)
            print(*Row3)
            turn -= 1
        

