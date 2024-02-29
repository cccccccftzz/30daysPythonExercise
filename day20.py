# PIP

print("Catch up in Preview".center(80, "-"))

#PIP stands for Preferred installer program

#My pip version :pip 23.2.1 

#Installing packages using 'pip <packagename>'
#Uninstalling packages using 'pip uninstall <packagename>'

#To check all installed pip by 'pip list'

#To show information about a package 'pip show <packagename>'

# Package - numpy
# To check the pip module version by' pip show numpy'
import numpy
'''
Name: numpy
Version: 1.26.3
Summary: Fundamental package for array computing in Python
'''
lst = [1, 2, 3, 4, 5]
np_arr = numpy.array(lst) #To convert a list to an array in python
print(np_arr) #[1 2 3 4 5]
print(len(np_arr)) #5

print(np_arr * 2) #[ 2  4  6  8 10]

print(np_arr + 2) #[3 4 5 6 7]

'''The spacing is not indicative of any specific property or difference in the array's data; 
it's purely for presentation purposes'''

# Package - pandas 
'''
Name: pandas
Version: 2.1.4
Summary: Powerful data structures for data analysis, time series, and statistics
'''

# Web browser module - can open any website 
import webbrowser
url_lists = [
    'http://www.python.org',
    'www.linkedin.com/in/fangting-chen-8a5112125',
    'https://github.com/cccccccftzz',
]

for url in url_lists:
    webbrowser.open_new_tab(url) #in any default webbrowser

print("Reading from URL".center(80, "-"))

