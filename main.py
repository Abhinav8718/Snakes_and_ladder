import tkinter as tk
from PIL import ImageTk, Image
import random

def start_game():
   
   global b1,b2

   b1.place(x=900,y=200)
   b2.place(x=900,y=400)
   
   im=Image.open("dice.jpg")
   im=im.resize((65,65))
   im=ImageTk.PhotoImage(im)
   b3=tk.Button(root,image=im,height=95,width=95)
   b3.place(x=700,y=300)
   
   b4=tk.Button(root,text="End Game",height=3,width=20,fg="black",bg="Yellow",font='Calibri',command=root.destroy)
   b4.place(x=900,y=50)
def reset_tokens():
   global player_1,player_2
   global pos1,pos2
   player_1.place(x=0,y=600)
   player_2.place(x=44,y=600)

   pos1=0
   pos2=0

def load_dice_images():
   global Dice 
   names=["1.png","2.png","3.gif","4.gif","5.gif","6.gif"]
   for nam  in names:
      im=Image.open(nam)
      im=im.resize((90,90))
      im=ImageTk.PhotoImage(im)
      Dice.append(im)

def check_ladder(turn):
   global pos1,pos2
   global ladder
   
   f=0
   if turn==1:
      if pos1 in ladder:
         pos1= ladder[pos1]
         f=1
   else:
      if pos2 in ladder:
         pos2 =ladder[pos2]  
         f=1    
   return f


def check_snake(turn):
   global pos1,pos2

   if turn==1:
      if pos1 in snake:
         pos1=snake[pos1]
   else:
      if pos2 in snake:
         pos2=snake[pos2]



def roll_dice():
   global Dice 
   global turn
   global pos1,pos2
   global b1,b2
   r = random.randint(1,6)
   b3=tk.Button(root,image=Dice[r-1],height=100,width=100)
   b3.place(x=700,y=300)

   if turn ==1:
      if(pos1+r)<=100:
         pos1=pos1+r
      lad=check_ladder(turn)
      check_snake(turn)
      move_coin(turn,pos1)
      if r!=6 and lad!=1:
         turn=2
         b1.configure(state='disabled')
         b2.configure(state='normal')
   else:
      if(pos2+r)<=100:
       pos2=pos2+r
      move_coin(turn,pos2)
      lad=check_ladder(turn)
      check_snake(turn)
      if r!=6 and lad!=1:
       turn=1
       b2.configure(state='disabled')
       b1.configure(state='normal')
   
   is_winner()
   move_coin(r)

def is_winner():
   global pos1,pos2

   if pos1==100:
      msg="Player-1 wins!"
      Lab=tk.Label(root,text=msg,height=2,width=20,bg='red',font='Calibri')
      Lab.place(x=300,y=300)
      reset_tokens()
   elif pos2==100:
      msg="Player-2 wins!"
      Lab=tk.Label(root,text=msg,height=2,width=20,bg='red',font='Calibri')
      Lab.place(x=300,y=300)
      reset_tokens()  

def move_coin(turn,r):
   global player_1,player_2
   global index

   if turn==1:
     player_1.place(x=index[r][0],y=index[r][1])
   else:
      player_2.place(x=index[r][0],y=index[r][1])


def get_index():
   global player_1,player_2
   Num=[
    100, 99, 98, 97, 96, 95, 94, 93, 92, 91,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    80, 79, 78, 77, 76, 75, 74, 73, 72, 71,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    60, 59, 58, 57, 56, 55, 54, 53, 52, 51,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10

   ]
   player_1.place(x=40,y=30)
   player_2.place(x=100,y=30)
   row=30
   i=0
   for x in range(1,11):
      col =40
      for y in range(1,11):
         index[Num[i]]=(col,row)
         col = col+57
         i=i+1
      row = row+57
   print(index) 

Dice=[]
index={}

pos1=None
pos2=None

ladder={4:56,12:50,14:55,22:58,41:79,54:88}
snake={96:42,94:71,75:32,48:16,28:10}


root = tk.Tk()
root.geometry("1200x800")
root.title("Snake and Ladder Game")

F1= tk.Frame(root,width=1200,height=800,relief="raised")
F1.place(x=0,y=0)

img1 = ImageTk.PhotoImage(Image.open("snake.gif"))
Lab=tk.Label(F1,image=img1)
Lab.place(x=0,y=0)

b1 = tk.Button(root,text="Player-1",height=3,width=20,fg="black",bg="red",font='Calibri',command=roll_dice)
b2 = tk.Button(root,text="Player-2",height=3,width=20,fg="black",bg="blue",font='Calibri',command=roll_dice)

player_1 =tk.Canvas(root,width=40,height=40)
player_1.create_oval(10,10,40,40,fill='red')


player_2 =tk.Canvas(root,width=40,height=40)
player_2.create_oval(10,10,40,40,fill='blue')

turn = 1



reset_tokens()
get_index()
load_dice_images()
start_game()
root.mainloop()