#Statistics

print("Catch up in Preview".center(80, "-"))

import numpy as np
print('numpy:', np.__version__)# How to check the version of the numpy package
print(dir(np)) # Checking the available methods

print("Creating int numpy arrays".center(80, "-"))
python_list = [1,2,3,4,5]# Creating python List

print('Type:', type (python_list)) # <class 'list'>
print(python_list) # [1, 2, 3, 4, 5]


numpy_array_from_list = np.array(python_list)
print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
print(numpy_array_from_list) # array([1, 2, 3, 4, 5])

print("Creating float numpy arrays".center(80, "-"))
python_list = [1,2,3,4,5]
numpy_array_from_list_float = np.array(python_list, dtype=float)
print(numpy_array_from_list_float) #array[1. 2. 3. 4. 5.]

print("Creating boolean numpy arrays".center(80, "-"))
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool) 
print(numpy_bool_array)#array[False  True  True False False]

print("Creating multidimensional array using numpy".center(80, "-"))
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

numpy_two_dimension_list = np.array(two_dimensional_list)
print(type(numpy_two_dimension_list)) #<class 'numpy.ndarray'>
print(numpy_two_dimension_list)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''

print("Converting numpy array to list".center(80, "-"))
# numpy_array_from_list =  array([1, 2, 3, 4, 5])
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print(f'One dimension array:', np_to_list)
print(f'Two dimension array:', numpy_two_dimension_list.tolist())

print("Creating numpy array from tuple".center(80, "-"))
# Creating tuple in python
python_tuple = (1, 2, 3, 4, 5)
print(type(python_tuple))
print(f'{python_tuple}')

numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))
print(f'{numpy_array_from_tuple}')

print("Shape of numpy array".center(80, "-"))
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print(nums.shape)
print(numpy_two_dimension_list)
print(numpy_two_dimension_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
                               [4, 5, 6, 7],
                               [8, 9, 10, 11]])
print(three_by_four_array.shape)

print("Data type of numpy array".center(80, "-"))
int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype) #int32
print(float_array)
print(float_array.dtype) #float64

print("Size of a numpy array".center(80, "-"))
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                                 [3, 4, 5],
                                 [6, 7, 8]])
print({numpy_array_from_list.size})
print({two_dimensional_list.size})

print("Mathematical Operation using numpy".center(80, "-"))
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print(f'{numpy_array_from_list}')

#Addition
ten_plus_original = numpy_array_from_list + 10
print(ten_plus_original)

#Subtraction
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print(f'{numpy_array_from_list}')
ten_minus_original = numpy_array_from_list - 10
print(ten_minus_original)

#Multiplication
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print(f'{numpy_array_from_list}')
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)

#Division
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
ten_division_original = numpy_array_from_list / 10
print(ten_division_original)

#Modulus
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print(f'{numpy_array_from_list}')
ten_modulus_original = numpy_array_from_list % 3
print(f'{ten_modulus_original}')

#Floor Division
ten_floor_division_original = numpy_array_from_list // 10
print(f'{ten_floor_division_original}')

#Power
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
ten_power_original = numpy_array_from_list ** 2
print(ten_power_original)

print("Checking data types".center(80, "-"))
#Int,  Float numbers
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

print("Converting types".center(80, "-"))

#Int to float
numpy_int_arr = np.array([1, 2, 3, 4], dtype='float')
print(numpy_int_arr) #[1. 2. 3. 4.]
print(type(numpy_int_arr)) #<class 'numpy.ndarray'>
print(numpy_int_arr.dtype) #float64

#float to int
numpy_int_arr = np.array([1., 2., 3., 4.], dtype='int')
print(numpy_int_arr)

#Int to boolean
numpy_int_arr = np.array([-3, -2, 0, 1, 2, 3], dtype = 'bool')
print(numpy_int_arr) #[ True  True False  True  True  True]

#Int to str
numpy_int_arr = np.array([-3, -2, 0, 1, 2, 3], dtype = '<U21')
print(numpy_int_arr) #['-3' '-2' '0' '1' '2' '3']

print("Multi-dimensional Arrays".center(80, "-"))
two_dimension_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(type(two_dimension_array)) #<class 'numpy.ndarray'>
print(two_dimension_array)
print(f'{two_dimension_array.shape = }') #(3, 3)
print(f'{two_dimension_array.size = }') #9
print(f'{two_dimension_array.dtype = }') #dtype('int32')

two_dimension_array = np.array([(1, 2, 3)])
print(f'{two_dimension_array.shape = }') # (1, 3) (row, columns)

print("Getting items from a numpy array".center(80, "-"))
#2 Dimension Array
two_dimension_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print(f'{first_row}') #[1 2 3]
print(f'{second_row}') #[4 5 6]
print(f'{third_row}') #[7 8 9]

first_column = two_dimension_array[:,0]
before_first_row = two_dimension_array[:0] # array([], shape=(0, 3), dtype=int32)
until_first_row = two_dimension_array[:1] #Still means to print until the first row
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print(f'{first_column = }')  #array([1, 4, 7])
print(f'{before_first_row = }') # array([], shape=(0, 3), dtype=int32)
print(f'{until_first_row = }') #array([[1, 2, 3]])
print(f'{second_column = }') #array([2, 5, 8])
print(f'{third_column = }') #array([3, 6, 9])

print("Slicing Numpy array".center(80, "-"))
two_dimension_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)

print("To reverse the rows and array".center(80, "-"))
print(two_dimension_array[1::])

print("To reverse the row and column positions".center(80, "-"))
two_dimension_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(two_dimension_array[::-1, ::-1]) #reverse the row and column position both
'''
[[9 8 7]
 [6 5 4]
 [3 2 1]]
'''

print("To present the missing values".center(80, "-"))
two_dimension_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
two_dimension_array[1, 1] = 55
two_dimension_array[2, 2] = 44
print(two_dimension_array)


numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
print(numpy_zeroes)
'''
[[0 0 0]
 [0 0 0]
 [0 0 0]]
'''

numpy_ones = np.ones((3,3), dtype=int, order='C')
print(numpy_ones)
'''
[[1 1 1]
 [1 1 1]
 [1 1 1]]
'''

#Only ones and zeros two built-in methods

