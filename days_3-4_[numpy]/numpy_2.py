import numpy as np
import time
import sys


# n = 100

# list_start = time.time()

# list1 = range(n)
# list2 = range(n)

# sum_list = [(n1 + n2) for n1, n2 in zip(list1, list2)]

# print(sum_list)
# print(f'List time: {time.time() - list_start}')



# # Array:

# array_start = time.time()

# arrya1 = np.arange(n)
# arrya2 = np.arange(n)

# sum_array = arrya1 + arrya2

# print(sum_array)
# print(f'Array time: {time.time() - array_start}')


l = [1, 2, 3, 4, 5]

a = np.array([1, 2, 3, 4, 5])

print(f'Array: {a}')
print(f'Array Item: {a[0]}')
print(f'Array Len: {a.size}')
print(f'Array Item Size: {a.itemsize}')
print(f'Array Size: {a.size*a.itemsize} Byets')

print('- '*25)

print(f'List: {l}')
print(f'List Item: {l[0]}')
print(f'List Len: {len(l)}')
print(f'List Item Size: {sys.getsizeof(l[0])}')
print(f'List Size: {sys.getsizeof(l[0])*len(l)} Byets')