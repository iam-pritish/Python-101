list1 = [1,2,3,4,5,6,7]
print("Maximum number from List:", max(list1))
print("Minimum number from list:", min(list1))
print("Sum number from List", sum(list1))

# These are pre-defined functions in Python ['max','min','sum']

# How Function works?
# They may or may not accepts input parameter
#  They may or may not return any output

# Example of Function which doesn't accepts any parameter
# and doesn't return anything
def welcome_msg():
    print(" Welcom to Big-Data Course..!!!")

welcome_msg()  #<--- This is the Calling a Function

# Example of Function which doesn't accepts any parameter
# and does return something

def bot_msg():
    print("Bot Message from Print Function..!")
    return "Message from BOT...!!!"

print( bot_msg() )
result = bot_msg()
print("Output from Bot_Message:", result )

# Example of Function which accepts some parameters
# and return the value

def avg_of_two_nums( a, b ):
    count = 2
    print("Print frist value:", a)
    print("Print Last value:", b)
    avg_result = (a + b) // 2
    return avg_result
num1 = 20
num2 = 30
output = avg_of_two_nums(num1, num2)
print("Result of avg of tow numbers:", output)  


# output1 = avg_of_two_nums(num1)
# print("Result of avg of tow numbers:", output1) >>>> Error:-avg_of_two_nums() missing 1 required positional argument: 'b' 


#--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# Find the Factorial of a number?

def factorial(n):
    
    if n == 0 or n == 1 :
        return 1


    result = 1
    for num in range( 1, n+1 ):
        result = num * result    #---> result = (1 , n+1) * 1
    return result


x = 5
ans = factorial(x)
print("Factorial of number",x, "=", ans)

x = 0
ans = factorial(x)
print("Factorial of number", x, "=", ans)

#--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# How to return multiple values from function

a,b,c = 3, 2, 5
print("The value of a is:", a)
print("The value of b is:", b)
print("The value of c is:", c)

def square_and_cube(n):
    sqr = n*n
    cube = n*n*n
    return sqr,cube

x = 3
sqr_ans,cube_ans = square_and_cube(x)
print("Square of", x, "is", sqr_ans)
print("Cube of", x, "is", cube_ans)

#--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# How to create Optional auguments in pyhton function

def multiply(a , b=3):
    result = a * b 
    return result

num1 = 5
num2 = 10
print(multiply (num1, num2)) # --> 50
print(multiply (num1))       # --> 15  >>> here num1 is assign non-squencially with aurgument (a,b=3)
print(multiply (num2))       # --> 30  >>> here num2 is assign non-squencially with aurgument (a,b=3)

# What IF we reverse this argument part

# def multiply(a=7, b):   >>> This is not Possible coz '1st' element in argument should not be Optional others CAN.
#     result = a * b
#     return result
# num3 = 4
# num4 = 2
# print(multiply(num3 , num4))
# print(multiply(num3))
# print(multiply(num4))  >>>>>> This shows def multiply(a=7, b) 
#                               SyntaxError: non-default argument follows default argument


def multiply(a, b=3, c=5):
    result = a * b * c
    return result

# What If we have mare then 2 values 

num5 = 5
num6 = 10
num7 = 2
print(multiply(num5,num6,num7))     # --> 100 [5*10*2 = 100]
print(multiply(num5,num6))          # --> 250 [5*10*5 = 250]        
print(multiply(num6,num7))          # --> 100 [10*2*5 = 100]
print(multiply(num5,num7))          # --> 50  [5*2*5  = 50 ]
print(multiply(num5))               # --> 75  [5*3*5  = 75 ]
print(multiply(num6))               # --> 150 [10*3*5 = 150]
print(multiply(num7))               # --> 30  [2*3*5  = 30 ]  In all of these it recalls the value which are pre-assign in the optional parameters

#--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# Non-Keyed Arguments

def example_nonkeyed_args(*argv):   # Here '*' works like a simple List
     for para in argv:
        print(para)

example_nonkeyed_args('Hello','and','Welcome','to','Python-Core!!!')

# Key Value type of Arguments in Pyhton

def example_of_kwargs(**kwargs):         # Here '**' we used as a dictionary

    # print("Value of Host:", kwargs['Host'])
    # print("Value of Port:", kwargs['Port'])     # Mind here NO-'()' dict object; Only '[]' List object.
    # print("Value of Password:", kwargs['Passw'])

    for k,v in kwargs.items():
        print("Key is:",k,"and Value is:",v)

example_of_kwargs( Host='198.191.1.1',Port=922813,Password='XXFGH' )

example_of_kwargs( Port=922813,Password='XXFGH',Host='198.191.1.1' )
# Whatever the sequence is Out put will be in arragened manner
