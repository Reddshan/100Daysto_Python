import random
from turtle import Turtle,Screen
import turtle as t

t.colormode(255)


def random_color():
    x=random.randint(0,255)
    y=random.randint(0,255)
    z=random.randint(0,255)
    colrtup=(x,y,z)
    return colrtup
def turtleobj(p_num):
    turt_obj_lst=[]
    counter=0
    counter1=0
    for i in range(0,p_num):
        obj1=Turtle(shape='turtle')
        obj1.color(random_color())
        obj1.penup()
        if i%2==0:
           obj1.setpos(-490,counter)
           counter=counter+50
        else:
          counter1 = counter1 - 50
          obj1.setpos(-490, counter1)


        turt_obj_lst.append(obj1)
    return turt_obj_lst

scr=Screen()
is_race=""
scr.setup(width=1000,height=1000)
player_number=int(scr.textinput("Number of Players","Enter the Number of Players :"))
winner_bet =int(scr.textinput("Bet Your winner",f"Enter Player Number who will be winner inputs(0-{player_number-1}):"))
if winner_bet:
    is_race=True
tur_lst=turtleobj(player_number)
t.colormode(1)
while is_race:
    for  i in range(0,len(tur_lst)):
        if tur_lst[i].xcor()>480:
            print(f"The Winner is turtle:{i} and its color is {tur_lst[i].color()}")
            is_race=False
            #print(player_number)
            if i==winner_bet:
                print("You won the race")
            else:
                print("You lost the race")
        rand_distance=random.randint(0,10)
        tur_lst[i].forward(rand_distance)

# timmy = Turtle(shape='turtle')
# timmy.color(random_color())
# timmy.penup()
# timmy.setpos(-490,0)

scr=Screen()
scr.exitonclick()

