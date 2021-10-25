#include<stdio.h>
#include<windows.h>
#include<stdlib.h>
#define M 48
#define N 70

void set_cursor(bool visible)
{
    CONSOLE_CURSOR_INFO info;
    info.dwSize = 100;
    info.bVisible = visible;
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &info);
}

void SetColor(int ForgC)
{
     WORD wColor;
     //This handle is needed to get the current background attribute

     HANDLE hStdOut = GetStdHandle(STD_OUTPUT_HANDLE);
     CONSOLE_SCREEN_BUFFER_INFO csbi;
     //csbi is used for wAttributes word

     if(GetConsoleScreenBufferInfo(hStdOut, &csbi))
     {
          //To mask out all but the background attribute, and to add the color
          wColor = (csbi.wAttributes & 0xF0) + (ForgC & 0x0F);
          SetConsoleTextAttribute(hStdOut, wColor);
     }
     return;
}

int evolution(int grid[N][N])
{
	int i, j, lifeVolume, newGrid[N][N];
	for (i=0; i<M; i++)
	{
		for (j=0; j<N; j++)
		{
			newGrid[i][j] = grid[i][j];
		}
	}
	
	for (i=0; i<M; i++)
	{
		for (j=0; j<N; j++)
		{
			lifeVolume = (grid[i][(j-1)%N] + grid[i][(j+1)%N] + 
                   grid[(i-1)%M][j] + grid[(i+1)%M][j] + 
                   grid[(i-1)%M][(j-1)%N] + grid[(i-1)%M][(j+1)%N] + 
                   grid[(i+1)%M][(j-1)%N] + grid[(i+1)%M][(j+1)%N]);
            
            if (grid[i][j] == 1)
            {
            	if (lifeVolume<2 || lifeVolume>3)
            		newGrid[i][j] = 0;
			}
			else
			{
				if (lifeVolume == 3)
					newGrid[i][j] = 1;
			}
		}
	}
	
	for (i=0; i<M; i++)
	{
		for (j=0; j<N; j++)
		{
			grid[i][j] = newGrid[i][j];
		}
	}
}

int main()
{
	int i, j, k, lifeMatrix[M][N], midM = (M/2), midN = (N/2);
									
	for (i=0; i<M; i++)
	{
		for (j=0; j<N; j++)
		{
			lifeMatrix[i][j] = 0;
		}
	}
	
	lifeMatrix[midM-2][midN-1] = 1;
	lifeMatrix[midM-3][midN-1] = 1;
	lifeMatrix[midM+2][midN-1] = 1;
	lifeMatrix[midM+3][midN-1] = 1;

	lifeMatrix[midM][midN] = 1;
	lifeMatrix[midM-1][midN] = 1;
	lifeMatrix[midM+1][midN] = 1;

	lifeMatrix[midM-2][midN+1] = 1;
	lifeMatrix[midM+2][midN+1] = 1;
	lifeMatrix[midM-1][midN+2] = 1;
	lifeMatrix[midM+1][midN+2] = 1;
	lifeMatrix[midM][midN+3] = 1;
	
	for (k=0; k<300; k++)
	{
		system("cls");
		SetColor(15);
		printf("\nGeneration %d: \n",k+1);
		evolution(lifeMatrix);
		for (i=0; i<M; i++)
		{
			for (j=0; j<N; j++)
			{
				if(lifeMatrix[i][j]==1)
				{
					SetColor(3);
					printf(" o ");
				}
				else
				{
					SetColor(15);
					printf(" . ");
				}
			}
			printf("\n");
			set_cursor(0);
		}
		Sleep(250);
	}
	return 0;
}
