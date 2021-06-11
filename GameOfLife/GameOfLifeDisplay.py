from GameOfLife import GameOfLifeGrid
import numpy as np
import time
import os

#define
res_x = 120
res_y = 40
T = 200
fps = 120


starting_grid = [[1,1,0,1],
                 [1,0,0,1],
                 [1,1,1,1],
                 [1,0,0,1]]
				 
starting_grid = np.random.randint(0, 2, (res_y, res_x))


def Display(Grid, ExtraString = "",fps = 4):
    sdisplay = ""
    for a in range(len(Grid)):
        for b in range(len(Grid[0])):
            if Grid[a][b]:
                sdisplay += "X"
            else:
                sdisplay += "."
        sdisplay += "\n"
		
    sdisplay += ExtraString
	
    os.system('cls' if os.name == 'nt' else 'clear')
    print(sdisplay)
    time.sleep(1/fps)

def DisplayGameOfLife(T = 100, fps = 5):
    Grid = GameOfLifeGrid()
    Grid.current_grid = starting_grid
    
    Start_Time = time.time()
    Display(starting_grid, "t = 0")
    for t in range(T):
        Grid.next_grid()
        Display(Grid.current_grid, ExtraString = "t= "+str(t), fps =fps)
    
    Time_Taken = time.time() - Start_Time
    print("Time_Taken = " + str(Time_Taken) + ", FPS = " + str(T/Time_Taken))
	
if __name__ == "__main__":
    DisplayGameOfLife(T = T, fps = fps)
	