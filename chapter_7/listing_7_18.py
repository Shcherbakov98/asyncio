"""Вычисление средних в большой матрице с помощью NumPy"""
import numpy as np
import time


data_points = 4000000000
rows = 50
columns = int(data_points / rows)

matrix = np.arange(data_points).reshape(rows, columns)

start = time.time()

res = np.mean(matrix, axis=1)

end = time.time()

print('total_time = ', end - start)
# total_time =
