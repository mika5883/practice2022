import numpy as np

overall = []

with open('sample.csv') as f:
    f.readline()
    for i, line in enumerate(f, start=1):
        try:
            numbers = [float(each) for each in line.split(',')]
            np_arr = np.asarray(numbers)
        except:
            continue
        mean = np.mean(np_arr)
        std = np.std(np_arr)
        new_arr = np.array([i, mean, std])
        if new_arr[2] < 250: 
            overall.append(new_arr)
np_overall = np.asarray(overall)
np.savetxt('output.txt', np_overall, fmt='%.2f', delimiter='\t')


        
        
            