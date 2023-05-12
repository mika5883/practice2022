import numpy as np

def some_func(function: str = None, minx: float = None, maxx: float = None, dx: float = None):
    func = np.__dict__[function]
    points = []
    max_range = maxx - minx
    center_point = int((max_range / 2) / dx)
    
    x = minx 
    
    for i in np.arange(minx, maxx+dx, dx):
        y = func(x)
        points.append((int(x/dx), int(round(y/dx, 1))))
        x += dx        
    
    lines_to_print = []
    for each in points:
        to_print = [i for i in points if (i[1]) == (each[1])]
        lines_to_print.append(to_print)
    lines_to_print = sorted(lines_to_print, key=lambda a: a[0][1], reverse=True)
    
    #избавляемся от повторяющихся строк
    for i, line in enumerate(lines_to_print):
        try:
            while line == lines_to_print[i+1]:
                lines_to_print.pop(i+1)
        except: pass 
    
    #избавляемся от повторяющихся элементов внутри строк
    for line in lines_to_print:
        for i, el in enumerate(line):
            try:
                while el == line[i+1]:
                    line.pop(i+1)
            except: pass
        
    for line in lines_to_print:
        to_print = []
        for each in line:
            while len(to_print) < (center_point + each[0]):
                to_print.append(' ') 
            to_print.append('*')
        print(''.join(to_print))

some_func(function='sin', minx=0, maxx=10, dx=0.1)
