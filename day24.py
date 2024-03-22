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

twoes = numpy_ones * 2
print(twoes)

print("reshape".center(80, "-"))
#reshape
first_shape = np.array([(1, 2, 3), (4, 5, 6)])
print(first_shape)

reshaped = first_shape.reshape(3, 2)
print(reshaped)
'''
[[1 2 3]
 [4 5 6]]
'''

print("Flatten".center(80, "-"))
#Flatten
flattened = reshaped.flatten()
print(flattened) #[1 2 3 4 5 6]

print("Horizontal stack".center(80, "-"))
#Horizontal stack
np_list_one = np.array([1, 2, 3])
np_list_two = np.array([4, 5, 6])
print(np_list_one + np_list_two) #[5 7 9]
print(f'{np.hstack((np_list_one, np_list_two))}') #[1 2 3 4 5 6]

print("Vertical Stack".center(80, "-"))
print(f'{np.vstack((np_list_one, np_list_two))}') 
'''
[[1 2 3]
 [4 5 6]]
'''

print("Generating Random Numbers from random module".center(80, "-"))
random_float = np.random.random()
print(random_float) #Just Generating ONE random float

random_float = np.random.random(5) #random() method, () stands for how many array number to be generated
print(random_float) #Generating as an array

random_int = np.random.randint(0, 11) #randint() method, () stands for a range
print(random_int)  #4

random_int = np.random.randint(0, 11, size=4) #randint() method: size meaning array number
print(random_int)  #[4 4 7 8]

random_int = np.random.randint(0, 11, size=(4, 2)) #4 rows, 2 cols array with random integer between 0~10
print(random_int)  #[4 4 7 8]

print("Generating Random Numbers from random module".center(80, "-"))
#Syntax:: np.random.normal(mu, sigma, size)
#mu:Mean (“centre”) of the distribution.
#sigma: Standard deviation (spread or “width”) of the distribution. Must be non-negative.

normal_array = np.random.normal(79, 15, 80)
print(normal_array)
'''
[ 90.80079252  78.28596759  78.02159718  76.41257498  71.60812818
  74.58027718  72.07787582  77.02227712  65.50652843  95.75141089
  97.90239649  54.271475    94.60833075  77.70214143 100.44400474
  78.00670482  76.81492309 107.82887331  92.99657298 100.78859393
  72.98039648  52.87398747  83.62999237  77.25617463  91.84559147
  85.39318451  92.38351696 101.20135841  82.47665509  76.52953816
  99.79583091  77.97359494  79.7813125   80.75846543  70.10124675
  72.48559649  75.17983081  76.73384076  62.24472454 128.63969039
 108.85576976  83.62069328  66.31557409 101.81045652  82.3641682
  68.05802968  63.77363631  78.13851672  71.07645789  81.18273882
  89.53894159  61.43266238  69.7722646   95.98699009  85.22723222
  90.18878734  73.45521083  74.17731291  82.25263192 105.18997118
  86.63445031  71.4219817   58.71226309  81.9507365   65.37687365
  65.18232687  71.95241714  55.17432759 115.39346808  94.04932081
  76.40173586  51.36004233  55.76281688  46.68250778  77.25581026
  61.53101846  53.8255023   62.38371     97.67199102  77.03840507]
'''
#The set of number mean value is 79, the standard devision is 15, and total 80 numbers


print("Numpy and Statistics".center(80, "-"))
#To use the matplot and seaborn module to visualize a set of data

import matplotlib.pyplot as plt 
#This module provides a MATLAB-like plotting framework in Python.

import seaborn as sns 
#seaborn is a statistical data visualization library built on top of Matplotlib.

plt.hist(normal_array, color='grey', bins=50)
#color: You can specify any valid color name or a hexadecimal color code.
#bins: This argument specifies the number of bins (or bars) to use in the histogram

# plt.show() #To type this row to see the histogram plot


print("Matrix in numpy".center(80, "-"))
four_by_four_matrix = np.matrix(np.ones((4, 4), dtype = float))
print(four_by_four_matrix)
'''
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
'''

print("Numpy numpy.arange()".center(80, "-"))
#To create values that are evenly spaced within a defined interval

#Normal list: range(starting, stop, step)
lst = range(0, 11, 2)
for i in lst:
    print(i) #0, 2, 4, 6, 8, 10

#To get as an Array: numpy.arrange(starting, stop, step)
whole_numbers = np.arange(0, 20, 1)
print(whole_numbers) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
odd_numbers = np.arange(1, 20, 2) 
print(odd_numbers) #[ 1  3  5  7  9 11 13 15 17 19]

print("Creating sequence of numbers using linspace".center(80, "-"))

#numpy.linspace()
#To create 10 values from 1 to 5 evenly spaced.
linspace_example = np.linspace(1.0, 5.0, num=10)
print(linspace_example) #[1.         1.44444444 1.88888889 2.33333333 2.77777778 3.22222222 3.66666667 4.11111111 4.55555556 5.        ]

#Not to include the last value in the interval but still with 10 spaces
linspace_example = np.linspace(1.0, 5.0, num=10, endpoint=False)
print(linspace_example)

#numpy.logspace() in python with example
#To return 