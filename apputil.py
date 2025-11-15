import numpy as np
from IPython.display import clear_output
import time
import seaborn as sns
import matplotlib.pyplot as plt

'''
show_game(game_board, n_steps=5, pause=1) ->
for each step:
    clear output
    call update_board to get new board
    show board using seaborn heatmap
    wait for pause seconds
'''


def get_neighbors(row_r, column_c, grid):
    '''Gets the coordinates of all eight neighbors of a cell [row_r, column_c] in a 2D grid,
    wrapping around edges.'''
    neighbors = []
    rows, cols = grid.shape

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not (i == 0 and j == 0):
                neighbor_row = (row_r + i) % rows
                neighbor_col = (column_c + j) % cols
                neighbors.append([neighbor_row, neighbor_col])  # <-- return coordinates

    return neighbors
    
def sum_neighbors(neighbors, grid):
    '''Sums the values of all neighbors in a grid given their coordinates.'''
    total = 0
    for r, c in neighbors:   # unpack coordinate pairs
        total += grid[r, c]  # look up value in grid
    return total

# update this one ...
def update_board(current_board):
    # your code here ...

    #initialize updated_board as 10x10 array of zeros
    updated_board = np.zeros(current_board.shape, dtype=int)

    # iterate through each cell in the board
    # for each row
    for i in range(current_board.shape[0]):
        # for each column
        for j in range(current_board.shape[1]):
            # count living neighbors
            sum_of_neighbors = sum_neighbors(get_neighbors(i, j, current_board), current_board)

            # apply Conway's rules
            if current_board[i, j] == 1:
                if sum_of_neighbors < 2 or sum_of_neighbors > 3:
                    updated_board[i, j] = 0  # cell dies
                else:
                    updated_board[i, j] = 1  # cell lives
            else:
                if sum_of_neighbors == 3:
                    updated_board[i, j] = 1  # cell becomes alive
                else:
                    updated_board[i, j] = 0  # cell remains dead

    

    return updated_board


def show_game(game_board, n_steps=10, pause=0.5):
    """
    Show `n_steps` of Conway's Game of Life, given the `update_board` function.

    Parameters
    ----------
    game_board : numpy.ndarray
        A binary array representing the initial starting conditions for Conway's Game of Life. In this array, ` represents a "living" cell and 0 represents a "dead" cell.
    n_steps : int, optional
        Number of game steps to run through, by default 10
    pause : float, optional
        Number of seconds to wait between steps, by default 0.5
    """
    for step in range(n_steps):
        clear_output(wait=True)

        # update board
        game_board = update_board(game_board)

        # show board
        sns.heatmap(game_board, cmap='plasma', cbar=False, square=True)
        plt.title(f'Board State at Step {step + 1}')
        plt.show()

        # wait for the next step
        if step + 1 < n_steps:
            time.sleep(pause)



