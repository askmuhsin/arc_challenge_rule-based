import matplotlib.pyplot as plt
from matplotlib import colors

def plot_grid_util(ax, grid):
    cmap = colors.ListedColormap([
        '#000000', '#0074D9','#FF4136','#2ECC40','#FFDC00',
        '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25'
    ])
    norm = colors.Normalize(vmin=0, vmax=9)
    ax.imshow(grid, cmap=cmap, norm=norm)
    ax.grid(True, which='both',color='lightgrey', linewidth=0.5)   

    ax.set_yticks([x-0.5 for x in range(1+len(grid))])
    ax.set_xticks([x-0.5 for x in range(1+len(grid[0]))])     
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
    
def plot_grid(grid):
    fig, ax = plt.subplots()
    plot_grid_util(ax, grid)
