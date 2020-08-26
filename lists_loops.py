# # Chapter 4: Working with LISTS
# states = ['New York', 'New Jersey', 'Connecticut', 'California']
# # Loops - within loops you create repetitive actions
#
# # for variable in list_of_elements:
# #    repetitive code here
#
# for state in states:
#     print(f"Welcome to {state}!!")
#     # pass # do nothing
#
# # THINGS TO REMEBER WHILD WORKING WITH LOOPS
# # colon at the end of 'for' line
# # 'in' in the 'for' line
# # give any name to a variable and use that varible inside the for loop code
# # lines of code that belongs to for loop (repetitive code) must be indented
# # # Always Check your indentation
#
#
# # states > 4 members >>
# #   >> 1st Loop/round >> state = 'New York'  -- python does this
# #   >>print(f"Welcome to {state}!!")        -- we will write this code
# #   >> Welcome to New york !!               -- This is execution
#
# #  >> 2nd loops/round >> state =='New Jersey'
# #   >> print(f"Welcome to {state}!!")           ---- this code we will write
# #   >> Welcome to New Jersey
#
# print(states)
# # PyCharm: refactoring >> Shift +f6
#
# # print(state)  # outside  of the scope  of Variable
#
# # SCOPE  >> where it belongs to / life of the code
# for state in states:
#     print(f"Welcome to {state.upper()}!!")
#
# print(f" Enjy your trip in {state} ")  # outside of Loop, independent
#
# print(state)  #Incorrect: outsdie of the scope of variable
#
# ### EXCERCISE ------ 4.1-------
# print()
# pizzas =["Regular Pizza", "Buffalo Pizza", "Peparoni Pizza"]
# for pizza in pizzas:
#     print(f"I really love {pizza}")
# print("I really love pizza")
#
# #HW 4-2
#
#
# # Marketing Numerical List
# for num in range(5): # from 0 to 4
#     print(f"My current number: {num}")
#
# for num in range(3,6): # from 3 to 5
#     print(f"my current number from range(3,6): {num}")
#
# # list(iterable) - mutable >> [4, 6, 12}
# # tuple - mutable >> 94,6,12) - immutable
#
# friends = list()
# students = []  ## Empty list
# numberss = list(range(5)) #   1. range >> 0,1,2,3,4   2. list() >> [0,1,2,3,4]   3.. numbers = [0,1,2,3,4]
# print(range(5))
#
#
# # print squares of numbers from 5 to 10
# print()
# squares = [] # squares = list()
# for num in range(5, 13):
#     num_sqr = num ** 2
#     # squares.insert(-1, num_sqr)
#     squares.append(num_sqr)
#      # print(num_sqr)
#     # print(squares)
# print(squares)
#
# squares = list() # resetting the list to empty list
# for num in range(5, 13):
#     squares.append(num ** 2)
# print(squares)
#
# numberss =[5, 78, 456, 127, 230, 6, 5]
# # min(list) , max(list), sum(list)
# print(f" Min numbers from numbers : {min(numberss)}")
# print(f" Max numbers from numbers : {max(numberss)}")
# print(f" sum numbers from numbers : {sum(numberss)}")

# # list comprehensions
# squares[]
# for num in range(5, 14,:  #STEP
#     squares.append(num ** 2)


# # FYI
# # squares = list(num ** 2 for num in range(5,13))
# squares = [num ** 2 for num in range(5, 14, 2)]
# print(squares)
#
# for num in range(1, 1000001):
#     pass
#     #code tp create a list
# print(min(num))
# print(max(num))
# print(sum(num))
# print(sum(num) / len(num))

numberss = list(range(1, 1000001))
print(f"Min number is: {min(numberss)}")
print(f"Max number is: {max(numberss)}")
print(f"sum number is: {sum(numberss)}")

# HW 4-6, 4-7, 4-8, 4-9

# Slicing the list
numbers = [5, 78, 456, 127, 230, 6, 5]
print(numbers[:3]) # indexes >> 0, 1, 2
print(numbers[0:3])

print(numbers[3:]) # from 3rd index to end of the list
print(numbers [1:-2]) # from 1st index(second element) to second from the end
new_numbers = numbers # this is linking the numbers_copy to numbers list
# if numbers is modified numbers_copy will be effected

numbers_copy = numbers[:] # copying the list to a new list

print("# copying the lists example")
print(numbers, new_numbers, numbers_copy)
numbers.append(5555)
print(numbers, new_numbers, numbers_copy)

# HW 4-10,  4-11, 4-12


