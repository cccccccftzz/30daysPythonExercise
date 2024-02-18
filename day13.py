print("Catch up in Preview".center(80, "-"))

print("Exercise 1".center(80, "-"))
print("Filter only negative and zero in the list using list comprehension")
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero_numbers = [i for i in numbers if i <= 0]
print(negative_and_zero_numbers)

print("Exercise 2".center(80, "-"))
print("Flatten the following list of lists of lists to a one dimensional list")
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
output = []
for i in list_of_lists:
    for ii in i:
        print(ii)
        output += ii
        # output.append(ii) # append to be like a adding one argument to the original list
        # += means extend, means merge two lists tgt, like flatten
print(output)

print("two layers lists only".center(80, "-"))

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output_1 = [mem for inner_lst in list_of_lists for mem in inner_lst]
print(output_1)

print("Chatgpt method for 3 layers lists ".center(80, "-"))
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [
    item for sublist in list_of_lists for subsublist in sublist for item in subsublist
]
print(flattened_list)

print("Exercise 3".center(80, "-"))
print("Using list comprehension create the following list of tuples:")

flattened_list = [
    (i,) + tuple((i**power) for power in range(0, 6)) for i in range(0, 11)
]
"""
1. Rmr change the list to tuple when joining a tuple : tuple(), it is () not []
2. (i,) + tuple(xxxx) is another way to define a tuple
"""
print(flattened_list)

# To change it in normal for loop without list comprehensive
result_list = []
for i in range(11):
    tuple_values = (i,)
    for power in range(6):
        tuple_values += (i**power,)
    result_list.append(tuple_values)

print(result_list)

print("Two ways to concentrate tuples".center(80, "-"))

print("\n")
print("Using concatenation with tuples (not recommended)")
result_tuples = tuple((i,) + tuple(i**power for power in range(6)) for i in range(11))
print(list(result_tuples))

print("\n")
print(
    "Using list accumulation and conversion to tuple (recommended), \nbut inside every tuple, still using the tuple concatenation"
)
result_list = [(i,) + tuple(i**power for power in range(6)) for i in range(11)]
print(result_list)
print("\n")

print("if wanna list type output")

"""
There is no way to use list accumulation 
to output a list of tuples by converting in the mid way
so the tuple accumulation in each tuple is not able to be avoided.
"""

print("Exercise 4".center(80, "-"))
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
print("My own script".center(80, "-"))
flattened_list = [
    [item[0].upper() for sublist in countries for item in sublist],
    # [first_three_letters for sublist in countries for item in sublist for first_three_letters in item[0][0:3]],
    ["".join(item[0][0:3]).upper() for sublist in countries for item in sublist],
    [item[1].upper() for sublist in countries for item in sublist],
]
print(flattened_list)
# The result are reading the each index member by index.
# Not the targeted output. So wrong. See GPT method below

print("Chatgpt method".center(80, "-"))
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
flattened_list = [
    [country.upper(), country[:3].upper(), capital.upper()]
    for sublist in countries
    for country, capital in sublist
]
# Can use two variable names for the tuple item 1 & 2
print(flattened_list)

print("Exercise 5".center(80, "-"))
print("Change the following list to a list of dictionaries.")
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
output = [
    {"country": country.upper(), "city": capital.upper()}
    for sublist in countries
    for country, capital in sublist
]
print(output)

print("Exercise 6".center(80, "-"))
print("Change the following list of lists to a list of concatenated strings:")
names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]
output = [" ".join(item[:2]) for sublist in names for item in sublist]
print(output)

print("Exercise 7".center(80, "-"))
print(
    "Write a lambda function which can solve a slope or y-intercept of linear functions."
)
slope_between_two_points = lambda a, b: (b[1] - a[1]) / (b[0] - a[0])
print(slope_between_two_points((3, 6), (8, 2)))
