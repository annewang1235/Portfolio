from turtle import *
import math

# Name your Turtle.
t = Turtle()
#Anne = Turtle()

person = input('Enter your name: ')
print('Hello', person)
col = input('What is your favorite color: ')
print('Awesome. The shapes will be in color',col )
num = input('Enter a number: ')
print('Now your shape will have' , num , 'sides.')

# type cast integer int(num)
# Set Up your screen and starting position.
# setup(500,300)
# x_pos = -250
# y_pos = -150
 #t.setposition(x_pos, y_pos)

### Write your code below:



bgcolor("pink")

t.color(col)


t.speed(5)
#Anne.speed(7)
int(num)
for i in range(50): #i is a list from [0,119] and it'll run 120 times
    for j in range(int(num)): #within this loop, j is a list from [0,4]
        t.forward(i) #the turtle will
        t.right(360/int(num))
    t.right(3)

# Anne.setposition(120, 120)
#
# chocolate = input('What is your second favorite color: ')
# print("Great. Triangles will be in the color", chocolate)
# Anne.color(chocolate)
#
# for i in range(120): #i is a list from [0,119] and it'll run 120 times
#     for j in range(3): #within this loop, j is a list from [0,4]
#         Anne.forward(i)
#         Anne.right(360/3)
#     Anne.right(3)





# Close window on click.
exitonclick()
