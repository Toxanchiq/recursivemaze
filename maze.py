import random 
#randomizer for directions and random generation
import copy
#copying the code so it doesnt alter first maze

def generate_maze(rows, cols):
 
    #making maze with walls
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
