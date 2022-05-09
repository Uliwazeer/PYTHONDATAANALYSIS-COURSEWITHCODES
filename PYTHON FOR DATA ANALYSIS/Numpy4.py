# https://numpy.org/doc/stable/index.html =>(THIS IS THE RESOURCE)
# ex1 ceil to make float to integer number(for up number)
import numpy as np
c=np.ceil(2.4)
print("\n")
print(c)
print("\n")
# ex2 floor to make float to integer number(for down number)
import numpy as np
f=np.floor(2.4)
print("\n")
print(f)
print("\n")
# ex3 round to make float to integer number(for down number when lettle than 0.5 for up number when bigger than 0.4)
import numpy as np
r1=np.round(2.3)
r2=np.round(2.6)
print("\n")
print(r1)
print("\n")
print(r2)
# ex4 add two numbers or matrix
import numpy as np
add = np.add(3.2)
print("\n")
print(add)
print("\n")
# ex5 add two numbers or matrix
import numpy as np
matrix = [[1,2,3,4,5],[0,6,7,8,9]]
add = np.add(matrix,2)
print("\n")
print(add)
print("\n")
# ex6 add two numbers or matrix
import numpy as np
matrix_1 = [[1,2,3,4,5],[0,6,7,8,9],[4,9,8,7,1]]
matrix_2 = [[1,2,3,4,5],[0,6,7,8,9],[4,9,8,7,1]]
add = np.add(matrix_1,matrix_2)
print("\n")
print(add)
print("\n")
# ex7 multiply every element in 2 matrix inothers
import numpy as np 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
add = np.multiply(matrix,2)
print("\n")
print(add)
print("\n")
# ex8 divide every element over 2 matrix inothers
import numpy as np 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
add = np.derive(matrix,2)
print("\n")
print(add)
print("\n")
# ex9 divide matrix_1 on matrix_2
matrix_1 = [[1, 2, 3, 4, 5], [0, 6, 7, 8, 9], [4, 9, 8, 7, 1]]
matrix_2 = [[1, 2, 3, 4, 5], [0, 6, 7, 8, 9], [4, 9, 8, 7, 1]]
add = np.divide(matrix_1, matrix_2)
print("\n")
print(add)
print("\n")
