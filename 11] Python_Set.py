# Set is use to Store multiple items in single variable
# Set is one of 4 types in Python, Which used to store data, other 3 are 'List','Tuple','Dictionary'
# Set is the collection which is Unoreded,Unchenaged* and UnIndexed
# Set items are unchangeble, but you can remove and Add new items
# Sets cannot have two items with the same value.
# Python example demonstrate that a set can store heterogeneous elements

myset = {"Geeks", "for", 10, 52.7, True}
print(myset)
# output: {True, 10, 'Geeks', 52.7, 'for'}

# Empty Set
set1 = set()   # Here Round brackes are used in set 
print(type(set1))

# What If we use '{}' curly Braket in Empty Set 
set2 = { }
print(type(set2)) #---> It is showing Type of class "Dictionary"

# If you want to showcase the values in "{}" bracket you need to insert atleast one value

set3 = {'mondy','tuesday','wednesday','thursday','friday','saturday','sunday'}
print(set3)   #--->{'saturday', 'mondy', 'tuesday', 'wednesday', 'sunday', 'friday', 'thursday'} "NO Oredr"

set4 = {1,2,3,2,4,6,7,5,6,8,5,4,3,9,}
print(set4)   #--->{1, 2, 3, 4, 5, 6, 7, 8, 9} "NO Duplication"


list1 = [2,4,3,5,6,8,5,6,4,8,9,3,2,4,1,0,5,6,3]
set5 = set(list1)
print(set5)

# How can we Iterate elements in the set
for num in set5:
    print(num)

# Conver output of Set into List
list2 = [54,24,88,87,67,92,73,51]
set6 = list(set(list2))
print(set6)

print(set6[-1]) # Print last value in the list 

# How to insert elements in set

set7 = set()
set7.add(1)
set7.add(2)
set7.add(1)
set7.add(5)
set7.add(4)
set7.add(2)
set7.add(1)

print(set7) #---> NO repeat values

# Use of Update Method
temp = [34,56,78,33,32,1,2,3,4,5,6,7,8,9,0]
set7.update(temp)
print(set7)

# Calculate the length of the set
print(len(set7))
#--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# SET Operations:- (Union[|],Intersections[&],Difference[-] and Symmetric Difference[^])

# Input :
# A = {0, 2, 4, 6, 8}
# B = {1, 2, 3, 4, 5}

# Output :
# Union : [0, 1, 2, 3, 4, 5, 6, 8]
# Intersection : [2, 4]
# Difference : [8, 0, 6]
# Symmetric difference : [0, 1, 3, 5, 6, 8]

set_a = {1,2,3,4,5,10,20}
set_b = {1,2,3,4,5,6,7,8,9,0}

# Union Operation
print(set_a | set_b)

# Intersection Operation
print(set_a & set_b)

# A - B = ?
# B - A = ?

# Difference Operation

print(set_a - set_b)
print(set_b - set_a)

#  Symmetic differences (Comparison) Operation

x_set = {1,2,3,4,5,6,7,8}
y_set = {3,4,5,2,6,7,8,1,9}
print(x_set == y_set)
# Output is ---> Flase
