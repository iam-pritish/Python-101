# Declaer Empty List 
L1 = []
print(type(L1))
print("Initial Lenght of the list",len(L1))

# Insert value in the list.
L1.append(5)
L1.append(8)
L1.append(21)
L1.append(9)
print(L1)

# Create a list of 1000 number starts for 1 to 1000
# int_list = []
# for num in range(1,11):
#     int_list.append(num)

# How to calculate the length of a List?

len_of_list = len(L1)
print("Lenght of the List",len_of_list)

# How to check if List are Equal to each Other??
list_1 = (1,"Pritish",4,"hi")
list_2 = (1,"Pritish",4,"hi")
print ("List are Equal?", list_1 == list_2)

List_1 = (1,"Pritish","hi",3)
list_2 = (1,"Pritish",3,"hi")
print ("2nd List are Equal?", list_1 == list_2)

#--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# How to concat
list4 = [2,3,9,4,8,6]
list5 = [22,45,28,99,17]
result = list4 + list5
print(result)

#--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# How to access List value
list6 = [10,20,30,40,50,60]

# Print all the element in the list --> Option:-01
for n in list6:
    print(n)

# Print 3rd element of given list
# Syntax = list_name[index]

print(list6[0])
print(list6[1])
print(list6[2])
print(list6[3])
print(list6[4])
print(list6[5])

# What will happend if index value is High??
# Answer:- ERROR will be index out of range
# print(list6[100])

#--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# How to updated the value of index in list?
list7 = [44,"OPPO",23,"LG",99]

# change 'OPPO' to 'SONY' and 'LG' to 'HTC'
list7[1] = "SONY"
list7[3] = "HTC"
print(list7)

#--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# how to print list element using length?
for index in range(0,len(list7)):    #range(0,3)---> [0,1,2] index
    print(list7[index])

#--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# What will be the output of length in list element having list in it{i.e.-->List-inside-List}

list8 = (34,"Siri",67,10,"Alexsa",90,[4,5,8,67,99],"Hublot",89)

print(len(list8)) # Ans will be '9' coz index considered one intity at time

#--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# Difference between append() and extend()
# Append()
list9 = [77,6,42,54,89]
list10 = ["AT&T","AirTel","VI","MTNL"]
list9.append(list10)
print("Output of append :",list9)
print("Length of append :",len(list9))
      #Output of append : [77, 6, 42, 54, 89, ['AT&T', 'AirTel', 'VI', 'MTNL']]
      #Length of append : 6

# Extend()
list11 = [90,32,29,34,49,12]
list12 = ["IKEA","WestSide","Mart","DallorTree"]
list11.extend(list12)
print("Output of extend list:", list11)
print("Length of extend list:", len(list11))
        #Output of extend list: [90, 32, 29, 34, 49, 12, 'IKEA', 'WestSide', 'Mart', 'DallorTree']
        #Length of extend list: 10

#--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# List Slicing
list13 = [77,66,55,44,33,22,11,00,99,88]

# SYNTAX:--->
# list_name[starts:end]
# End index is exclusive

print(list13[ : 3])  #--> O/p is [77, 66, 55]
print(list13[2 : 8]) #--> o/p is [55,44,33,22,11,00]
print(list13[5 : ])  #--> o/p is [22, 11, 0, 99, 88]

print(list13[ : ])   #--> o/p is [77, 66, 55, 44, 33, 22, 11, 0, 99, 88]
print(list13[ : 9])   #--> o/p is [77, 66, 55, 44, 33, 22, 11, 0, 99]

  

# To step up the value in the list 
# 3rd space in the list will be used 

print(list13[ 0 : 6 : 2])  # Here the 3rd value is for spte value which will jump values accordingly
# The output is [77,55,33]--->[77,66,55,44,33,22,11,00,99,88]

print(list13[ 1 : 9 : 3]) 
# The output is [66,33,00]--->[77,66,55,44,33,22,11,00,99,88]

# How to print the last value of the list?
print(list13[ len(list13) - 1])  #--> '88'
print(list13[-1])                #--> '88'  --->> '-ve' index [-1]means last element of the list

# Print 2nd last element form the list
print(list13 [ len(list13) - 2 ]) #--> '99'
print(list13[-2])                 #--> '99'

# Print in-Out list in reverse direction
print(list13[ -1 :  : -1 ])
#-->[88, 99, 0, 11, 22, 33, 44, 55, 66, 77] <<<<<[77,66,55,44,33,22,11,00,99,88]

