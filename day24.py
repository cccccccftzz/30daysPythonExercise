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
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print(f'{first_row}') #[1 2 3]
print(f'{second_row}') #[4 5 6]
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

#Because the following script still includes one more diagram, so comment this line to avoid showing and interupt
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
logspace_example = np.logspace(2.0, 4.0, num=4)
print(logspace_example) #[  100.           464.15888336  2154.43469003 10000.        ]
#it generates 4 numbers spaced evenly on a logarithmic scale between 10^2 and 10^4

#To plot out the concept and values to illustrate the logspace function
import numpy as np
import matplotlib.pyplot as plt

# Compute the values
start = 2.0
stop = 4.0
num = 4
indices = np.arange(num)
values = 10**(start + indices * (stop - start) / (num - 1))

# Plotting
# plt.figure(figsize=(8, 6))
# plt.plot(indices, values, marker='o', linestyle='-')
# plt.title('Values on Logarithmic Scale')
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.xticks(indices)
# plt.grid(True)
# # plt.show()

#To check the size of any array
x = np.array([1, 2, 3], dtype = np.complex128)
print(x) #[1.+0.j 2.+0.j 3.+0.j]

'''The dtype parameter specifies the data type of the array. 
np.complex128 indicates that the array should contain complex numbers with 128-bit precision.
Since the array x contains complex numbers, each number is printed in the format a+bj, 
where a is the real part and b is the imaginary part. 
In this case, the imaginary part is 0 for all elements, 
so it's just a+0j, which simplifies to a'''

print(x.itemsize) #16
'''To return the size of a single array element in bytes. np.complex128 has a size of 128 bits, 
which is equivalent to 16 bytes (1 byte =  8 bits).'''

print("NumPy Statistical Functions with Example".center(80, "-"))
np_normal_dis = np.random.normal(5, 0.5, 100)
print(np_normal_dis)

two_dimension_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(f'{two_dimension_array.min() = }')
print(f'{two_dimension_array.max() = }')
print(f'{two_dimension_array.mean() = }')
print(f'{two_dimension_array.std() = }')


print(f'{two_dimension_array = }')
'''
np.max(): This function takes multiple arrays as arguments and returns the maximum of all the elements.
np.amax(): This function is an alias for np.max(). It behaves exactly the same way as np.max().
'''

print(f'=== Row ===')
print(f'Row with minimum: {np.amin(two_dimension_array, axis=0)}') #Column with minimum: [1 2 3]
print(f'Row with maximum: {np.amax(two_dimension_array, axis=0)}') #Column with maximum: [7 8 9]
print(f'Row with maximum: {np.max(two_dimension_array, axis=1)}') #Column with maximum: [7 8 9]
print(f'=== Column ===')
print(f'Column with minimum: {np.amin(two_dimension_array, axis=1)}') #Row with minimum: [1 4 7]
print(f'Column with maximum: {np.amax(two_dimension_array, axis=1)}') #Row with maximum: [3 6 9]

print("To create repeating sequences".center(80, "-"))
a = [1, 2, 3]

#Repeat whole of 'a' two times
print(f'Tile: {np.tile(a, 2)}') #Tile: [1 2 3 1 2 3]

#Repeat each element of 'a' two times 
print(f'Repeat: {np.repeat(a, 2)}') #Repeat: [1 1 2 2 3 3]

print("To generate random numbers".center(80, "-"))
#One random number between [0, 1)
one_random_num = np.random.random()
print(one_random_num)

#Random numbers between [0,1) of shape 2, 3
array_random_num = np.random.random(size=[2,3])
print(array_random_num)
'''
[[0.01438347 0.53018921 0.758398  ]
 [0.11995643 0.88860391 0.42871238]]
 '''

#random choice among few strings
random_choice = np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10)
print(random_choice) #['e' 'a' 'a' 'e' 'u' 'o' 'o' 'i' 'a' 'e']

combined_random_choice = ''.join(random_choice)
print(combined_random_choice) #iuauuuuuaa, just to join the character and output as one string

array_random_choice = np.array([combined_random_choice])
print(array_random_choice) #['iaauoeiuuo'], to join into a string but convert to an array including one element

