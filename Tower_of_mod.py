#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63
floor = 0
tile = 0
tile_two = 0
# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  painter.color("black")
  y = y + 5 # location of next floor
  floor = floor + 1
  rem = floor % 9
  if (rem > 2):
    painter.color("green")
  if (rem > 5):
    painter.color("blue")
  
  #draw the floor
  painter.pendown()
  painter.forward(50)
  remain = floor % 21
  if remain < 1:
    x = x + 50
    y = -150

 

wn = trtl.Screen()
wn.mainloop()