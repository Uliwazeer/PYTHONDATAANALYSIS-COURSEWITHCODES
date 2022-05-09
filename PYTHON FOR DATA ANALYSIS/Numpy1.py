# numpy is a libirary to treat with Numbers AND numerical operation ,matrix,probability
# NumPy is the fundamental package for scientific computing in Python. It is a Python library
# that provides a multidimensional array object, various derived objects(such as masked arrays
# and matrices), and an assortment of routines for fast operations on arrays, including
# mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms,
# basic linear algebra, basic statistical operations, random simulation and much more.

# ex1
import numpy as np
ls = [1, 2, 3, 4, 5]
array = np.array(ls)
print(ls)
print("#################")
print(array)

# ex2

ls = [1, 2, 3, 4, 5, [8, 9, 8, 7, 4], [
    8, 88, 99, 66, 55, 44, 11], [12, 56, 58, 96, 54, 11, 58]]
array = np.array(ls)
print(ls)
print("#################")
print(array)


# Arange Function=>(start,end,step(optional))
# ex3
arange = np.arange(1, 100)
print(arange)
# ex4
arange = np.arange(1, 1000, 5)
print(arange)

# Zeros Function=>(rows,columns) print matrix all elements are zeros from its name
# ex5
z = np.zeros((5, 8))
print(z)
# Ones Function=>(rows,columns) print matrix all elements are ones from its name
# ex6
o = np.ones((5, 8))
print(o)

# 3
# WHAT ABOUT ZEROS IN NUMPY OF PYTHON  ?
# numpy.zeros
# numpy.zeros(shape, dtype=float, order='C', *, like=None)
# Return a new array of given shape and type, filled with zeros.

# Parameters
# shapeint or tuple of ints
# Shape of the new array, e.g., (2, 3) or 2.

# dtypedata-type, optional
# The desired data-type for the array, e.g., numpy.int8. Default is numpy.float64.

# order{‘C’, ‘F’}, optional, default: ‘C’
# Whether to store multi-dimensional data in row-major(C-style) or column-major(Fortran-style) order in memory.

# likearray_like
# Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as like supports the __array_function__ protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

# New in version 1.20.0.

# Returns
# outndarray
# Array of zeros with the given shape, dtype, and order.

# See also

# zeros_like
# Return an array of zeros with shape and type of input.

# empty
# Return a new uninitialized array.

# ones
# Return a new array setting values to one.

# full
# Return a new array of given shape filled with value.

# Examples

# np.zeros(5)
# array([0.,  0.,  0.,  0.,  0.])
# np.zeros((5,), dtype=int)
# array([0, 0, 0, 0, 0])
# np.zeros((2, 1))
# array([[0.],
#        [0.]])
# s = (2, 2)
# np.zeros(s)
# array([[0.,  0.],
#        [0.,  0.]])
# np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')])  # custom dtype
# array([(0, 0), (0, 0)],
#       dtype=[('x', '<i4'), ('y', '<i4')])


# WHAT ABOUT ONES IN NUMPY IN PYTHON ?
# The numpy.ones() function returns the new array of given shape and data type, where the element’s value is set to 1. The ones() function is very similar to numpy zeros() function.

# np.ones
# The np.ones() is a Numpy library function that returns an array of similar shape
# and size with values of elements of the array as ones. The np.ones() function takes three
# parameters at
# max and returns an array with element values as ones.

# arange in numpy in python
# numpy.arange
# numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
# Return evenly spaced values within a given interval.

# Values are generated within the half-open interval [start, stop) (in other words, the interval including start but excluding stop). For integer arguments the function is equivalent to the Python built-in range function, but returns an ndarray rather than a list.

# When using a non-integer step, such as 0.1, it is often better to use numpy.linspace. See the warnings section below for more information.

# Parameters
# startinteger or real, optional
# Start of interval. The interval includes this value. The default start value is 0.

# stopinteger or real
# End of interval. The interval does not include this value, except in some cases where step is not an integer and floating point round-off affects the length of out.

# stepinteger or real, optional
# Spacing between values. For any output out, this is the distance between two adjacent values, out[i+1] - out[i]. The default step size is 1. If step is specified as a position argument, start must also be given.

# dtypedtype
# The type of the output array. If dtype is not given, infer the data type from the other input arguments.

# likearray_like
# Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as like supports the __array_function__ protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

# New in version 1.20.0.

# Returns
# arangendarray
# Array of evenly spaced values.

# For floating point arguments, the length of the result is ceil((stop - start)/step). Because of floating point overflow, this rule may result in the last element of out being greater than stop.

# Warning

# The length of the output might not be numerically stable.

# Another stability issue is due to the internal implementation of numpy.arange. The actual step value used to populate the array is dtype(start + step) - dtype(start) and not step. Precision loss can occur here, due to casting or due to using floating points when start is much larger than step. This can lead to unexpected behaviour. For example:

# np.arange(0, 5, 0.5, dtype=int)
# array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# np.arange(-3, 3, 0.5, dtype=int)
# array([-3, -2, -1,  0,  1,  2,  3,  4,  5,  6,  7,  8])
# In such cases, the use of numpy.linspace should be preferred.

# See also

# numpy.linspace
# Evenly spaced numbers with careful handling of endpoints.

# numpy.ogrid
# Arrays of evenly spaced numbers in N-dimensions.

# numpy.mgrid
# Grid-shaped arrays of evenly spaced numbers in N-dimensions.

# Examples

# np.arange(3)
# array([0, 1, 2])
# np.arange(3.0)
# array([ 0.,  1.,  2.])
# np.arange(3,7)
# array([3, 4, 5, 6])
# np.arange(3,7,2)
# # array([3, 5])
