from grid import Grid

import numpy as np

debug = True

def debug_options(func):
    def transform(*args, **kwargs):
        result = func(*args, **kwargs)
        if debug:
            print(func)
            result.show()
        return result
    return transform


@debug_options
def tfm_zeros_like(grid):
    out_grid = Grid(np.zeros_like(grid.grid))
    return out_grid


@debug_options
def tfm_copy_grid_right(grid, times=2):
    out = np.concatenate(
        ([grid.np_grid] * times),
        axis=1
    )
    out_grid = Grid(out)
    return out_grid


@debug_options
def tfm_copy_grid_down(grid, times=2):
    out = np.concatenate(
        ([grid.np_grid] * times),
        axis=0
    )
    out_grid = Grid(out)
    return out_grid


@debug_options
def tfm_flip_vertical(grid):
    out = np.flipud(grid.np_grid)
    out_grid = Grid(out)
    return out_grid


@debug_options
def tfm_flip_horizontal(grid):
    out = np.fliplr(grid.np_grid)
    out_grid = Grid(out)
    return out_grid


@debug_options
def tfm_concat_horizontal(grid_1, grid_2):
    out = np.concatenate((grid_1.np_grid, grid_2.np_grid))
    out_grid = Grid(out)
    return out_grid