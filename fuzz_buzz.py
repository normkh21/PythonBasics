# Fuzz - Buzz problem

# accept a number from the user - input(), int()
# if that number is divided bt 3 print ('fuzz')
# if that number is divided by 5 print ('Buzz')
# if that number is dividable by 3 and5 print ('Fuzzbuzz'



for i in range(3):
    num = int(input('Enter your Number:'))
    if num % 3 == 0 and num % 5 == 0:
        print('Fuzz Buz')
    elif num % 3 == 0:
        print('Fuzz')
    elif num % 5 == 0:
        print('Buzz')

# ## **** ALTERNATIVE ******
# for i in range(3):
#     num = int(input('Enter your Number:'))
#     if num % 3 == 0 and num % 3 <= 0:
#         print('Fuzz')
#     if num % 5 == 0 and num % 5 <= 0:
#         print('Buzz')
#     if num % 3 == 0 and num % 5 == 0:
#         print('Fuzz Buzz')

bin_num = bin(45)
print(bin_num)



