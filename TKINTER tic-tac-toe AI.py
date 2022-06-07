from tkinter import *
from tkinter import messagebox
window=Tk()

window.title('Tic-Tac-Toe AI')
window.geometry('400x200')

lbl=Label(window,text="Tic-tac-toe Game",font=('Helvetica','15'))
lbl.grid(row=0,column=0)
lbl=Label(window,text="You are: X ",font=('Helvetica','10'))
lbl.grid(row=1,column=0)
lbl=Label(window,text="Computer is: O",font=('Helvetica','10'))
lbl.grid(row=2,column=0)

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

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
    if board[i]==' ':
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



turn = 1
def clicked1():
    global turn
    if btn1["text"]==" ":   #For getting the text of a button
        if turn==1:
            turn =2;
            btn1["text"]="X"
            btn1.config(state="disabled")
        elif turn==2:
            turn=1;
            btn1["text"]="O"
            btn1.config(state="disabled")
        check();
def clicked2():
    global turn
    if btn2["text"]==" ":
        if turn==1:
            turn =2;
            btn2["text"]="X"
            btn2.config(state="disabled")
        elif turn==2:
            turn=1;
            btn2["text"]="O"
            btn2.config(state="disabled")
        check();
def clicked3():
    global turn
    if btn3["text"]==" ":
        if turn==1:
            turn =2;
            btn3["text"]="X"
            btn3.config(state="disabled")
        elif turn==2:
            turn=1;
            btn3["text"]="O"
            btn3.config(state="disabled")
        check();
def clicked4():
    global turn
    if btn4["text"]==" ":
        if turn==1:
            turn =2;
            btn4["text"]="X"
            btn4.config(state="disabled")
        elif turn==2:
            turn=1;
            btn4["text"]="O"
            btn4.config(state="disabled")
        check();
def clicked5():
    global turn
    if btn5["text"]==" ":
        if turn==1:
            turn =2;
            btn5["text"]="X"
            btn5.config(state="disabled")
        elif turn==2:
            turn=1;
            btn5["text"]="O"
            btn5.config(state="disabled")
        check();
def clicked6():
    global turn
    if btn6["text"]==" ":
        if turn==1:
            turn =2;
            btn6["text"]="X"
            btn6.config(state="disabled")
        elif turn==2:
            turn=1;
            btn6["text"]="O"
            btn6.config(state="disabled")
        check();
def clicked7():
    global turn
    if btn7["text"]==" ":
        if turn==1:
            turn =2;
            btn7["text"]="X"
            btn7.config(state="disabled")
        elif turn==2:
            turn=1;
            btn7["text"]="O"
            btn7.config(state="disabled")
        check();
def clicked8():
    global turn
    if btn8["text"]==" ":
        if turn==1:
            turn =2;
            btn8["text"]="X"
            btn8.config(state="disabled")
        elif turn==2:
            turn=1;
            btn8["text"]="O"
            btn8.config(state="disabled")
        check();
def clicked9():
    global turn
    if btn9["text"]==" ":
        if turn==1:
            turn =2;
            btn9["text"]="X"
            btn9.config(state="disabled")
        elif turn==2:
            turn=1;
            btn9["text"]="O"
            btn9.config(state="disabled")
        check();

def btnchng(key):
    if key=='btn1':
        clicked1()
    if key=='btn2':
        clicked2()
    if key=='btn3':
        clicked3()
    if key=='btn4':
        clicked4()
    if key=='btn5':
        clicked5()
    if key=='btn6':
        clicked6()
    if key=='btn7':
        clicked7()
    if key=='btn8':
        clicked8()
    if key=='btn9':
        clicked9()
flag=1;
def check():
    global flag;
    b1 = btn1["text"];
    b2 = btn2["text"];
    b3 = btn3["text"];
    b4 = btn4["text"];
    b5 = btn5["text"];
    b6 = btn6["text"];
    b7 = btn7["text"];
    b8 = btn8["text"];
    b9 = btn9["text"];
    flag=flag+1;
    if b1==b2 and b1==b3 and b1=="O" or b1==b2 and b1==b3 and b1=="X":
        win(btn1["text"])
    if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
        win(btn4["text"]);
    if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
        win(btn7["text"]);
    if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
        win(btn1["text"]);
    if b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X":
        win(btn2["text"]);
    if b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X":
        win(btn3["text"]);
    if b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X":
        win(btn1["text"]);
    if b7==b5 and b7==b3 and b7=="O" or b7==b5 and b7==b3 and b7=="X":
        win(btn7["text"]);
    if flag ==10:
        messagebox.showinfo('Draw',"oh shit!! Here we go again DRAW")
        window.destroy()


def main(key,move): #to make all things run syatematicaly
    btnchng(key)
    board[move-1]='X'
    if hackermove()==-1:
        b=randomshit(posm())
    else:
        b=hackermove()
    board[b]='O'
    btnchng('btn'+str(b+1))




#tkinter

def win(player):
    messagebox.showinfo("Congratulations", "Game complete " +player + " won ")
    window.destroy()  # is used to close the program


btn1 = Button(window, text=' ',bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'), command=lambda:main('btn1',1))
btn1.grid(column=1, row=1)
btn2 = Button(window, text=' ',bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'), command=lambda:main('btn2',2))
btn2.grid(column=2, row=1)
btn3 = Button(window, text=' ',bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:main('btn3',3))
btn3.grid(column=3, row=1)
btn4 = Button(window, text=' ',bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:main('btn4',4))
btn4.grid(column=1, row=2)
btn5 = Button(window, text=' ',bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:main('btn5',5))
btn5.grid(column=2, row=2)
btn6 = Button(window, text=' ',bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:main('btn6',6))
btn6.grid(column=3, row=2)
btn7 = Button(window, text=' ',bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:main('btn7',7))
btn7.grid(column=1, row=3)
btn8 = Button(window, text=' ',bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:main('btn8',8))
btn8.grid(column=2, row=3)
btn9 = Button(window, text=' ',bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:main('btn9',9))
btn9.grid(column=3, row=3)

window.mainloop()

   