import AuxilleryFunctions as af

board = af.newBoard();
gameOver = False;
turn = 0;
print("########## 4 IN A ROW - created by Asaf Dov ###########")
input("\nPress Enter key to start game")

while not gameOver:
    af.printBoard(board)
    if turn==0:
        try:
            col = int(input("\nPlayer 1 (0-6)  X:\n"))
        except ValueError:
            print('Wrong input - put number between 0-6')
            continue;
        if af.isLegalInput(board, col):
            row = af.getAvailableRow(board,col);
            af.drop(board, row, col, 1);
            turn = 1;
            win =af.didIWin(board,row,col, 1 );
        else:
            print('Wrong input - put number between 0-6')
            continue;

    else:
        try:
            col = int(input("\nPlayer 2 (0-6)  O:\n"))
        except ValueError:
            print('Wrong input - put number between 0-6')
            continue;

        if af.isLegalInput(board, col):
            row = af.getAvailableRow(board,col)
            af.drop(board, row, col, 2);
            win =af.didIWin(board, row, col, 2);
            turn = 0;
        else:
            print('Wrong input - put number between 0-6')
            continue;

    if win is not None:
        print('Player ' + str(win) + ' is the WINNER\n\n' );
        restart = input('Start a new game? answer y/n');
        if (restart !='y'):
            gameOver = True;
        else:
            board = af.newBoard();
            turn = 0;






