import turtle as t
import random
import json
def make_star(size,st_color):
    t.begin_fill()
    t.color(st_color)
    t.seth(110)
    for i in range(5):
        t.forward(size)
        t.left(144)
    t.end_fill()

def drawTree(length):
	if length < 1:
		return
	t.forward(length)
	t.right(45)
	drawTree(length * 0.7)
	t.left(45 * 2)
	drawTree(length * 0.7)
	t.right(45)
	t.backward(length)

def hh(color):
    t.pendown()
    t.color(color)
    t.pensize(1.4)
    drawTree(5)
    t.penup()


#color = ("red","orange","blue","green","white","yellow","indigo","pink")
color = ("red","orange","springgreen","palegreen","magenta","green","lawngreen","darkgreen","silver","forestgreen","palegreen","gold")

t.ht()
t.bgcolor("black")
home = [-150,280]
t.setpos(home[0],home[1])
t.speed(0)
line = 15
for y in range(1, line * 2, 2):
    k = y//3
    home[1] -= 30
    home[0] = -150
    t.sety(home[1])
    home[0] += 10 * (line*2-1-y-k//2)//2
    t.setx(home[0])
    for z in range(y+k):
        if y== 1 and z == 0 :
            t.setx(home[0]+20)
            make_star(50,"yellow")
            t.right(15)
            t.up()
        else:
            htm = random.choice(color)
            if 'green' in htm:
                hh(htm)
            else:
                hh('green')
                t.dot(7,htm)
        home[0] += 10
        t.setx(home[0])
home[0] = -150 + (line*2-line//3-1)*5
home[1] -= 10
t.setpos(home[0],home[1])
#나무 그리기
for i in range(1,line//2+2):
    home[1] -= 10
    t.setpos(-100,home[1])
    temp = 0
    for j in range(line//3):      
        temp += 10
        t.setx(home[0]+temp)
        t.dot(7,'saddlebrown')

#나는야 나는야 확인용
t.done()
