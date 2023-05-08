playerO = 'O'
playerX = 'X'
# board for game
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


# printing the board
def printBoard(board):
    print("\n")
    print(board[1]+' |'+board[2]+' |'+board[3])
    print("---------")
    print(board[4]+' |'+board[5]+' |'+board[6])
    print("---------")
    print(board[7]+' |'+board[8]+' |'+board[9])
    print("\n")

# function that checks if board is full


def isFullBoard(board):
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

# checking for draw


def checkDraw(board):
    if isFullBoard(board) and checkWin(board, ' ') == False:
        return True
    return False

# check if one of the players is won


def checkWin(board, mark):
    return ((board[1] == board[2] and board[1] == board[3] and board[1] != mark) or
            (board[4] == board[5] and board[4] == board[6] and board[4] != mark) or
            (board[7] == board[8] and board[7] == board[9] and board[7] != mark) or
            (board[1] == board[4] and board[1] == board[7] and board[1] != mark) or
            (board[2] == board[5] and board[2] == board[8] and board[2] != mark) or
            (board[3] == board[6] and board[3] == board[9] and board[3] != mark) or
            (board[1] == board[5] and board[1] == board[9] and board[1] != mark) or
            (board[7] == board[5] and board[7] == board[3] and board[7] != mark))

# check if we can insert letter to the board.


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    return False

# function to insert letter into the board.


def playTurn(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        # after every move , checks if win or draw
        if (checkDraw(board) == True):
            print("Draw!")
        elif (checkWin(board, ' ') == True):
            if letter == 'X':
                print("player X is won!")
            else:
                print("player O is Won!")
            exit()

    else:
        # incase player try to insert letter where a place is taken.
        position = int(input("This position is invalid! Try again: "))
        playTurn(letter, position)

# player O action


def playerOMove():
    bestScore = 1000
    bestMove = 0
   # calculate every move recursive to check wich move is the best for 'O'
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = playerO
            score = minimax(board, True, playerX, playerO)
            board[key] = ' '
            if (score < bestScore):
                bestScore = score
                bestMove = key
    playTurn(playerO, bestMove)
    return

# function that checks if player with mark X or O is won


def playerXMove():
    bestScore = -1000
    bestMove = 0

    for key in board.keys():
        if (board[key] == ' '):
            board[key] = playerX
            score = minimax(board, False, playerX, playerO)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    playTurn(playerX, bestMove)
    return


def minimax(board, isMaximizing, player1, player2):
    if (checkWin(board, player1)):
        return 1
    elif (checkWin(board, player2)):
        return -1
    elif (checkDraw(board)):
        return 0

    if (isMaximizing):
        bestScore = -1000
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player1
                score = minimax(board, False, player1, player2)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore
# minimizing the result
    else:
        bestScore = 1000
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player2
                score = minimax(board, True, player1, player2)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


firstCase = {1: 'X', 2: ' ', 3: ' ',
             4: ' ', 5: 'O', 6: ' ',
             7: ' ', 8: 'X', 9: ' '}
secoundCase = {1: ' ', 2: ' ', 3: 'X',
               4: ' ', 5: 'X', 6: ' ',
               7: 'O', 8: ' ', 9: ' '}

choice = input(
    "\nEnter the case you want to play? \n1 for first case , 2 for secound case: ")
if (choice == '1'):
    board = firstCase
elif (choice == '2'):
    board = secoundCase
printBoard(board)
while not checkWin(board, ' ') and not checkDraw(board):
    playerOMove()
    playerXMove()
