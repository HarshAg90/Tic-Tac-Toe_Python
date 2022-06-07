board=['-','-','-','-','-','-','-','-','-']

def clear_board():
  for i in range(len(board)):
    board[i]='-'

def print_board(): #printing board

  print(board[0],'|',board[1],'|',board[2])

  print(board[3],'|',board[4],'|',board[5])

  print(board[6],'|',board[7],'|',board[8])


def usermove(): #usr move interpreter

  move = input('enter ur move: (0-9)')

  if move.isdigit():
    move=int(move)
    if move>=0 and move<9:
      if board[move]!='-':
        print('space aquired')
        return usermove()

      else:
        return move

    else:
      print('invalid space')
      return usermove()
  else:
    print('please enter an integer')
    return usermove()


def randomshit(li): #STARING comp move 

  import random
  l=len(li)
  return li[random.randrange(0,l)]

def posm():
  possible_move=[]

  for i in range(len(board)): #to check for empty spaces
    if board[i]=='-':
      possible_move.append(i)
  return possible_move
def hackermove(): #computer logical move

  move =-1
  possiblemove=[]

  for i in range(len(board)): #to check for empty spaces
    if board[i]=='-':
      possiblemove.append(i)

  for l in ('O','X'): #to check where any one is winning
    for j in possiblemove:
      hackerB=board[:]
      hackerB[j]=l
      if iswinning(l,hackerB)==True:
        return j
  if 4 in possiblemove:
    return 4
  corner=[]
  for k in [0,2,6,8]: #when in begaining of game
    if k in possiblemove:
      corner.append(k)
  if len(corner)>1:
    return randomshit(corner)
  return move


def iswinning(per,board1): #per=(X/O),board1 is board t use

  if (board1[0]== per and board1[3]==per and board1[6]==per):
    return True

  elif (board1[7]==per and board1[1]==per and board1[4]==per):
    return True

  elif (board1[8]==per and board1[5]==per and board1[2]==per):
    return True

  elif (board1[0]==per and board1[1]==per and board1[2]==per):
    return True

  elif (board1[3]==per and board1[5]==per and board1[4]==per):
    return True

  elif (board1[7]==per and board1[8]==per and board1[6]==per):
    return True

  elif (board1[4]==per and board1[8]==per and board1[0]==per):
    return True

  elif (board1[2]==per and board1[4]==per and board1[6]==per):
    return True

  else:
    return False


def insertingmove(mo,yo): #to insert move in board
  board[mo]=yo


def main(): #to make all things run syatematicaly
  print_board()
  
  a=usermove()
  insertingmove(a,'X')
  if iswinning('X',board)==True:
    print_board()
    q=input('congrats, u won, great work!! press y to replay and x to end:')
    if q=='y':
      clear_board()
      print('Here u go again:- \n your are using "X"')
      main()
    else:
      print('bye')

  if hackermove()==-1:
    b=randomshit(posm())
  else:
    b=hackermove()
  insertingmove(b,'O')
  if iswinning('O',board)==True:
    print_board()
    q=input('O won, better luck next time! press y to replay and x to end: ')
    if q=='y':
      clear_board()
      print('Here u go again:- \n your are using "X"')
      main()
    else:
      print('bye')
  
  if len(posm())==1:
    print('Draw!!')
    print_board()

  else: #if no one is winning
    main()

print("HELLO, Welcome to Tic-Tac-Toe\nyou are using 'X'")

main() #starting program