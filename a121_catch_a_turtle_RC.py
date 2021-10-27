#-----import statements-----
import turtle as trtl
import random as rand
t = trtl.Turtle()
t.shape("circle")
t.shapesize(10)
t.fillcolor("green")
xpos = 0
ypos = 0
t.penup()
t.speed(0)
score = 0

#-----game configuration----

def random_text():
  num1 = rand.randint(0,3)
  if num1 > 2.5:
    print("Wow!")
  elif num1 > 1.5:
    print("Great!")
  elif num1 > 0.5:
    print("Amazing!")
  else:
    print("Keep it up!")

def change_pos():
  global xpos
  global ypos
  xpos = rand.randint(-350,350)
  ypos = rand.randint(-350,350)
  t.goto (xpos, ypos)

def click(x, y):
  change_pos()



if t.onclick(click):
  change_pos()
  score = score + 1
  print("score",score)


#-----initialize turtle-----


#-----game functions--------


#-----events----------------
wn = trtl.Screen()
wn.mainloop()
