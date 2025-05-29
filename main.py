import numpy as np
print(np.__version__)

array_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array_2d)

element = array_2d[0,3]
print(element)

dimension = array_2d.ndim
print(dimension)

size = array_2d.size
print(size)

#shuma e komplet listes
total_sum = np.sum(array_2d)
print(total_sum)

sum_columns = np.sum(array_2d, axis = 0)
print(sum_columns)

sum_rows = np.sum(array_2d, axis = 1)
print(sum_rows)