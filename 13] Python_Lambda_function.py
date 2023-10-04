# Lambda Fuction is Anonymous funtion - Which means this function is without Name
# Syntax : lambda arguments : expression
# Here This fuction can have ANY number of Arguments but only ONE Expression
# Lambda dunctions are syntactically restricted to single 
# How to create a Lambda Function

# Frist Normal function to add integre 5 in give number

def add_five(num):
    result = num + 5
    return result

x = 7
print("Five is added to this number:", (add_five(x)))

# Same Program with Lamda Function

lambda_add_five = lambda x : x + 5

y = 7

print("Five is added to this number:",(lambda_add_five(y)))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Difference Between Lambda functions and def defined function
def cube(y):
    return y*y*y
 
lambda_cube = lambda y: y*y*y
 
# using function defined
# using def keyword
print("Using function defined with `def` keyword, cube:", cube(5))
 
# using the lambda function
print("Using lambda function, cube:", lambda_cube(5))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Write a Lambda fuction to add two input number

lambda_add_two_nums = lambda m , n : m + n

a = 6
b = 7
print("Added Two Numbers 6 & 7 is:",lambda_add_two_nums(a,b))

# Write a lambda fuction to concatinate two strings

lambda_add_2_strings = lambda str1 , str2: str1 + str2

word1 = "Jason"
word2 = "Brody"
print(lambda_add_2_strings(word1, word2))

# Write a Lambda function to calculate maximum of given Two numbers?
# 1st Write in normal function
def max_two_nums(x,y):
    if x>y:
        return x
    else:
        return y

a = 9
b = 3
print(max_two_nums(a,b))

# Now Use Lambda Funtion

lambda_max_2_nums = lambda x, y: x if x>y else y

a = 77
b= 90
print(lambda_max_2_nums(a,b))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Here, the format_numric calls the lambda function, and the num is passed as a parameter to perform operations.

format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.5f}"

print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# How to use 
# 1] map() 
# 2] filter()
# 3] reduce()

# Implement map() Function

# To make Square of all numbers contain in the list with lambda fuction 

list1 = [11,12,13,14,15,16,17,18,19,20]

# Our expected Result will be [121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

sqr_num = lambda x : x * x
sqr_list = map(sqr_num,list1)  #---> This shows the result like this:- "<map object at 0x7fc98bf9d460>"

# To over-come that result we have to outcast the map fuction like below:

sqr_list = list(map(sqr_num,list1))
print(sqr_list)

# Add squential respective elements of two different lists
list_a = [4,5,6,7,8,9]
list_b = [9,8,7,6,5,4]

# Expected result is [13, 13, 13, 13, 13, 13]

sum_2_elements = lambda x , y : x + y
result = list(map(sum_2_elements, list_a, list_b))
print(result)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# How to Use reduce() in Lambda Function
# In order to Use reduce () we have to import a Library called "functools"
# This python function implement mathamatical techinq called 'Folding' or 'Reduction'
# This fucntion will use when you need to apply a function to an iterable and reduce it to "Single" comulative value
 
# here import functools

import functools

list_m = [1,2,3,4,5,6]
add_two_nums = lambda x, y: x+y
multiply_two_nums = lambda x,y: x*y


result_1 = functools.reduce(add_two_nums,list_m)
result_2 = functools.reduce(multiply_two_nums,list_m)
print(result_1)                                     #---> 21
print(result_2)                                     #---> 720


#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*--*---*-**--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*

# Here’s an example in which you use my_add() with initializer set to 100:
def my_add(a,b):
    result = a + b
    print(f"{a}+{b}={result}")
    return result
from functools import reduce
numbers = [1,2,3,4]
reduce(my_add,numbers,100)              #---> 100+1=101
#                                             101+2=103
#                                             103+3=106
#                                             106+4=110

my_add(9,8)                             #---> 9+8=17


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#The filter() method filters the given sequence with the help of a function that-
# tests each element in the sequence to be true or not.
# Syntax: filter(function, sequence)
#  How to use Filter() function

# Crete list of only ODD and Only Even list seperatly

Seq_list = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,4,5,7,8,9,6,5,4,3,2]

filter_odd = lambda x : x % 2!= 0 

filter_even = lambda x : x % 2 == 0

result_o = list(filter(filter_odd,Seq_list))
result_e = list(filter(filter_even,Seq_list))


print(result_o)                             #--->[1, 3, 5, 7, 9, 7, 5, 3, 1, 3, 5, 5, 7, 9, 5, 3]

print(result_e)                             #--->[2, 4, 6, 8, 8, 6, 4, 2, 2, 4, 6, 4, 8, 6, 4, 2]
