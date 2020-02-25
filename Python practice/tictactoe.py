theboard={'T-L':' ','T-M':' ','T-R':' ','M-L':' ','M-M':' ','M-R':' ','L-L':' ','L-M':' ','L-R':' '}
def printBoard(board):
    print(board['T-L']+ '|' +board['T-M']+ '|' +board['T-R'])
    print('-+-+-')
    print(board['M-L']+ '|' +board['M-M']+ '|' +board['M-R'])
    print('-+-+-')
    print(board['L-L']+ '|' +board['L-M']+ '|' +board['L-R'])
turn= 'X'
for i in range(9):
    printBoard(theboard)
    print(' Turn for '+ turn + '.move in which space?')
    move=input()
    theboard[move]= turn
    if turn== 'X':
        turn='0'
    else:
        turn='X'
    if (theboard['T-L']==theboard['T-M']==theboard['T-R']==theboard[move]):
        print('The player has won')
        break
    elif(theboard['M-L']==theboard['M-M']==theboard['M-R']==theboard[move]):
        print('The player has won')
        break
    elif(theboard['L-L']==theboard['L-M']==theboard['L-R']==theboard[move]):
        print('The player has won')
        break
    elif(theboard['T-L']==theboard['M-L']==theboard['L-L']==theboard[move]):
        print('The player has won')
        break
    elif(theboard['T-M']==theboard['M-M']==theboard['L-M']==theboard[move]):
        print('The player has won')
        break
    elif(theboard['T-R']==theboard['M-R']==theboard['L-R']==theboard[move]):
        print('The player has won')
        break
    elif(theboard['T-L']==theboard['M-M']==theboard['L-R']==theboard[move]):
        print('The player has won')
        break
    elif(theboard['T-R']==theboard['M-M']==theboard['L-L']==theboard[move]):
        print('The player has won')
        break
    else:
        continue
printBoard(theboard)
