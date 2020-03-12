import numpy as np
from copy import copy, deepcopy

import os
import json
import matplotlib.pyplot as plt

from plot_utils import plot_grid

class Grid:
    def __init__(self, grid):
        if isinstance(grid, np.ndarray):
            grid = grid.tolist()
        
        assert isinstance(grid, list), "grid should be list of list"
        assert isinstance(grid[0], list), "grid should be list of list"
        
        self.grid = grid
        self.R = len(grid)
        self.C = len(grid[0])
        self.np_grid = np.asarray(grid)
        
        self.direction_arithematic = {
            'N': [-1, 0],
            'E': [0, 1],
            'S': [1, 0],
            'W': [0, -1],
        }
        
    
    def return_possible_grids(self, i, j, blocks=False):
        possible_grids = []
        for _, op in self.direction_arithematic.items():
            ni, nj = i + op[0], j + op[1]
            if (0 <= ni < self.R) and (0 <= nj < self.C):
                if not blocks:
                    possible_grids.append((ni, nj))
                else:
                    if self.is_empty(ni, nj):
                        possible_grids.append((ni, nj))
                        
        return possible_grids
    
    def show_cart_coords(self, with_val=False):
        for r in range(self.R):
            for c in range(self.C):
                if not with_val:
                    print("|{} {}| ".format(r, c), end="")
                else:
                    val = gi.access(r, c)
                    print("|{} {} ({})| ".format(r, c, val), end="")
            print("\n")
    
    def show(self):
        plot_grid(self.grid)
        
    def as_string(self):
        str_grid = ""
        for row in self.grid:
            for n in row:
                str_grid += "{} ".format(n)
            str_grid += "\n"
        return str_grid
    
    def is_edge(self, i, j):
        edge_v = [self.R - 1, self.C - 1, 0]
        return i in edge_v and j in edge_v
        
    def is_empty(self, i, j):
        val = self.access(i, j)
        return not val
    
    def access(self, i, j):
        return self.grid[i][j]
    
    def modify(self, i, j, val):
        self.grid[i][j] = val
    
    def __str__(self):
        return self.as_string()
    
    def __repr__(self):
        return self.as_string()