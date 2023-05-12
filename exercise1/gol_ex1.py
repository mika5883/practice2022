import math
import numpy as np

def some_func(function, minx: float = None, maxx: float = None, dx: float = None):
    points = []
    max_range = maxx - minx
    center_point = int(max_range / 2) / dx

    x = minx 
    
    for i in np.arange(minx, maxx, dx):
        y = function(x)
        points.append((x, y))
        x += dx

    for point in points:
        if point[1] > 0:
            print(' '*(int(round(center_point + (point[1] / dx), 1))) + '*')
        else:
            print(' '*(int(round(center_point - (point[1] / dx), 1))) + '*')


some_func(function=lambda x: math.sin(x), minx=-3, maxx=3, dx=0.2)
