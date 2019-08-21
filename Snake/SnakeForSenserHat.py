from time import sleep
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED

sense = SenseHat()


xPosStartSnake = 3
yPosStartSnake = 3

B= [114, 57, 57]         #" " #BackGround
H= [255, 255, 0]            #"@" #Head Of Snake
T= [0, 255, 0]         #"O" #Tail Of Snake
F= [255, 0, 0]        #"F" #Food



def pushed_up(event):
    global Direction
    if Direction != "down":
        if event.action != ACTION_RELEASED:
            Direction = "up"

def pushed_down(event):
    global Direction
    if Direction != "up":
        if event.action != ACTION_RELEASED:
            Direction = "down"

def pushed_left(event):
    global Direction
    if Direction != "right":
        if event.action != ACTION_RELEASED:
            Direction = "left"

def pushed_right(event):
    global Direction
    if Direction != "left":
        if event.action != ACTION_RELEASED:
            Direction = "right"



def DisplayGrid(Grid):
    LEDGrid = []
    for y in range(0,len(Grid)):
        for x in range(0,len(Grid)):
            LEDGrid.append(Grid[y][x])

    sense.set_pixels(LEDGrid)

def Move(Direction, Grid, xPosSnake, yPosSnake):

    xFood = -1
    yFood = -1
    bStopLoop = True
    HeadValue = ""
    aGridxyPos = [] 
    Size = len(xPosSnake)
    if Direction == "right":
        if (xPosSnake[0]+1) > 7:
            xPosSnake.insert(0,0)
        else:
            xPosSnake.insert(0,xPosSnake[0]+1)
        yPosSnake.insert(0,yPosSnake[0])

    if Direction == "left":
        if (xPosSnake[0]-1)==-1:
            xPosSnake.insert(0,7)
        else:
            xPosSnake.insert(0,xPosSnake[0]-1)
        yPosSnake.insert(0,yPosSnake[0])

    if Direction == "up":
        xPosSnake.insert(0,xPosSnake[0])
        if (yPosSnake[0]-1==-1):
            yPosSnake.insert(0,7)
        else:
            yPosSnake.insert(0,yPosSnake[0]-1)

    if Direction == "down":
        
        xPosSnake.insert(0,xPosSnake[0])
        if (yPosSnake[0]+1)>7:
            yPosSnake.insert(0,0)
        else:
            yPosSnake.insert(0,yPosSnake[0]+1)

    HeadValue = Grid[yPosSnake[0]][xPosSnake[0]]
    #Update Grid
    Grid[yPosSnake[0]][xPosSnake[0]] = H
    for i in range(1,Size-1):
        Grid[yPosSnake[i]][xPosSnake[i]] = T

    Grid[yPosSnake[Size]][xPosSnake[Size]] = B

    
    if HeadValue != F:
        xPosSnake.pop(Size)
        yPosSnake.pop(Size)
    else:
        while bStopLoop:
            aBool = []
            xFood = random.randint(0,7)
            yFood = random.randint(0,7)
            bStopLoop = False
            if Grid[yFood][xFood] == B and Grid[yFood][xFood] != F:
                for i in range(0,Size-1):
                    if (xFood == xPosSnake[i]) and (yFood == yPosSnake[i]):
                        aBool.append(True)
                    else:
                        aBool.append(False)
                for i in range(0, len(aBool)):
                    if aBool[i]:
                        bStopLoop = True
                if bStopLoop == False:
                    Grid[yFood][xFood] = F
            else:
                bStopLoop = True


                
    if HeadValue == T:
        sense.show_message("Game Over", text_colour=[255, 0, 0])

        sense.clear()
        sys.exit(0)

        
        



    aGridxyPos.append(Grid)
    aGridxyPos.append(xPosSnake)
    aGridxyPos.append(yPosSnake)


    return aGridxyPos
    

Direction = "right"

#cords of snake
xPosSnake = [3,2,1]
yPosSnake = [3,3,3]

Grid = [[B,B,B,B,B,B,B,B],
        [B,B,B,B,B,B,F,B],
        [B,B,B,B,B,B,B,B],
        [B,B,B,B,B,B,B,B],
        [B,B,B,B,B,B,B,B],
        [B,B,B,B,B,B,B,B],
        [B,B,B,B,B,B,B,B],
        [B,B,B,B,B,B,B,B]]
#print ((Grid[2])[2:5])
#print (''.join(Grid[2]))

#(Grid[y])[x]

Grid[yPosStartSnake][xPosStartSnake] = H
Grid[yPosStartSnake][xPosStartSnake-1] = T
Grid[yPosStartSnake][xPosStartSnake-2] = T
DisplayGrid(Grid)




while True:




    aGridxyPos = Move(Direction, Grid, xPosSnake, yPosSnake)
    Grid = aGridxyPos[0]
    xPosSnake = aGridxyPos[1]
    yPosSnake = aGridxyPos[2]
    #DisplayGrid(Grid)
    #Direction = input("Direction: ")
    sense.stick.direction_up = pushed_up
    sense.stick.direction_down = pushed_down
    sense.stick.direction_left = pushed_left
    sense.stick.direction_right = pushed_right
    #sense.stick.direction_any = DisplayGrid(Grid)
    DisplayGrid(Grid)
    #print (str(event.action) + str(event.direction))
    
    # = sense.stick.wait_for_event()
    # = (event.direction)
    sleep(0.16)
    
