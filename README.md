# Green vs Red
Built with Python (+ NumPy).

To run the program write [ python main.py ] in your terminal.

#
###Description
'Green vs. Red' is a game played on a 2D grid that in theory can be infinite (in our case 
we will assume that x <= y < 1 000).

Each cell on this grid can be either green (represented by 1) or red (represented by 0). The
game always receives an initial state of the grid which we will call "Generation Zero". After that
a set of 4 rules are applied across the grid and those rules form the next generation.

##### Rules that create the next generation:

    1). Each red cell that is surrounded by exactly 3 or 6 green cells will also become green in
    the next generation.
    
    2). A red cell will stay red in the next generation if it has either 0, 1, 2, 4, 5, 7 or 8 
    green neighbours.
    
    3). Each green cell surrounded by 0, 1, 4, 5, 7 or 8 green neighbours will become red in the
    next generation.
    
    4). A green cell will stay green in the next generation if it has either 2, 3 or 6 green
    neighbours.
    
#
##### Important facts:
    - Each cell can be surrounded by up to 8 cells, 4 on the sides and 4 on the corners. Exceptions
    are the corners and the sides of the grid.
    - All the 4 rules apply at the same time for the whole grid in order for the next generation 
    to be formed.

## Task:
Create a program that accepts:
    - the size of our grid - x (columns/width), y (rows/height)
    - the next y lines should contain strings (long x characters) created by 0s and 1s which will
    represent the "Generation Zero" state and help us build the grid.
    - the last arguments to the program should be coordinates (x1 and y1) and the number N.
   
(x1 and y1) will be coordinates of a cell in the grid. We would like to calculate in how many
generations from Generation Zero until generation N this cell was green. (The calculation should 
include generation Zero and generation N).

Print your result in the console.

