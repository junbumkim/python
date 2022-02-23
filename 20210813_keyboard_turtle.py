#거북이를 움직여서 그림을 그릴수 있다

import turtle as t

def turn_right():
    t.setheading(0)
    t.forward(10)
def turn_left():
    t.setheading(180)
    t.forward(10)
def turn_up():
    t.setheading(90)
    t.forward(10)
def turn_down():
    t.setheading(270)
    t.forward(10)
def clear():
    t.clear()
def color():
    t.color("red")
def cc():
    t.color("blue")
t.shape("turtle")
t.speed(0)
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.listen()
t.onkeypress(clear,"c")
t.onkeypress(color,"r")
t.onkeypress(cc,"b")