#Random numbers between including negative
random_neg = np.random.randn(2,2)
print(random_neg)
'''
[[ 0.61563571 -0.03991531]
 [-0.24975162  0.55968014]]
 '''

 #Random integers between [0,10) of shape 2,5
rand_int = np.random.randint(0, 10, size=[5,4])
print(rand_int)

'''[[8 1 6 0]
 [9 8 3 7]
 [2 8 5 7]
 [8 7 1 9]
 [5 4 2 9]]'''

rand_int = np.random.randint(-1, 10, size=[5,4])
print(rand_int)
'''
[[-1  5  2  2]
 [ 1  4  0  2]
 [ 7  3  0  4]
 [ 5  3  8  6]
 [ 3  0  7  7]]'''

from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
print(np_normal_dis)
'''[4.99546549 4.66725035 4.78255402 5.51136884 5.24827863 4.40564177
 5.10613319 5.48827654 4.95152608 5.94817414 5.4389035  4.1655341
 4.63152593 3.98462463 4.27154552 3.89537752 5.18866083 4.93496092
 5.24229475 3.96499062 5.71226698 4.80378795 5.79504971 5.11177002
 3.90789474 5.32237812 5.81079787 4.50458944 4.87598489 6.0580581
 4.31703638 5.68417007 4.48688895 4.98114722 4.80735195 5.37708779
 4.84380773 5.4457797  4.95371186 5.62706304 5.21978485 4.71831707
 4.90936271 5.46109027 4.35019697 5.56427841 5.35138604 5.5400904
 5.48892754 5.60821461 5.86168268 4.80468784 4.89709392 4.81625827
 4.91760414 5.47949349 5.74593074 4.56571511 4.97085768 4.9916194
 5.43756445 5.03484279 5.08267313 4.6527888  5.38741203 5.1050018
 5.10218223 5.12213474 4.35859663 4.6762554  4.85148058 4.27899811
 4.33209916 4.82834922 4.75727645 5.45980792 5.40073624 4.64552709
 4.25080528 4.57315092 4.58780409 5.54929271 5.59936376 4.32723651
 5.45837187 5.29568189 4.06175141 4.8488743  4.48569286 4.15087923
 5.38707618 5.5046073  4.10851188 5.03323233 4.58463992 5.93911867
 5.6965384  5.34114894 4.91270792 4.30869648 5.63253955 4.94913195
 4.55790246 5.31933645 4.2366903  4.71004862 5.39679265 4.82190467
 4.87438544 5.27047277 4.96747192 5.16492436 5.2793731  5.47258847
 5.43573951 4.98250665 5.82105343 4.72412572 5.83386812 4.94509365
 4.72496348 4.59533596 5.39914693 5.09349064 4.31428044 5.02483783
 5.03327662 5.48953513 4.70762628 4.2344492  4.89318699 5.27057953
 5.43902302 5.04476178 5.25003567 4.67277219 4.49809035 4.79015018
 4.74678137 5.53629845 4.44578928 4.80916362 5.51611649 5.25066842
 4.98288121 4.2919589  5.10922631 5.29828276 5.25501929 5.63001707
 4.80462787 4.68417504 5.42124215 5.46703449 4.91925515 4.94361652
 5.13865525 4.77212566 4.98712347 4.95269343 4.78053932 4.46122157
 5.0476178  4.57827337 5.23699275 4.21030107 4.4104989  4.4428217
 5.71335711 4.80726992 5.44416285 4.98168705 4.42096267 5.86200844
 5.76626301 5.26701449 5.54622329 5.73793791 4.19221293 5.54168771
 4.81428085 4.7189249  4.42151911 4.90476748 4.6118225  5.92180966
 4.68882218 4.3539001  5.82545369 5.33917504 4.97288873 4.79682459
 5.06864508 4.89447387 4.69403931 4.72107342 5.62946003 5.80215343
 4.17838668 5.58289292 4.81812897 5.10305374 4.69801409 4.83202664
 5.06246979 5.00213362 5.12464907 5.14173005 5.39648319 5.11013024
 4.91502045 5.39362102 4.22015069 5.87563656 4.82868385 4.95883719
 5.17360619 4.93362089 4.8988998  5.63179092 5.1166936  5.67410843
 5.56076872 5.70377736 4.49334651 5.15324718 4.54125113 4.20863594
 4.88769963 5.46278368 4.61374407 4.92755364 4.88636803 5.63439561
 4.97356613 4.48565202 4.73020127 4.81041925 4.90010067 5.53210967
 4.86269375 4.22569923 4.66013329 6.19423903 5.63951092 4.70346463
 4.72578783 5.36249793 5.71374329 5.03391308 5.04671324 4.92524318
 5.77078953 4.72372006 4.86215812 4.90085686 4.90291906 4.70298666
 5.23724118 4.96517315 5.29837236 5.32971826 3.97334574 5.24612748
 5.49506553 5.07625888 6.08722325 4.10240405 4.66077651 4.60120035
 4.14602671 5.36037598 4.86984912 4.89354561 3.96959967 5.96401453
 4.66156161 5.32849604 5.09973194 5.29880899 4.96554607 4.99110974
 3.93950052 5.76227071 4.66432127 5.37334914 4.33577634 5.34278912
 5.43135256 5.37498874 5.0740689  5.01869254 6.00057047 5.00296973
 5.34171426 5.19592088 4.96779938 5.66168506 4.89519897 5.10409714
 5.23486273 5.1313104  4.82539639 4.77436543 5.68518183 4.83685089
 5.39916409 5.34310985 4.6921353  4.87008133 4.66204318 4.78547007
 4.65138346 4.24184207 4.96948217 5.16217217 5.00042639 5.00549944
 6.2045932  4.38838603 5.40810061 4.18249964 3.64796812 5.13311924
 4.50510118 5.07704748 5.21900411 4.628472   5.31944488 4.72857868
 5.18946767 4.81587233 5.26426035 5.14698847 5.03693413 4.88041358
 4.62024986 5.30215693 5.64494859 5.33723803 4.62574356 4.83615826
 4.98226936 5.00696277 4.6240898  5.24463416 5.31542584 4.7539687
 5.52290038 5.51575336 4.86133205 5.4010675  5.02484766 5.12205284
 4.4902945  5.30321115 5.29340048 4.19635258 4.68049151 5.67626812
 5.31006427 4.89573909 4.55532397 5.64388988 6.419496   4.3550991
 4.47575234 5.01528885 5.05584439 5.14465365 4.51651976 5.31277857
 5.28697976 5.1492991  4.43511544 4.63616867 5.14060513 5.4168782
 5.59142713 5.68326143 5.44359673 4.77457816 5.52445358 5.27373984
 5.76162191 4.06168625 5.59637291 4.16326404 5.63057522 4.73108527
 4.80578516 4.96062883 5.85632429 5.81700714 4.81566363 5.31761635
 4.73074948 4.80627122 5.42547136 5.35015058 5.35288409 4.96125581
 4.94172157 4.40348957 5.46539844 5.18997441 5.05708423 4.88580424
 5.07944507 5.97620302 5.02609267 5.12327735 6.20097999 5.35587431
 5.01192868 4.45494254 5.39918007 5.11919859 5.68633953 5.06695293
 5.52631239 6.03516429 4.69933494 4.65966588 5.15616422 4.98275907
 4.49856496 4.45354007 4.09585549 4.7415271  4.58971923 4.9759549
 5.56544479 4.62532762 5.00798539 4.9575477  4.12881326 6.19787009
 5.01793922 3.89928838 4.84550904 5.60193761 5.68459259 5.32348291
 5.49409587 4.99655372 5.42145209 5.36411263 4.45064182 5.7838677
 4.61791099 3.40155505 5.29641131 4.56510514 4.26008374 6.0964264
 4.78612748 4.55561081 4.78690247 4.60084081 4.6663154  4.67966345
 5.16295063 4.61226298 5.62744911 4.27858028 4.88310024 4.76614758
 4.75312857 4.9596733  5.58167528 5.47143521 5.07210864 3.91443191
 4.61402822 4.56232088 6.02631047 5.40282934 5.41019272 4.90211891
 4.93583098 5.2207646  4.25488522 5.25127454 4.25709949 4.3169583
 4.37152179 4.91897848 5.71063578 4.44861945 5.84579406 5.33931325
 4.85377849 4.67518666 5.6028836  4.62856595 4.85678637 5.49788784
 6.04196173 4.45528179 4.61270554 5.96603513 4.93991536 5.02149363
 5.08485069 5.27808934 5.81141223 4.89793674 4.75282881 4.79754889
 4.20788877 5.89353926 5.29688366 5.15863776 4.26622531 6.11566909
 5.54722853 5.45184924 5.10722189 5.50923628 5.80164733 4.73778516
 5.30009745 4.00724339 5.03444093 4.84268319 4.87232074 5.0841534
 4.20482018 4.07583729 5.16868485 5.02379666 5.00111095 4.41780639
 5.54696731 5.53605033 4.86236968 4.26965528 4.60011395 3.7456937
 5.16468582 4.78199364 5.01595098 4.98041253 4.03306447 4.48897497
 4.62111951 4.47646007 4.41410555 4.72082757 5.42765041 4.96610312
 4.03374511 4.61785874 5.24340077 5.64506043 4.04934871 4.80226601
 4.37192096 5.27372516 4.07038946 4.55286586 4.18544952 4.27354269
 5.59587218 4.47486582 4.47138148 5.16498586 5.13333728 5.10246186
 4.78262455 4.30943494 4.41624067 5.18532147 4.70858926 4.5485872
 5.38269214 4.11377936 5.00594409 4.77258916 4.26640252 5.12692211
 4.53311721 4.18021227 4.31879295 4.74106493 5.20904062 5.04521459
 5.17978855 5.04106919 6.05313884 5.13815193 4.41487065 4.60776173
 4.7554108  5.48753676 4.70357214 5.24205133 5.69779417 4.36716905
 4.0042756  4.81948289 5.40666669 5.18245827 5.0913085  5.15206527
 5.37710312 5.23769097 5.35947603 5.30159615 5.88453702 5.72064205
 4.3168401  3.8370599  4.48589291 4.87934397 5.45999124 5.43791336
 5.42143107 3.99920723 4.69091498 5.77381657 4.75161125 4.9585202
 5.25853662 4.90336498 4.59952578 5.11590397 4.54525957 5.16199735
 5.20167685 4.8029792  4.84350326 5.44183713 5.43643836 5.90436673
 4.75036572 5.4446983  5.76025675 5.07221495 5.19612247 4.18831364
 6.17718287 5.84826398 5.17976932 5.55626802 5.34931416 5.59693792
 5.71294697 5.68164492 4.33479293 4.68782177 4.59027995 4.38254135
 5.25373248 5.00862592 3.83393523 5.07967019 5.33232335 5.29593071
 5.33090377 5.50400061 4.9825689  4.22831098 4.47609453 4.38869461
 5.47679005 4.59867248 5.1006992  4.70347526 5.03752938 4.51522144
 5.01050603 4.70250187 5.22261569 4.06822275 5.15570414 4.55083554
 5.19195969 4.42746688 5.33415723 4.79385997 5.12853949 4.85870169
 4.93621261 4.65384677 4.69675852 5.15409462 4.89392069 4.25368465
 5.07689315 4.59249456 4.6526676  4.74270807 5.36106517 5.05040708
 4.85214204 4.67244604 4.9574788  4.83456528 5.81031613 5.03360663
 5.15675889 4.92239303 4.45685942 4.99892523 4.5463039  4.89428347
 5.36039547 4.7906672  4.76943785 5.6902819  5.32958899 5.34837102
 5.28047648 4.58450767 4.13318505 4.4991621  5.62942005 4.66556228
 4.29576424 4.49257309 4.83158017 4.76928917 4.56248206 5.09167054
 4.76565534 4.29694921 4.82998096 4.62581303 4.59776495 5.50186494
 4.93761594 4.8851419  5.74639763 5.02579766 5.23049768 4.85302572
 5.41567475 4.48246818 4.93606239 4.54706368 4.80576458 5.57437315
 4.7929109  4.79246336 4.78193124 4.74498206 5.74008218 4.67882001
 5.69266474 5.23412802 4.61583065 5.13793898 4.26192395 4.2383492
 5.27630267 5.35143032 5.05732223 4.74674995 4.64804855 4.78338644
 4.62469197 5.32239782 5.76264785 4.66769226 4.8101371  4.09127162
 5.76674827 4.89056813 4.74492546 5.55586829 4.86915088 5.49691152
 5.00780467 5.29757116 4.78163481 5.45046294 5.57930586 4.85753264
 5.0905395  5.71334655 5.29236754 4.97283731 4.78154783 5.2413048
 4.90826271 5.2912871  4.53467887 4.55586302 3.97275475 5.21616368
 5.26797925 5.00666445 4.96405022 4.52452285 4.68426142 4.05771993
 5.06698363 4.02676525 5.36450853 5.82050173 4.07957632 5.57280185
 5.57319464 4.71976713 4.70945738 4.37522496 5.29881038 4.70443307
 5.26104021 5.19526036 5.05612113 5.46862188 4.50497967 4.30937297
 4.53350725 4.36764464 5.58528872 5.46006787 4.54588538 4.9524235
 4.89725626 4.96663095 6.35082424 4.87675982 6.17926622 4.62890974
 5.00819649 5.30091087 5.63314571 4.81647982 5.23699067 6.15137683
 4.68051492 4.7875213  4.88588851 5.93711255 4.37799338 4.27424128
 4.62143891 4.97028214 5.01994773 5.10648247 4.19481918 4.98732308
 5.49094989 4.5452993  5.39083546 4.9234005  4.23563082 5.09764755
 4.98090005 4.87451239 5.51182434 4.49582683 5.0457385  5.67147537
 4.71608434 4.91194819 4.90978835 5.10088373 4.61521938 5.68129493
 5.6050801  4.78580853 4.8893963  4.35162875 4.61521552 4.86233748
 5.72988049 5.42252591 4.67805543 5.66193688 5.12855096 4.94700726
 4.38506749 5.6416678  5.99780244 4.87711219 4.36326533 4.44129305
 4.60123293 4.64811132 5.26899233 4.95769389 4.6340307  5.51163257
 5.62206172 5.28363262 4.94609846 5.40003972 5.22916344 4.75490312
 4.38740971 4.26664475 5.07467561 4.65989068 4.85202734 5.03134494
 4.08663188 5.08911244 4.38510116 4.8299716  4.55825465 5.22254156
 4.75244866 4.85992032 5.21585971 5.03821968 4.03893614 4.57050368
 4.62846752 4.65548773 4.90629782 5.4711614  5.44679096 4.48704326
 4.58261484 5.39306471 4.14371565 4.91519783 5.49528938 4.24910416
 5.37649557 4.48861916 5.3403884  5.62881814 4.62781683 4.87356804
 4.48642072 5.15369985 4.55154756 4.81907013 4.52689032 5.16638125
 4.79472819 4.57871774 5.72104011 5.29907956 5.29468871 5.32069968
 4.14748058 5.08154019 5.14492333 4.62112868 5.26466997 5.05299989
 5.05409451 4.07439589 5.73294891 4.97205348 4.47376933 4.79075787
 5.67491985 5.33477509 6.44891138 5.7065045  5.21521062 4.80242717
 5.23601554 4.48582385 5.74614841 4.72538018 5.03783178 5.3247189
 5.73656175 5.79910265 4.98912749 5.1396463  5.39710246 4.72107483
 4.77945861 6.01272649 5.20165748 4.64530657 5.08855337 5.11168
 4.21781538 4.53508047 5.62347672 5.10883056 5.20849616 4.69081007
 4.46648325 4.70681709 5.16341412 5.28819592 5.72216069 4.69600363
 5.41182432 4.4793983  4.58441053 5.22512787 5.69214068 5.00943208
 5.65227576 5.30237431 4.60576059 4.44554574]'''
