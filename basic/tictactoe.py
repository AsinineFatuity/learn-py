#initializing and declaring variables
theBoard={
    'top-L':' ','top-M':' ','top-R':' ',
    'mid-L':' ','mid-M':' ','mid-R':' ',
    'low-L':' ','low-M':' ','low-R':' '
}
turn='X'
#initializing and declaring functions
def printBoard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])
    print('-+-+-')    
def changingTurn(current_turn):
    if current_turn=='X':
        current_turn='O'
    elif current_turn=='O':
        current_turn='X'
    return current_turn
def printWinner(current_turn):
    winner_turn=changingTurn(current_turn)
    print("Player "+winner_turn+" has won the game")
def continueGame(myBoard):
    for key,value in myBoard.items():
        if value==' ':
            return True
        else:
            return False
#the program continues unannounced,loop ten times so that one can have their last laugh announced
board_len=len(theBoard)
i=0
#the above grants flexibility on how I will handle the length should a player make a move on the same space twice

while continueGame(theBoard)==True:
    """
    check if the player has won the game after at least an initial move is made then no need to proceed with game
    by changing turns to the next player
    """
    if i>0:
        if((theBoard['top-L']==theBoard['top-M']==theBoard['top-R']!=' ')==True):
            printWinner(turn)
            break
        elif ((theBoard['top-L']==theBoard['mid-M']==theBoard['low-R']!=' ')==True):
            printWinner(turn)
            break
        elif ((theBoard['top-L']==theBoard['mid-L']==theBoard['low-L']!=' ')==True):
            printWinner(turn)
            break
        elif ((theBoard['top-R']==theBoard['mid-R']==theBoard['low-R']!=' ')==True):
            printWinner(turn)
            break
        elif ((theBoard['top-M']==theBoard['mid-M']==theBoard['low-M']!=' ')==True):
            printWinner(turn)
            break
        elif ((theBoard['mid-L']==theBoard['mid-M']==theBoard['mid-R']!=' ')==True):
            printWinner(turn)
            break
        elif ((theBoard['low-L']==theBoard['low-M']==theBoard['low-R']!=' ')==True):
            printWinner(turn)
            break
#safely proceed to change player turns
    print("Turn for "+turn+" Move on which space?")
    printBoard(theBoard)
    move=input()
#the following lines ensure that I don't make a move where move has already been made
#and also allow the players to still have the 9 chances by incrementing the length of the dictionary board
#should there be a duplicate
    if theBoard[move]!=' ':
        print("Move already made") 
        # print(board_len)
        # board_len+=1#so as to maintain the loop to range of 9 values in as much as the length changes
        # print(board_len)
        if turn=='X':
            turn='X'
        elif turn=='O':
            turn='O'   
    elif theBoard[move]==' ':
        theBoard[move]=turn 
        if turn=='X':
             turn='O' 
        else:
            turn='X'  
    i+=1 #ensures that at least I check for win after first move is made      
printBoard(theBoard)



