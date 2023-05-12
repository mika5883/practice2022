import numpy as np
import math
'''
- `^` -- функция имеет локальный максимум
- `v` -- функция имеет локальный минимум
- `|` -- функция резко возрастает или убывает: `|(f(x + dx) - f(x)) / dx| > 10`
- `-` -- функция (почти) не изменяется `|(f(x + dx) - f(x)) / dx| < 0,1`
- `/` -- функция возрастает
- `\` -- функция убывает
- `*` -- остальные случаи
'''
specials = '^ v | - / \ *'.split()

def some_func(function: str = None, minx: float = None, maxx: float = None, dx: float = None):
    func = math.__dict__[function]
    points = []
    max_range = maxx - minx
    center_point = int((max_range / 2) / dx)
    
    x = minx 
    if func == math.__dict__['log']:
        x += dx + 0.1
    
    for i in np.arange(minx, maxx+dx, dx):
        y = func(x)
        next_func = func(x+dx)
        prev_func = func(x-dx)
        previous_val = (func(x - dx) - func(x)) / dx
        next_val = (func(x + dx) - func(x)) / dx
        print(f'x: {round(x, 5)}  cur func: {round(y, 5)}.  Previous: {round(previous_val, 5)}.   Next: {round(next_val, 5)}')
        #print((func(x + dx) - func(x)) / dx)
        if y > next_func and y > prev_func:
            print(x)
            symb = specials[0]
        elif y < next_func and y < prev_func:
            print(x)
            symb = specials[1]
        elif next_val > 10:
            symb = specials[2]
        elif 0 < next_val < 0.1 :
            symb = specials[3]
        elif next_val > 0:
            symb = specials[4]
        elif next_val < 0:
            symb = specials[5]
        else:
            symb = specials[6]
        print(symb)
        points.append((int(x/dx), int(round(y/dx, 1)), symb))
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
        print(line)
        for i, el in enumerate(line):
            try:
                while abs(el[0] - line[i+1][0]) == 1:
                    if line[i+1][2] == specials[0]:
                        line[i][2] = specials[0]
                    line.pop(i+1)
            except: pass
        print(line)
    for line in lines_to_print:
        to_print = []
        #print(line)
        for each in line:
            while len(to_print) < (center_point + each[0]):
                to_print.append(' ') 
            #to_print.append('*')
            to_print.append(each[2])
        print(''.join(to_print))

some_func(function='erf', minx=-5, maxx=5, dx=0.1)
