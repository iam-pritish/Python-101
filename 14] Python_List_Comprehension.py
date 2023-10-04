# What is List-Comprehension??
# # Write a program to generate a list of 10 numbers

result = []
for i in range(1,11):
    result.append(i)

print(result)                                        #--->[1,2,3,4,5,6,7,8,9,10]

# How to Do it with the helo of "List Comprehension"?

result = [ x for x in range(1,11)]                   #---> NewList = [expression (x) for x in OldList if check]
print(result)                                        #--->[1,2,3,4,5,6,7,8,9,10]

# Get a list of all even numbers between 1 to 50 
result = [ x for x in range(1,51) if x % 2 == 0]
print(result)                                       #--->[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

# Get a list of all even numbers from given list
list_a = [1,2,4,3,6,7,9]
result = [  x for x in list_a if x % 2 == 0  ]
print(result)                                       #--->[2, 4, 6]

# Conver all String in given list to Upper case using List-Comprehension
list_str = ['hi','hello',"how's going",'go','see you','bye']

result = [x.upper() for x in list_str]
print(result)                                       #--->['HI', 'HELLO', "HOW'S GOING", 'GO', 'SEE YOU', 'BYE']

# Put all '-ve' numbers after '+' ve numbers from given list??

# gereral way of Doing It.
list_n = [1,-1,2,5,-6,9,19,-10,10]
result1 = [x for x in list_n if x > 0]
result2 = [x for x in list_n if x < 0]

print(result1+result2)

# Another way of doing It.

result = [x for x in list_n if x > 0] + [x for x in list_n if x < 0]
print(result)

#  Same result will get = [1,2,5,9,10,19,-1,-6,-10]
