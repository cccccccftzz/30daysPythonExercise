# Dictionary

print("Catch up in Preview".center(80, "-"))

"""#Creating a empty Dictionary 
Different from set
fruits = set () #Creating an empty set
"""
dct = {}
print(type(dct))

dct = {
    "first_name": "Fang Ting",
    "last_name": "Chen",
    "age": 30,
    "Country": "China",
    "is_married": False,
    "skills": ["Gym", "cook", "paint"],  # Dictionary can store list
    "address": {
        "street": "Beach Road",
        "zipcode": "500045",
    },  # Dictionary can store subdictionary
}
print(dct)

print(len(dct))  # To check the nos of keys

print(dct["age"])
print(dct["address"])
print(dct["skills"][2])  # To give index only after using dct['key'][index]
# print (dct['city']) If cannot get the key in the dictionary, by using index it will return error

print(dct.get("first_name"))
print(
    dct.get("city")
)  # By using get, even the key is not available in the dictionary, it returns None

# Adding Items to a Dictionary
dct["job_title"] = "Designer"
dct["skills"].append("programming")  # To add into list in the end
dct["address"][
    "lane"
] = 48  # To add one key into the subdictionary inside the main dictionary
print(dct)

# Modifying Items in a Dictionary
dct["age"] = 18
print(dct)
dct["address"]["lane"] = 55
print(dct)

# Checking Keys in a Dictionary
print("skills" in dct)  # To the key as string

# Removing Key and Value Pairs from a Dictionary
dct.pop("age")
print(dct)  # Remove age
dct.popitem()
print(dct)  # Remove job title
del dct["address"]
print(dct)  # Remove address

# Changing Dictionary to a list of items
print(dct.items())  # Few tuples inside a list
print(type(dct.items()))  # New Type Dictionary items!!

# print (dct.clear())

# del dct

# Copy a Dictionary
person = dct.copy()
print(person)

# Getting Dictionary Keys as a List by keys()
key_of_person = person.keys()
print(key_of_person)

print("Exercise 1".center(80, "-"))
# Create an empty dictionary called dog
dog = {}
print(dog)

print("Exercise 2".center(80, "-"))
# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Feifei"
dog["color"] = "Yellow"
dog["breed"] = "Asian"
dog["age"] = 8

print(dog)
print(len(dog))

print("Exercise 3".center(80, "-"))
student = {
    "first_name": "Fang Ting",
    "last_name": "Chen",
    "gender": "female",
    "age": 18,
    "marital status": "single",
    "skills": ["Gym", "cook", "paint"],
    "country": "China",
    "city": "Shanghai",
    "address": "Beach Road",
}

print("Exercise 4".center(80, "-"))
print(len(student))

print("Exercise 5".center(80, "-"))
print(student["skills"])
print(type(student["skills"]))

print("Exercise 6".center(80, "-"))
student["skills"].append("driving")
student["skills"].append("programming")

print(student["skills"])

print("Exercise 7".center(80, "-"))
keys = student.keys()
print(keys)

print("Exercise 8".center(80, "-"))
values = student.values()
print(values)

print("Exercise 9".center(80, "-"))
list_student = student.items()
print(list_student)

print("Exercise 10".center(80, "-"))
del student["age"]
print(student)

print("Exercise 11".center(80, "-"))
del student
