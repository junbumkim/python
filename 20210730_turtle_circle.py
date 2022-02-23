
import turtle as t
t.shape("turtle")

t.bgcolor("black")
t.color("gold")
t.speed(0)

t.up()
t.goto(-200,0)
t.down()
n = 50
for x in range(n):
    t.circle(100)
    t.left(360-n)

t.up()
t.goto(200,0)
t.down()
for x in range(1500):
    t.forward(x)
    t.left(80)
