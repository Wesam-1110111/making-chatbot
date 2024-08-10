import numpy as np


def pr():
	print(f'\n{'-'*50}\n')


def title(x):
	pr()
	print(f'{x}:\n')





# print(np.__version __)

# list & array:
print('list & array:\n')

n = [1, 2, 3, 4]
a = np.array(n)

print(f'list: {n}')
print(f'array: {a}')

pr()

# type:
print('type:\n')

print(type(n))
print(type(a))

pr()

# Array-D:
print('Array-D:\n')

d0 = np.array(6)
d1 = np.array([4, 3])
d2 = np.array([ [12, 7], [30, 0] ])
d3 = np.array([ [ [5, 21], [10, 7] ] ])
d4 = np.array([ [ [ [7, 3], [7, 4] ] ] ])


print('Zero-D: ', d0)
print('One-D: ', d1)
print('Two-D: ', d2)
print('Three-D: ', d3)
print('Four-D: ', d4)

print()
print('d2[0, 1]:', d2[0, 1])
print('d4[0, 0, 1, 0]:', d4[0, 0, 1, 0])

pr()

# Number of Dimensions:
print('Number of Dimensions:\n')

print(np.ndim(d0))
print(np.ndim(d1))
print(np.ndim(d2))
print(np.ndim(d3))
print(np.ndim(d4))



# Custom Array-D:
title('Custom Array-D')

cd = np.array(7, ndmin=16)
print('Custom D: ', cd)
print('Number of D:', np.ndim(cd))


# END
print('\nThe End.')