print(f'{stats.mode(np_normal_dis) = }') #ModeResult(mode=3.4011733054941393, count=1)

'''the mode represents the value in the dataset that occurs with the highest frequency.
count:the count of occurrences of the mode value, which is 1 in this case. 
when there are multiple values with the same maximum frequency, 
the function returns the smallest value among them as the mode.'''

# plt.hist(np_normal_dis, color='grey', bins=21)
# plt.show()

print("Linear Algebra".center(80, "-"))
#numpy.dot(): Dot Product in Python using Numpy
f = np.array([1, 2, 3])
g = np.array([4, 5, 6])
# [1, 2, 3] * [4, 5, 6]
result = np.dot(f,g)
print(result) # 1*4+2*5 + 3*6 = 32

print("NumPy Matrix Multiplication with np.matmul()".center(80, "-"))
#Matmul: matruc project of two arrays
h = [[1, 2], [3, 4]]
i = [[5, 6], [7, 8]]
result = np.matmul(h, i)
print(result) 
'''
[1, 2]     [5, 6]           [1x5+2x7, 1x6+2x8]         [19, 22]
[3, 4]     [7, 8]    ->     [3x5+4x7, 3x6+4x8]    ->   [43, 50]
'''

#np.linalg.det(): Compute the determinant of an array
#for 2D array [[a, b], [c, d]] is ad - bc:
i = [[5, 6], [7, 8]]
result = np.linalg.det(i)
print(result) #-2

