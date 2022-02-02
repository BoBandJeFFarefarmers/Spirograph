import turtle
 
t = turtle.Turtle()

t.speed(0)
t.color('magenta')
t.shape("turtle")
for c in range(72):
   t.forward(50)
   t.right(45)
   t.forward(50)
   t.right(45)
   t.forward(50)
   t.right(45)
   t.forward(50)
   t.right(45)
   t.forward(50)
   t.right(45)
   t.forward(50)
   t.right(45)
   t.forward(50)
   t.right(45)
   t.forward(50)
   t.right(50)
   t.speed(0)
t.penup()
t.goto(-125,-125)
t.pendown()
for c in range(113):
  for c in ['crimson', 'lime', 'yellow', 'blue']:
    t.color(c)
    t.forward(250)
    t.left(89.8)

