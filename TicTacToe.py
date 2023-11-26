
board = [' ' for x in range(10)]

def insertletter(letter, position):
    board[position] = letter 

def spaceIsFree(position):
    return board[position] == ' '

def printboard(board): 
    print( '    |   |')
    print('  ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print( '    |   |')
    print('-------------')
    print( '    |   |')
    print('  ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print( '    |   |')
    print('-------------')
    print( '    |   |')
    print('  ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print( '    |   |') 
def isWinner(bo , le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (
        bo[4] == le and bo[5] == le and bo[6] == le) or (
        bo[1] == le and bo[2] == le and bo[3] == le) or (
        bo[1] == le and bo[2] == le and bo[7] == le) or (
        bo[2] == le and bo[5] == le and bo[8] == le) or (
        bo[3] == le and bo[6] == le and bo[9] == le) or (
        bo[1] == le and bo[5] == le and bo[9] == le) or (
        bo[3] == le and bo[5] == le and bo[7] == le)
  
def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'x\' (1-9): ')
        #data validation
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertletter('x', move)
                else:
                    print('Sorry, tis space is occupied')    
            else:
                print("Please type a number within the range")        
        except:
            print('Please type a number')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x!=0] #generates a list of all the positions the computer can move into
    move = 0
    #check if there is a move the computer could win with
    #the x checks if there is a move the player could win with that the computer can block
    for let in ['o', 'x']: 
        for i in possibleMoves:
            boardCopy = board[:] #lists are mutuable thats why this could be done
            boardCopy[i]  = let
            if isWinner(boardCopy, let):
                move = i
                return move
    #there is no posistion the computer and player could win. move to an open corner         
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    #the center
    if 5 in possibleMoves:
        move = 5
        return move
    #the edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4 , 6, 8]:
            edgesOpen.append(i) 
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)       
    return move
              
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1: #there will always be a space at the beginning of the list
        return False
    else:
        return True 

def main():
    print('wlecome to Tic Tac Toe!!')
    printboard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'o')): #checks if the computer has won
            playerMove()
            printboard(board)
        else:
            print('sorry, o\'s won this time!')
            break

        if not(isWinner(board, 'x')): #checks if player  has won
            move = compMove()
            if move == 0: # if our computer move function was not able to come up with a move for some reason
                print('Tie game!')
            else:
                insertletter('o', move)
                print('Computer placed an \'0\' in position', move)
                printboard(board)                     
        else:
            print('x\'s won this time! Good job!')
            break    
    #if isBoardFull(board):
        #print('Tie Game')
main()        