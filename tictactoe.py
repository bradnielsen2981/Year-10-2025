print('\33c')
import turtle
import sys
turtleobject = turtle.Turtle()
turtle.tracer(0,0)
def draw_square(side):
    for it in range(4):
        turtleobject.forward(side)
        turtleobject.right(90)
def draw_grid(grid):
    turtleobject.pensize(2)
    for row in range(3): #row => 0, 1, 2
        for col in range(3): #col => 0, 1, 2
            value = grid[row][col]
            x = col*100-200
            y = -row*100+200
            turtleobject.penup()
            turtleobject.goto(x, y)
            turtleobject.pendown()
            draw_square(100)
            if value == 'nought':
                turtleobject.penup()
                turtleobject.goto(x+50, y-100)
                turtleobject.pendown()
                turtleobject.circle(50)
    turtle.update()
    return

grid = [[0,0,0], #0
        [0,0,0], #1
        [0,0,0]] #2
draw_grid(grid)

turns = ['cross','nought']

gameover = False
turncount = 0
while not gameover and turncount < 9:
    i = turncount%2 #retrict the variable to a range one less than the number
    turn = turns[i]
    print("Now it is turn: ", turns[i])
    row = int(input("Which row? 1-3 : ")) - 1
    column = int(input("Which column? 1-3 : ")) - 1
    if row < 0 or column < 0:
        break
    grid[row][column] = turn
    draw_grid(grid)
    turncount = turncount + 1
