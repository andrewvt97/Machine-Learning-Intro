import numpy as np

a = np.array([1,2,3]) # 1 dimensional array in numpy
b = np.array([(1.5,2,3), (4,5,6)],dtype=float) # two dimensional array with floats (each tuple is a row)
c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]],dtype=float) # 3 dimensional array, with 2 2 dimensional arrays that have 2 rows and 3 cols

np.zeros((3,4)) # two dimensional array of 3 rows and 4 cols filled with zeros
np.ones((2,3,4), dtype=np.int16) # 3 dimensional arrays with 2 2 dimensional arrays, 3 rows, and 4 cols with values as 16 bit integers
d = np.arange(10, 25, 5) # d= [10, 15, 20]
np.linspace(0, 2, 9) # array of 9 numbers from 0 to 2 = [0,0.25,0.5,0.75,1,1.25,1.5,1.75,2]
e = np.full((2,2), 7) # 2D array of 2 rows and 2 cols filled with 7
f = np.eye(2) # generates array of 2 rows and 2 cols with 1's on the diagonal and 0's everywhere else (identity matrix)
np.random.random((2,2)) # 2D array of 2 rows, 2 cols filled with random values from 0 to 1 (1 is not included)
R = np.floor(np.random.random((5,5)) * 6) + 1 # this changes the ranges from 1 to 6 (floor is used and 6.999 will be rounded down)
np.empty((3,2)) # 2D array of 3 rows, 2 cols filled with unitialized memory

# different data types that can be used
np.int64
np.float32
np.complex # real and imaginary numbers
np.bool
np.object # any data type, so more flexible but less efficient
np.string_
np.unicode_ # more symbols beyond ASCII


a.shape # tuple that represents the dimensions of the array such as (3,4)
len(a) # size of the first dimension of the array, so in a 2D array it would be num of rows, for 3d it would be number of 2D arrays
b.ndim # returns number of dimensions, ex: 3 for 3D array
e.size # total number of elements in the array, ex: 3 x 4 * 2 = 3 * 4 * 2 = 24 elements
b.dtype # data type of the elements of the array such as dtype('int32')
b.dtype.name # returns data type as a string such as 'int32'
b.astype(int) # returns new array with data type changed to specified

np.info(np.ndarray.dtype) # gives quick info about dtype of an array
# these all return new arrays
# the arithemetic operations either require the same shape or can use broadcasting
# (this works if a was 1 x 3 and b was 3 x 3 which would result in the a's single row being added to all 3 of b's rows otherwise error)
# both functions below subtract matrices
g = a - b 
np.subtract(a, b)
# both functions below add matrices
b + a
np.add(b, a)
# both functions below dividematrices
a / b
np.divide(a, b)
# both functions below add matrices
a * b
np.multiply(a, b)
np.exp(b) # raises all elements to an exponent
np.sqrt(b) # calculates square root for all elements
np.sin(a) # calculates sin of all elements
np.cos(b) # calculates cos of all elements
np.log(a) # calculates natural log of all elements
e.dot(f) # calculates dot product of e and f (dimensions must agree)

a == b # compares a and b and returns a boolean array of same shape as a and b
a < 2 # compares all elements of a with 2 and returns boolean values of same array shape
np.array_equal(a, b) # returns True if a and b have same shape and elements, False otherwise
a.sum() # sum of all elements in the array
a.min() # min of all elements in the array
b.max(axis=0) # returns max of every column from array b
b.cumsum(axis=1) 
''' 
returns array of same shape as b where each element is replaced by cumulative sum of elements before it 
(axis = 1 means going along each row) 
'''
a.mean() # mean of all elements in the array
b.median() # median of all elements in the array (np.median(b)?)
a.corrcoef() # finds the correlation matrix considering each row of a as a separate variable and comparing them (np.corrcoef(a)?)
corr_matrix_complex = np.corrcoef([x, y, z])
[[1.        , 0.97227182, 0.6279595 ], # correlation of row x with each of x, y, z
 [0.97227182, 1.        , 0.66359273], # same pattern but with row y
 [0.6279595 , 0.66359273, 1.        ]] # same but row z
# being compared with themselves results in 1's across the diagonal
np.std(b) # standard deviation of all elements in the array

# axis 0 runs downward, axis 1 runs horizontal in a 2d

h = a.view() # creates array h that is a copy of array a, points to the same memory so a will be affected
# things like transpose of h won't affect a because it doesn't do anything to memory
np.copy(a) # deep copy of a where new array owns its own data
h = a.copy() # assigns deep copy of a to h
a.sort() # sorts array in ascending order, will sort around the last axis for multi dimensional (rows)
c.sort(axis=0) # sorts among the column axis
a[2] # 3rd element of the array
b[1,2] # element at row 1 col 2
a[0:2] # elements from 0 upto 2 (not inclusive) (first dimension if multiple)
b[0:2,1] # elements from row 0 upto 2 and selects column 1 of these rows
b[:1] # slects first element, or selects first group in the first dimension
c[1,...] # used to get group 1 of first dimension
a[::-1] # reverses the array, reverses groups of first dimension in multiple dimensions

a[a<2] # returns values of a that are less than 2, will flatten 2 or 3d to 1d
b[[1,0,1,0],[0,1,2,0]] # fancy indexing where the first array refers to row and second array refers to column
# together this would select b[1][0] b[0][1] b[1][2] and b[0][0] into a single 1D array
b[[1,0,1,0]][:,[0,1,2,0]] # creates an array choosing rows 1, 0, 1 and 0 again
# next it selects all rows and only chooses column 0, 1, 2, and 0 again
i = np.transpose(b) # columns become rows
i.T # another way to transpose
b.ravel() # flattens b into a 1D array row wise
g.reshape(3, -2)
h.resize((2,6))
np.append(h, g)
np.insert(a, 1, 5)
np.delete(a, [1])
