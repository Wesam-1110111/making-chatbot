import numpy as np  





arr1 = np.array([0, 1, 2, 3, 4, 5, 6, 7])

print(arr1)
print(arr1.ndim)
print(arr1.shape)

print('\n- - - - - - - - - - - - - - - - - - - - - - \nEx 2:\n')

arr2 = arr1.reshape(4, 2)
print(arr2)
print(arr2.ndim)
print(arr2.shape)
