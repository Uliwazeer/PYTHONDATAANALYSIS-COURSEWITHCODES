# RANDOM rand=>print a random numbers between 0 and 1
# ex1
from random import randint
import numpy as np
r = np.random.rand(5)
print(r)
# ex2 as matrix rows and columns
r = np.random.rand(5, 8)
print(r)
# ex3 randint =>print a random number between 0 to vavlue which you give it
i = np.random.randint(100)
print(i)
# ex4 randint =>print a random number between 100 to vavlue(500) which you give it
i = np.random.randint(100, 500)
print(i)
# ex5 randint =>print a random number between 100 to vavlue(500) number of numbers(8) which you give it
i = np.random.randint(100, 500, 8)
print(i)
# ex6 randint =>print a random number as a matrix between 100 to vavlue(500) number of numbers(8) which you give it
i = np.random.randint(100, 500, (5, 6)  # dimensional of matrix)
print(i)
# ex7 no_shape and reshape
import numpy as np
no_shape=np.random.randint(100, 200, 10)
shape=no_shape.reshape(5, 2)
print("\n")
print(no_shape)
print("\n")
print(shape)

# random randint
    # Examples

    # np.random.randint(2, size=10)
    # array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0])  # random
    # np.random.randint(1, size=10)
    # array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    # Generate a 2 x 4 array of ints between 0 and 4, inclusive:

    # np.random.randint(5, size=(2, 4))
    # array([[4, 0, 2, 1],  # random
    #        [3, 2, 2, 0]])
    # Generate a 1 x 3 array with 3 different upper bounds

    # np.random.randint(1, [3, 5, 10])
    # array([2, 2, 9])  # random
    # Generate a 1 by 3 array with 3 different lower bounds

    # np.random.randint([1, 5, 7], 10)
    # array([9, 8, 7])  # random
    # Generate a 2 by 4 array using broadcasting with dtype of uint8

    # np.random.randint([1, 3, 5, 7], [[10], [20]], dtype=np.uint8)
    # array([[8,  6,  9,  7],  # random
    #        [1, 16,  9, 12]], dtype=uint8)

    # random rand
    # numpy.random.rand
    # random.rand(d0, d1, ..., dn)
    # Random values in a given shape.

    # Note

    # This is a convenience function for users porting code from Matlab, and wraps random_sample. That function takes a tuple to specify the size of the output, which is consistent with other NumPy functions like numpy.zeros and numpy.ones.

    # Create an array of the given shape and populate it with random samples from a uniform distribution over[0, 1).

    # Parameters
    # d0, d1, …, dnint, optional
    # The dimensions of the returned array, must be non-negative. If no argument is given a single Python float is returned.

    # Returns
    # outndarray, shape(d0, d1, ..., dn)
    # Random values.

    # See also

    # random
    # Examples

    # np.random.rand(3, 2)
    # array([[0.14022471,  0.96360618],  # random
    #        [0.37601032,  0.25528411],  # random
    #        [0.49313049,  0.94909878]])  # random
