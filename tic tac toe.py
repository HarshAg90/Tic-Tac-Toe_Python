board=['-','-','-','-','-','-','-','-','-']
def disp_board():
  print(board[0] + ' | ' + board[1] + ' | ' + board[2])
  print(board[3] + ' | ' + board[4] + ' | ' + board[5])
  print(board[6] + ' | ' + board[7] + ' | ' + board[8])
def handle_function():
  pos,move=input().split()
  board[int(pos)-1]=move
def continue_or_won():
  if board[0]==board[3] and board[3]==board[6] and board[0]!='-':
    print(board[0],'won')
  elif board[7]==board[1] and board[1]==board[4] and board[1]!='-':
    print(board[7],'won')
  elif board[8]==board[5] and board[5]==board[2] and board[2]!='-':
    print(board[8],'won')
  elif board[0]==board[1] and board[1]==board[2] and board[2]!='-':
    print(board[0],'won')
  elif board[3]==board[4] and board[4]==board[5] and board[4]!='-':
    print(board[3],'won')
  elif board[6]==board[7] and board[8]==board[7] and board[6]!='-':
    print(board[6],'won')
  elif board[0]==board[4] and board[0]==board[8] and board[0]!='-':
    print(board[0],'won')
  elif board[2]==board[4] and board[4]==board[6] and board[6]!='-':
    print(board[2],'won')
  else:
    game()
def game():
  disp_board()
  print('enter position then space then "x" or "o"')
  handle_function() #for input
  continue_or_won() #recheck board
  a=int(input('press "1" to end and "0" to play again'))
  if a==0:
    game()
game()
