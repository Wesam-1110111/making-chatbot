import numpy as np



arr1 = np.array([2, 4, 6, 8, 0])
arr2 = np.array([1, 5, 7, 9, -1])


print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

print()
print('-'*30)
print()

arr3 = np.array([[1, 0], [8, 12]])
arr4 = np.array([[-5, 7], [3, 13]])

print(arr3 + arr4)
print(arr3 - arr4)
print(arr3 * arr4)
print(arr3 / arr4)


print('the MIN value in arr3:', np.min(arr3))
print('the MAX value in arr3:', np.max(arr3))
print('the SUM of values arr3:', np.sum(arr3))

print()
print('-'*30)
print()

print(arr3)
print(arr3.ndim)
arr3 = arr3.ravel()
print(arr3)
print(arr3.ndim)
