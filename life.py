import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

N = 100
alive = 255
dead = 0
life = [alive, dead]
chancesOfLife = [0.1, 0.9]

grid = np.random.choice(life, N*N, chancesOfLife).reshape(N, N)

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
    return [mat]

fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=50, save_count=50)
#ani.save('life.gif', writer='imagemagick', fps=60)
plt.show()
