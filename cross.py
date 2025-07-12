# from turtle import *
# from random import randint

#функція старт - переміщення в координату
def start(x, y):
  penup()
  goto(x, y)
  pendown()
  
###############################
def field(col):
    xStart,yStart = -150,50
    size = 100
    x,y = xStart, yStart
    for i in range(3):
        for j in range(3):
            start(x,y)
            square(size,10,col)
            x += size
        x = xStart
        y -= size
       
def draw_cross(x,y,col):
    size = 100
    start(x,y)
    color(col)
    width(10)
    setheading(45)
    fd(1.4*size)
    start(x+size, y)
    setheading(135)
    fd(1.4*size)
def draw_dot(x,y,col):
    start( x+size//2, y)
    setheading(0)
    color(col)
    circle( size//2)
   
def move_player(player, col):
    cell = int(input("Введіть номер клітинки від 1 до 9"))
    while playing_field[cell]!=-1:
        print("Клітинки вже зайнята!")
        cell = int(input("Введіть номер клітинки від 1 до 9"))
    x = x_cor[cell]
    y = y_cor[cell]
    start(x,y)
    playing_field[cell] = player
    color(col)
    if player == 1:
        draw_cross(x,y,col)
    else:
        draw_dot(x,y,col)
       

def check_win():
    # 1 = 2 = 3
    if playing_field[1] == playing_field[2] == playing_field[3] :
        return playing_field[1],1,0
    # 4 = 5 = 6
    if playing_field[4] == playing_field[5] == playing_field[6] :
        return playing_field[4],5,0
    # 7 = 8 = 9
    if playing_field[7] == playing_field[8] == playing_field[9] :
        return playing_field[7],7,0
    # 1 = 4 = 7
    if playing_field[1] == playing_field[4] == playing_field[7] :
        return playing_field[1],1,270
    # 2 = 5 = 8
    if playing_field[2] == playing_field[5] == playing_field[8] :
        return playing_field[2],2,270
    # 3 = 6 = 9
    if playing_field[3] == playing_field[6] == playing_field[9] :
        return playing_field[3],3,270
    # 1 = 5 = 9
    if playing_field[1] == playing_field[5] == playing_field[9] :
        return playing_field[1],1,315
    # 3 = 5 = 7
    if playing_field[3] == playing_field[5] == playing_field[7] :
        return playing_field[3],3,225


    return -1  # Ніхто не виграв

def crossOut(cell,h,who):
    x = x_cor[cell]
    y = y_cor[cell]
    if h == 0:
        y += size//2
        s= size*3
    elif h == 270:
        x+= size//2
        s = size*3
    else:
        y += size
        s =size*1.4*3
    if who != "нічія":
        start(x,y)
        setheading(h)
        color("green")
        width(7)
        fd(s)
    start(0,0)
    write(f"Виграв - {who}", font=("Arial",20,"bold"))

def check_no_one_won():
    if -1 in playing_field:
        return False
    else:
        return True
