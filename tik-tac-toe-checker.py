def is_solved(board):
    X = False
    O = False
    empty_spots = False
    
    for row in range(3):
        for colum in range(3):
            if board[row][colum] == 0:
                empty_spots = True
            if board[row][colum] != 0:
                print('checking ' + str(board[row][colum]) + ' on col ' + str(colum) + ' and row ' + str(row))
                if check(board, row, colum, board[row][colum]):
                    print(board[row][colum])
                    if board[row][colum] == 1:
                        X = True
                    elif board[row][colum] == 2:
                        O = True
                    
    if X == False and O == False and empty_spots == True:
        return -1
    elif X == True and O == False:
        return 1
    elif X == False and O == True:
        return 2
    else:
        return 0
            

def check(board, row, colum, num):
    wonrow = 0
    woncol = 0
    for rows in range(3):
        if board[rows][colum] == num:
            wonrow+=1
    for cols in range(3):
        if board[row][cols] == num:
            woncol+=1
    if board[0][0] == num and board[1][1] == num and board[2][2] == num:
        woncol = 3
    if board[0][2] == num and board[1][1] == num and board[2][0] == num:
        woncol = 3
    if wonrow == 3 or woncol == 3:
        return True
