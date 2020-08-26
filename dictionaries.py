# DICTIONARIES - data stricture, mutable, {key1: value1, key2: value2 }
    # in java > HashMap, HashTable, Hashset >> hashing algorithm to store the key -value pairs
# recap: list - data strucutre, mutable [a,b]
cars = ['lexus', 'bugatti', 'bmw', 'ferrari']
#recap: Tuple - data strucutre, immutable, (a, b)
cars = ('lexus', 'bugatti', 'bmw', 'ferrari')

# Stores the values as key-value pair
# Does not guarnatee the order
# Must Know:
# create, Access modify (add element, remove elements, reset ), loop through elements
students = {} # empty dictionary
students1 = dict() # creates empty dictionary, converts to a dictionary

student1 = {'name': 'Hamza', 'gpa':  3.8}
student2 = {'name': 'Alexa', 'gpa': 3.9}

#cars[0]

# Accessing the Values of Dictionary, as in ist with >> cars [0]
print(student1)
print(student1['name'], student1['gpa'])
print(f"Next student is {student2['name']} with GPA = {student2['gpa']}")

# assigning the valu
student1['gpa'] = 3.7  # if key is existing this will reset the value, new gpa=3.7
print(student1)
student1['state'] = 'NY'
print(student1)
print(sorted(student1)) # only sorted keys are printed as a list

del student1['state']
print(student1)


