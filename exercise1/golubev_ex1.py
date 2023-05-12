import math
import numpy as np

def some_func(function, minx: float=None, maxx: float=None, dx: float=None):
    points = []
    function = math.__dict__[function]
    
    maxrange = maxx - minx
    center_point = int(maxrange / 2) / dx
    x = minx
    
    for x in np.arange(minx, maxx+dx, dx):
        y = function(x)
        points.append((int(x/dx), int(round(y/dx, 1))))
        x += dx
    points.sort(key=lambda a: a[0])
    print(points)
    
    lines_to_print = []
    for each in points:
        to_print = [i for i in points if i[1] == each[1]]
        lines_to_print.append(to_print)
    lines_to_print = sorted(lines_to_print, key=lambda a: a[0][1], reverse=True)
    print(lines_to_print)
    
    for each in lines_to_print:
        cur_ind  = lines_to_print.index(each)
        try: prev_ind = lines_to_print[cur_ind-1]
        except:
            pass
        
    
some_func('sin', 0, 3, 0.1)


