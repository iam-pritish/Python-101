# NUMERICAL Operators in Python

# '+' for  addition
# '-' for  substraction
# '*' for  multiplication
# '/' for  float division
# '//' for integer division
# '**' for power calculation
# '%'  for Modulus

x = 5
y = 3
print("1] Addition of x + y =", x+y)
print("2] Substraction of x - y =",x-y)
print("3] Multiplication of x * y =",x*y)
print("4] Float Division of x / y =",x/y)
print("5] Integer DIvision of x // y =",x//y)
print("6] Modulus of x m% y =",x%y) #The Modulus is the Reminder value in division 5%3===> 1 is quicent and 2 is Reminder
print("7] Power of y on x i.e.; x ** y =",x**y)

# Some Operations on String
str_data = "Pritish"

#Concate Operation for string
full_name = str_data + " " + "Yelekar"
print("Full Name:-", full_name)

#If we can use '-' minus operator for "str" class
#minus_str = "Pritish" - "Yelekar"
#print("Minus str =", minus_str)
# In Result it shows:- minus_str = "Pritish" - "Yelekar"
#TypeError: unsupported operand type(s) for -: 'str' and 'str'

#Same for Power operators '**' not supported

#But for Multiplication, it works 
Multiply_Name = "Pritish" * 3
print("Multiply Name =",Multiply_Name)

# ASSIGNMENT OPERATORS
# '='  , x = 5

# '+=' , x += 5 ---> x = x + 5
# '-=' , x -= 5 ---> x = x - 5
# '*=' , x *= 5 ---> x = x * 5
# '/=' , x /= 5 ---> x = x / 5

# '//=' , x //= 5 ---> x = x // 5
# '%=' , x %= 5 ---> x = x % 5

# COMPARISON OPERATORS [Here we compaire operats]
# '==' , Equals to condition,       ex:- x == y
# '!=' , Not Equals to condition,   ex:- x != y

# '>' ,  Greater than condition,    ex:- x > y
# '<' ,  Less than condition,       ex:- x < y

# '>=' ,  Greater than and Equals to condition,     ex:- x >= y
# '<=' ,  Less than and Equals to condition,        ex:- x =< y

a = 10 
b = 5
print("1] Result of x == y ,", a == b)
print("2] Result of a != b ,", a != b)

print("3] Result of a > b ,", a > b)
print("4] Resul of a < b ,", a < b)

print("5] Result of a >= b ,", a >= b)
print("6] Result of a <= b ,", a <= b)

# LOGICAL OPERATORS in python [Logical check will happen for Expreesion Result]

# 'and' ---> Result 'True' if BOTH the statements are 'True' else 'False'
# 'or'  ---> Result 'True' if ONE of the statements are 'True' else 'False'
# 'not' ---> Reverse the Result, returns 'False' if the statement is 'True'

# Ex:-

m = 10
n = 7
print("Result of 1] m>10 and 2] n<10", m>10 and n<10) # False and True --> False
print("Result of 2] m>20 or  2] n<10", m>20 or n<10) # False or True   --> True
print("Result of not(m>20 and n<0)", not(m>20 and n<0)) 
# not(False and True)=not(False)--> True