#For a stack of matrices
a = np.array([ [[1, 2], [3, 4]], [[1, 2], [2, 1]], [[1, 3], [3, 1]] ])
'''
[[1, 2]     [1, 2]     [1, 3]
[3, 4]]     [2, 1]     [3, 1]
'''
result_shape = a.shape
print(result_shape) #(3, 2, 2)

result= np.linalg.det(a)
print(result) #[-2. -3. -8.]


print("To set array with value by positioning" .center(80, "-"))
z = np.zeros((8, 8))
z[1::2, ::2] = 1
print(z)
'''
[[0. 0. 0. 0. 0. 0. 0. 0.]
 [1. 0. 1. 0. 1. 0. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0.]
 [1. 0. 1. 0. 1. 0. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0.]
 [1. 0. 1. 0. 1. 0. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0.]
 [1. 0. 1. 0. 1. 0. 1. 0.]]
step 1: 1::2 -> first element stands for row number rules: means from 2nd row, step 2rows, i.e. 2nd row, 4th row, 6th rows, 6th rows 
Then ::2 -> second element stands for column number rules: from 1st col, step 2ols, i.e, 1st col, 3rd col, 5th col, 7th col 
according to both positioning criteria, then to set the value as 1
'''
z[::2, 1::2] = 1
print(z)
'''
[[0. 1. 0. 1. 0. 1. 0. 1.]
 [1. 0. 1. 0. 1. 0. 1. 0.]
 [0. 1. 0. 1. 0. 1. 0. 1.]
 [1. 0. 1. 0. 1. 0. 1. 0.]
 [0. 1. 0. 1. 0. 1. 0. 1.]
 [1. 0. 1. 0. 1. 0. 1. 0.]
 [0. 1. 0. 1. 0. 1. 0. 1.]
 [1. 0. 1. 0. 1. 0. 1. 0.]]
 '''

print("Traditional plus minus in Array" .center(80, "-"))
new_list = [x + 2 for x in range(0, 11)]
print(new_list) #[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] by list comprehension
np_arr = np.array(range(0, 11))
print(np_arr + 2) #[ 2  3  4  5  6  7  8  9 10 11 12] by using array direct '+'

temp = np.array([1, 2, 3, 4, 5])
pressure = temp * 2 + 5
print(pressure)

# plt.plot(temp, pressure) #(x, y)
# plt.xlabel('Temperature in oC')
# plt.ylabel('Ptressure in atm')
# plt.title('Temperature VS Pressure')
# plt.xticks(np.arange(0, 6, step=0.5))
# # plt.yticks(np.arange(0, 20, step=0.5)) #if wanna specify the y axis scale also
# plt.show()

mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.displot(x)
ax.set(xlabel='x', ylabel='y')
plt.show()

