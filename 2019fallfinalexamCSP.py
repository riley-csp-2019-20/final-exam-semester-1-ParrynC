#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Parryn Cornell
#
#12/18/2019
#


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl

#create turtle
sketch = trtl.Turtle()
sketch.pensize(5)
#movement functions
def sketchup():
    sketch.setheading(90)
    sketch.forward(10)
   

def sketchdown():
    sketch.setheading(270)
    sketch.forward(10)
   

def sketchleft():
    sketch.setheading(180)
    sketch.forward(10)
   

def sketchright():
    sketch.setheading(0)
    sketch.forward(10)

wn = trtl.Screen()

#color/drawing functions
letter_list = ["O","P","U","I"]

#pen 
def check_o():
  if ("O"):
    sketch.pensize(20)
def check_p():
  if ("P"):
    sketch.pensize(5)

def check_u():
  if ("U"):
    sketch.penup()
def check_i():
  if ("I"):
    sketch.pendown()

#colors
def check_r():
  if ("R"):
    sketch.pencolor("red")
def check_b():
  if ("B"):
    sketch.pencolor("blue")
def check_g():
  if ("G"):
    sketch.pencolor("green")
def check_q():
  if ("Q"):
    sketch.pencolor("black")

#Delt
def check_space():
  if ("space"):
    sketch.clear()


#create screen
wn = trtl.Screen()


#bind to keypresses
wn.onkeypress(check_o, "o")
wn.onkeypress(check_p, "p")
wn.onkeypress(check_u, "u")
wn.onkeypress(check_i, "i")

wn.onkeypress(check_r, "r")
wn.onkeypress(check_b, "b")
wn.onkeypress(check_g, "g")
wn.onkeypress(check_q, "q")

wn.onkeypress(sketchup, "Up")
wn.onkeypress(sketchdown, "Down")
wn.onkeypress(sketchleft, "Left")
wn.onkeypress(sketchright, "Right")

wn.onkeypress(check_space, "space")



#listen
wn.listen()


#mainloop
wn.listen()
wn.mainloop()