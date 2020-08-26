# looping dictionaries and more
student1 = {'name': 'Hamza', 'gpa':  3.8, 'lastName': 'Hamrakulov'}
student2 = {'name': 'Alexa', 'gpa': 3.9, 'lastName': 'Moseyeva'}

# looping with keys
for key in student1:
    print(' key is:', key)

print()

for key in sorted(student1.keys()):
    print('key is:', key)

# for info in  student1.keys():
for key in student1:
    print('value is:', student1[key])

for value in student1.values():
    print('value is', value)

print()
# Looping the values
for dkey, dvalue in student1.items():
    print('key is', dkey)
    print('value is ', dvalue)

print("Nesting dictionaries in LIST ")
class_2020 = [student1, student2]
print(class_2020)
for student in class_2020:
    print('Name of the student:', student['name'])
    print('GPA of student:', student['gpa'])
    print('Last name of student:', student['lastName'])
    print("------------------------------------")

print("****** Nesting dictionaries in Dictionaries")

dclass_2020 = {'student1': student1, 'student2': student2}
print(dclass_2020)
for key, value in dclass_2020.items():
    print('Key of the element: ', key)
    print('Value of the element: ', value)
    print('Name of the student: ', value['name'])
    print('GPA of the student: ', value['gpa'])
    print('Last Name of the student: ', value['lastName'])

    print("----------------")

#
#
# print()
# print('Excercise 6-5')
# rivers = {'nile': 'egypt:', 'hudson' : 'usa:', 'volga':  'russia:', 'mississippi' : 'usa', 'thames': 'uk'}
#
# # The KEY runs through Value
# for river, country in rivers.items():
#     # if country == 'usa' or cuntry == 'uk'
#     if country in ['usa', 'uk']:
#          print(f"The {river.title} runs through {country.upper()}")
#     else:
#         print(f"The {river.title} runs through {country.title()}")
#
# print('Rivers are: ')
# for river in rivers.keys():
#     print('\t',  river.title)
#
# print('Countires are: ')
# for  country in sorted(rivers.values(), reverse=True):
#     if country in ['usa', 'uk']:
#         print('\t', country.title())
#     else:
#         print('\t', country.upper(), end=" | ")
#
#
