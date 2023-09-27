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

