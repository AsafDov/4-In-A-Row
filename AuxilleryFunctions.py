import numpy as np
import os # for windows only


def newBoard():
    board = np.zeros((6, 7));
    os.system('cls');
    return board;

def drop(board, row, col, disk):
    board[row][col] = disk;

def isLegalInput(board, col):
    if col in range(7):
        if board[5][col] ==0:
            return True;
    return False;
def getAvailableRow(board, col):
    for row in range(6):
        if board[row][col] == 0:
            return row

def printBoard(board):
    os.system('cls');
    print(np.flip(board,0))

def didIWin(board,row,col,disk):
    countVertical =0;
    countRightDiagonal=0;
    countHorizontal=0;
    countLeftDiagonal=0;
    for i in [-3,-2,-1,0,1,2,3]:
        # Vertical
        if col +i>=0 and col+i<7:
            if board[row][col+i] ==disk:
                countVertical = countVertical+1;

            else :
                countVertical=0;

        # Diagonal
        if col + i >= 0 and col + i < 7 and row + i >= 0 and row + i < 6:
            if board[row + i][col + i] == disk:
                countRightDiagonal = countRightDiagonal + 1;
            else:
                countRightDiagonal = 0;

        if col - i >= 0 and col - i < 7 and row + i >= 0 and row + i < 6:
            if board[row + i][col - i] == disk:
                countLeftDiagonal = countLeftDiagonal + 1;
            else:
                countLeftDiagonal = 0;
        # Horizontal
        if row + i >= 0 and row + i < 6:
            if board[row + i][col] == disk:
                countHorizontal = countHorizontal + 1;
            else:
                countHorizontal = 0;

        if countVertical==4 or countLeftDiagonal==4 or countRightDiagonal==4 or countHorizontal==4 :
            return disk
