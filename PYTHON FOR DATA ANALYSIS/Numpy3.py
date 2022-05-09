# https://numpy.org/doc/stable/index.html=>(THIS IS RESOURSE OF NUMPUY LIBRARY)
# shuffle
# ex1
import numpy as np
numbers = np.arange(1, 10)
print("\n")
print(numbers)
np.random.shuffle(numbers)
print("\n")
print(numbers)
print("\n")
# ex2
numbers = np.arange(1, 101)
numbers_reshaped = numbers.reshape(3, 4)
print("\n")
print(numbers)
print("\n")
print(numbers_reshaped)
np.random.shuffle(numbers)
print("\n")
np.random.shuffle(numbers_reshaped)
print("\n")
print(numbers)
print("\n")
# ex3 MAXMUIM RANDOM FUNCTION
numbers = np.random.randint(1, 20, (5, 6))
print("\n")
print(numbers)
maxmuim = numbers.max()
print("\n")
print("Maxmuim : " + str(maxmuim))
print("\n")
# ex4 MINMUIM RANDOM FUNCTION
numbers = np.random.randint(1, 20, (5, 6))
print("\n")
print(numbers)
maxmuim = numbers.min()
print("\n")
print("Minmuim : " + str(minmuim))
print("\n")
# EX5 index matrix
numbers = np.random.randint(1, 20, (5, 5))
print("\n")
print(numbers)
max_index = numbers.argmax()
print("\n")
print("max index : +" str(max_index))
print("\n")
# EX6 index matrix
numbers = np.random.randint(1, 20, (5, 5))
print("\n")
print(numbers)
min_index = numbers.argmin()
print("\n")
print("min index : +" str(min_index))
print("\n")
# EX7 index matrix SHAPE
numbers = np.random.randint(1, 20, (5, 5))
print("\n")
print(numbers)
shape = numbers.shape[0]  # to know number of rows
print("\n")
print("Shape: +" str(shape))
print("\n")
# EX8 index matrix SHAPE
numbers = np.random.randint(1, 20, (5, 5))
print("\n")
print(numbers)
shape = numbers.shape[1]  # to know number of column
print("\n")
print("Shape: +" str(shape))
print("\n")

# # SHUFFLE
# random.shuffle(x)
# Modify a sequence in -place by shuffling its contents.

# This function only shuffles the array along the first axis of a multi-dimensional array. The order of sub-arrays is changed but their contents remains the same.

# Note

# New code should use the shuffle method of a default_rng() instance instead
# please see the Quick Start.

# Parameters
# xndarray or MutableSequence
# The array, list or mutable sequence to be shuffled.

# Returns
# None
# See also

# Generator.shuffle
# which should be used for new code.

# Examples

# arr = np.arange(10)
# np.random.shuffle(arr)
# arr
# [1 7 5 2 9 4 3 6 0 8]  # random
# Multi-dimensional arrays are only shuffled along the first axis:

# arr = np.arange(9).reshape((3, 3))
# np.random.shuffle(arr)
# arr
# array([[3, 4, 5],  # random
#        [6, 7, 8],
#        [0, 1, 2]])
