import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import colors

N = 100
alive = 1
dead = 0
life = [alive, dead]
colormap = colors.ListedColormap(["black","cyan"])
chancesOfLife = 0.11
p = [chancesOfLife, 1-chancesOfLife]

grid = np.random.choice(life, N*N, p).reshape(N, N)

for i in range(N):
    for j in range(N):
        grid[i][j] = dead
grid[50][50] = alive
grid[50][50+1] = alive
grid[50+1][50] = alive
grid[50+1][50-1] = alive
grid[50+2][50] = alive

def gridView(data):
    mat.set_data(grid)
    return [mat]

def update(data):
    global grid 
    newGrid = grid.copy()
    
    for i in range(N):
        for j in range(N):
          lifeVolume = (grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
                   grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
                   grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
                   grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])
          total = lifeVolume/alive
          
          if grid[i, j]  == alive:
              if (total < 2) or (total > 3):
                  newGrid[i, j] = dead
          else:
              if total == 3:
                  newGrid[i, j] = alive
    
    mat.set_data(newGrid)
    grid = newGrid
    print("Simulating Generation ",data)
    return [mat]

fig, ax = plt.subplots()
mat = plt.imshow(grid, cmap=colormap)
ani = animation.FuncAnimation(fig, update, interval=50, save_count=50)
#ani.save('R-Pentomino.gif', writer='imagemagick', fps=60)
plt.show()
