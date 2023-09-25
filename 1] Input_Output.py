# Declare & Assign Variables

int_var = 10
float_var = 18.25
string_var = 'Pritish' # or another way "Pritish"
bool_var = True # if we want to assign flase then it should be like False


# Function in Python for Output 
# Function does WHAT? --->>> they might or might not accept some parameter

print("Hello Wrold !!!!")

# Print variable values in Python
print("Value of int_var")  # <<<---- This is wrong way to put variable values
print("Value of int_var = ",int_var,"<--Reault Done")
print("Value of float_var =",float_var,"<--Result Done!!!")
print("Value of string_var=",string_var,"---Result Done...!!")
print("value of bool_var=",bool_var,'- Result Done')

# How to check the Data Type of any variable in Python??
# We can use type()---->Function

print("Type of int_var?", type(int_var))
print("Type of float_var?", type(float_var))
print("Type of string_var?", type(string_var))
print("Type of bool_var?", type(bool_var))

# How to do the type casting in Python?
# int() , str() , float() , bool() this way we can do the type casting
#For ex-01
int_var = int_var + 10       # int_var = 10 + 10 and in next step int_var = 20
#for ex-02
casted_int_var = float(int_var)
print("Int to Float TypeCasting for int_var =", casted_int_var)
#for ex-03
casted_float_var = int(float_var)
print("Float To Int TypeCasting for float_var =",casted_float_var)

# Now for the String Variable-->> We can not directly convert string into any other data type if its string then its ok
#for ex-04
numeric_str ="123"
print("Value of numeric_str =", numeric_str)
#numeric_str = numeric_str + 50 # Is It valid?-->TypeError: can only concatenate str (not "int") to str, will appear
# because "123"+50 cant be happening 


# Now If we have to Typecast the string variable we need to convert str to int if we want to add some numbers in str 
#For Ex-05
numeric_str = int(numeric_str) + 50 # numeric_str = int(123) + 50 = 123+50=173
print('Value of numeric_str =',numeric_str)

#How to take a INPUTS in Python?
#We can use input() Function

# Ex-01 --->

name = input()
age = input()
print("User Name=",name)
print("User Age =",age)  #--->> Here, you want to execute this INPUT code, do it vai Python File Terminal
#Then type the inputs on termial like name and age

# Another way to take user INPUT

name = input("Enter value for Name =")
age = input("Enter value for Age =")
print("User Name =",name)
print("User Age =",age)

print("Type Of Name =", type(name))
print("Type Of Age=", type(age))

#The Result in the terminal --->>>
#Enter value for Name =Pritish
#Enter value for Age =29
#User Name = Pritish
#User Age = 29
#Type Of Name = <class 'str'>
#Type Of Age= <class 'str'>
# Here we can see the class of Name and Age I "str"
# we can CHANGE the class as follows :-- By Using CASTING Method
#CONVERT TYPE OF DATA DURING INPUT:--->>
name = input("Enter value of Name=")
age = int(input("Enter vale of Age="))
print("User Name=",name)
print("User Age=",age)

print("Type of Name =", type(name))
print("Type of Age =", type(age))
#Results are as follows--->>
#Enter value of Name=Pritish
#Enter vale of Age=29
#User Name= Pritish
#User Age= 29
#Type of Name = <class 'str'>
#Type of Age = <class 'int'>  <-------This is the change in class(int)
