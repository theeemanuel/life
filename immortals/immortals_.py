import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import colors

N = 100
immortal = 2
alive = 1
dead = 0
life = [immortal, alive, dead]
chancesOfLife = 0.3
chancesOfImmortality = 0.01
p = [chancesOfImmortality, chancesOfLife, 1-(chancesOfLife+chancesOfImmortality)]

grid = np.random.choice(life, N*N, p).reshape(N, N)

def update(data):
    global grid
    population = 0
    newGrid = grid.copy()

    for i in range (N):
        for j in range(N):
            if newGrid[i][j] == 2:
                population += 1
    
    for i in range(N):
        for j in range(N):
            lifeVolume = (grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
                   grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
                   grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
                   grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])
            if population == 0:
                total = lifeVolume
            else:
                total = lifeVolume/(immortal*population)
          
            if grid[i, j]  == immortal:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = alive
            if grid[i, j]  == alive:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = dead
                elif total == 2:
                    newGrid[i, j] = immortal
            elif grid[i, j]  == dead:
                if total == 3:
                    newGrid[i, j] = alive
                elif total == 4:
                    newGrid[i, j] = immortal
            
    mat.set_data(newGrid)
    grid = newGrid
    print("Simulating Generation ",data)
    return [mat]

colormap = colors.ListedColormap(["black", "cyan", "blue"])
fig, ax = plt.subplots()
mat = plt.imshow(grid, cmap=colormap)
ani = animation.FuncAnimation(fig, update, interval=50, save_count=50)
#ani.save('immortals.gif', writer='imagemagick', fps=60)
plt.show()
