
import random
board = [[' ' for i in range(3)] for j in range(3)]

def printRow(row, symbol,str = None):
    for j in range(len(row)):
        if str == None:
            print(f' {row[j]} ',end='')
        else:
            print(f'{str}',end='')
        if j == len(row) - 1:
            continue
        print(symbol,end='')
        

def printBoard(board):
    for i in range(len(board)):
        printRow(board[i],chr(9553))
        print()
        if i == len(board) - 1:
            continue
        printRow(board[i],chr(9580),f'{chr(9552)*3}')
        print()
def getCoord(cell):
    match cell:
        case 1:
            return (0,0)
        case 2:
            return (0,1)
        case 3:
            return (0,2)
        case 4:
            return (1,0)
        case 5:
            return (1,1)
        case 6:
            return (1,2)
        case 7:
            return (2,0)
        case 8:
            return (2,1)
        case 9:
            return (2,2)


def checkLine(board,*cells):
    x_1, y_1 = getCoord(cells[0])
    x_2, y_2 = getCoord(cells[1])
    x_3, y_3 = getCoord(cells[2])
    if board[x_1][y_1] == board[x_2][y_2] and board[x_1][y_1] == board[x_3][y_3]:
            return True
    else:
        return False

def checkWin(board):
    if board[0][0] != ' ':
        if checkLine(board,1,2,3):
            return board[0][0]
        if checkLine(board,1,4,7):
            return board[0][0]
        if checkLine(board,1,5,9):
            return board[0][0]
    if board[0][1] != ' ':
        if checkLine(board,2,5,8):
            return board[0][1]
    if board[0][2] != ' ':
        if checkLine(board,3,6,9):
            return board[0][2]
        if checkLine(board,3,5,7):
            return board[0][2]
    if board[1][0] != ' ':
        if checkLine(board,4,5,6):
            return board[1][0]
    if board[2][0] != ' ':
        if checkLine(board,7,8,9):
            return board[2][0]
    
# [1 - 9]
printBoard(board)
count = 9

user = 'X'
bot = 'O'
flag = True

while count > 0:
    if flag:
        step = int(input('Enter number cell > '))
        x,y = getCoord(step)
        if board[x][y] != ' ':
            continue
        board[x][y] = user
        flag = False
        count-=1
    else:
        x,y = getCoord(random.randint(1,9))
        if board[x][y] != ' ':
            continue
        board[x][y] = bot
        flag = True
        count-=1
    print()
    printBoard(board)
    win = checkWin(board)
    if win != None:
        break
if win == user:
    print(f'Win User {user}')
elif win == bot:
    print(f"Win bot {bot}")
else:
    print('Draw')
