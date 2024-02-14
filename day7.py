# Set

print("Catch up in Preview".center(80, "-"))

# Creating an empty set
fruits = set()  
print(type(fruits))
fruits = {"banana", "orange", "mango", "lemon"}
print(len(fruits))

# Adding Items to a Set
fruits = {"banana", "orange", "mango", "lemon"}
fruits.add("lime")
print(fruits)

# Add multiple items using update()
fruits = {"banana", "orange", "mango", "lemon"}
fruits.update("tomato", "potato", "cabbage")
"""
Typical Mistakes, update() only take ONE LIST Argument!!
If multiple strings, then only update as individual character!
"""
print(fruits)
print(type(fruits))

fruits = {"banana", "orange", "mango", "lemon"}
vegetables = ["tomato", "potato", "cabbage"]  # Only can adding one list one argument
fruits.update(vegetables)
print(fruits)

# Converting List to Set
fruits = ["banana", "orange", "mango", "lemon"]
fruits_set = set(fruits)
print(type(fruits_set))

fruits = {"banana", "orange", "mango", "lemon"}
vegetables = {"tomato", "potato", "cabbage"}
print(fruits.union(vegetables))  # Union is for creating a new set
print(fruits)
print(vegetables)

# Difference between .union() and .update()
fruits.update(vegetables)
print(fruits)  # To add in vegtables into set fruits

# Finding Intersection Items
fruits_one = {"banana", "orange", "mango", "lemon"}
fruits_two = {"durian", "apple", "mango", "lemon"}
intersection_list = fruits_two.intersection(fruits_one)
print(intersection_list)

# Checking Subset and Super Set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(
    whole_numbers.issubset(even_numbers)
)  # A.issubset(B), A is the subset of B -> False
print(whole_numbers.issuperset(even_numbers))  # True

# Checking the Difference Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers))  # A.differece(B), A\B

# Finding Symmetric Difference Between Two Sets (A\B) ∪ (B\A)
python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
print(python.symmetric_difference(dragon))  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}

# Joint / disjoint Sets
print(python.isdisjoint(dragon))

even_numbers = {0, 2, 4, 6, 8, 10}
odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers.isdisjoint(even_numbers))

print("Exercise Level 1".center(80, "-"))
# Given Sets:
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Exercise 1".center(80, "-"))
print(len(it_companies))

print("Exercise 2".center(80, "-"))
it_companies.add("Twitter")
print(it_companies)

print("Exercise 3".center(80, "-"))
it_companies.update(
    "Lazada", "Tiktok", "Shoppee"
)  # Typical Mistakes, update() only take ONE LIST Argument!!
print(it_companies)
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
it_companies.update(["Lazada", "Tiktok", "Shoppee"])
print(it_companies)

print("Exercise 4".center(80, "-"))
# print (it_companies.remove('Lazada')) #Result is None bc it altered the original list not give a new set
it_companies.remove("Lazada")
print(it_companies)

it_companies.discard(
    "Lazada"
)  # .discard() will not pop out the Error even if the result didnt find in the set
print(it_companies)

print("Exercise Level 2".center(80, "-"))
# Given Sets:
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Exercise 1".center(80, "-"))
# Join A and B
A.update(list(B))
print(A)

print("Exercise 2".center(80, "-"))
# Find A intersection B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.intersection(B))
print(A)
print(B)

print("Exercise 3".center(80, "-"))
# Is A subset of B
print(A.issubset(B))  # True
print(A)
print(B)

print("Exercise 4".center(80, "-"))
# Are A and B disjoint sets
print(A.isdisjoint(B))  # False
print(A)
print(B)

print("Exercise 5".center(80, "-"))
# Join A with B and B with A
A_B = A.union(B)
B_A = B.union(A)
print(A_B)
print(B_A)

print("Exercise 6".center(80, "-"))
# What is the symmetric difference between A and B
print(A.symmetric_difference(B))
print(A)
print(B)

print("Exercise 7".center(80, "-"))
# Delete the sets completely
del A
del B

print("Exercise Level 3".center(80, "-"))
# Given Sets:
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Exercise 1".center(80, "-"))
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(
    f'The Set length {'is' if len(age) > len(age_set) else 'is not'} than the list length.'
)
print(len(age))
print(len(age_set))  # 5
"""
When coverting to the set
it will auto delete the duplicate items! 
set can only store unique items
"""

print("Exercise 2".center(80, "-"))
# Explain the difference between the following data types: string, list, tuple and set

print("Exercise 3".center(80, "-"))
sentence = "I am a teacher and I love to inspire and teach people."
sentence_word = sentence.split()
print(sentence_word)
print(len(sentence_word))
print(len(set(sentence_word)))
