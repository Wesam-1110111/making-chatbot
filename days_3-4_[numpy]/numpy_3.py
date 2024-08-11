import numpy as np



a1 = np.array((1, 2, 3, 4), dtype=int) # int or 'int', 'i'

print(a1)
print(a1.dtype)

print()

a2 = np.array((0, 5, 0, 77), dtype=float) # float or 'float', 'f'

print(a2)
print(a2.dtype)

print()

a3 = a2.astype(bool)

print(a3)
print(a3.dtype)


print()

a4 = a3.astype(str)

print(a4)
print(a4.dtype)