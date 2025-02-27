print('\33c')
import turtle

def draw_grid(grid):
        # draw 9 squares
        # for each row in grid
            #for each column in each row
                #draw either a cross or circle
    return
        #0 #1 #2
grid = [[0,0,0], #0
        [0,0,0], #1
        [0,0,0]] #2
print(grid)
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
    print(grid)
    turncount = turncount + 1
