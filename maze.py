import random 
#randomizer for directions and random generation
import copy
#copying the code so it doesnt alter first maze

def generate_maze(rows, cols):
 
    #making maze with walls
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
 def carve_passages(r, c):
        #define the moves (jumping two cells) for up, left, right, down
        directions = [(0, -2), (-2, 0), (0, 2), (2, 0)]
        random.shuffle(directions)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            #make sure we stay within the maze and the neighbor is a wall
            if 0 < nr < rows and 0 < nc < cols and maze[nr][nc] == '#':
                #make the passage between the two cells
                maze[r + dr // 2][c + dc // 2] = ' '
                maze[nr][nc] = ' '
                carve_passages(nr, nc)
                
    #start to carving passages from (1,1)
    maze[1][1] = ' '
    carve_passages(1, 1)
 #set start and exit points
    maze[0][1] = 'S'            # start at (0,1)
    maze[rows - 1][cols - 2] = 'E'  # exit at bottom right 
    return maze

def display_maze(maze):
    """
    print the maze to the console
    
    Arguments:
        maze (list[list[str]]): Maze to display
    """
    for row in maze:
        print(''.join(row))
    def solve_maze(maze, r, c, path=None):
    """
     DFS Recursion
    
    Argumens:
        maze (list[list[str]]): The maze grid
        r (int): Current row
        c (int): Current column
        path (list of tuple): Accumulated path
    """
    if path is None:
        path = []
# base case (exit is found)
    if maze[r][c] == 'E':
        path.append((r, c))
        return path
    
    #check for walls or already visited cells
    if maze[r][c] in ('#', '.', '+'):
        return None
    
    # mark the current cell (except if it's the start 'S')
    if maze[r][c] != 'S':
        maze[r][c] = '+'
    path.append((r, c))
