# Create stiring in Python
str1 = "iNeuron"
print(str1)         #iNeuron

str2 = "Pritish's Phone"
print(str2)         #Pritish's Phone

str3 = 'he is a "very Good" boy.'
print(str3)         #he is a "very Good" boy.

# How to use the lenght function
print("Lenght of the String :", len(str3))      # Lenght of the string is : 24

# How to write a Muliline string 
str4 = '''Up coming sunday I'm 
going to attend 
the meeting for 
my client..!!'''
print(str4)         
#Up coming sunday I'm 
#going to attend 
#the meeting for 
#my client..!!

# String Concatination

str5 ="Jason"
str6 ="Brody"
print(str5  +  str6)
# JasonBrody

# String comparison
str7 ="Jason"
str8 ="Jason"
print(str7 == str8) #>>> True

# How to print each character form the string
for char in str8:
    print(char) # J a s o n ---> output in vertical form 

print(str8[0]) # J
print(str8[1]) # a
print(str8[2]) # s
print(str8[3]) # o
print(str8[4]) # n

# Update the 5th character in the string by 'y'

str9 = "MultiNational"   #<-- This is Immutable 

# str9[4] = 'y'
# print(str9)
# here we will not be able to Update the value directly

# Convert String to lower case 
print(str9.lower())

# Convert Strig to upper case
print(str9.upper())

# Other functinalities will be same as LIST.
