# Dictionary in Python
# Dictionaries in pyhton is a collection of key values,used to store data values like Map.
# Unlike, other types which holds only a single values in an element.
# Each element in the dictionary is 'Key' and 'Value'.
# Each key-value pair in a dictionary is separated by a colon (:).

dict1 = {}
print(type(dict1))

# How to insert values in Dictionary
dict2 = {}
dict2['name'] = 'Pritish'
dict2['age'] = 27
dict2['skills'] = ['Python','Java','Power-BI','SQL','Communication']           #<-- Can assign List
dict2['State_Visited'] = ('MH','TS','Karnatak','Ladak')  #<-- Can assign Tuple
dict2[45] = 'Random Key'

dict2['Other_Details'] = {'Gender' : 'Male', 'Color' : 'Brown','Nationality' : 'Indian'} #<-- Can assign Dictionary
# Here we can insert new infomation explicitly via '{}'--> dictionary type class. Dictionary within Dictionary.

print(dict2)

# Check the lenght of Dictionary
print(len(dict2))       #--> Output will be '6', cuz 6-times we assign the values in a Dictionary

# How to access the value of particular key

print(dict2['name'])      #---> Dictionary Name and put Key in "[]" to retrive the particular Data.
print(dict2["age"])       #---> Single or Double Inverted both can work.
print(dict2['skills'][3]) #---> Here we can Target on Index values to Iterate.
print(dict2['Other_Details']['Nationality'])

# How to update value on particular key
dict2['age'] = 30
print(dict2['age'])

# How to get the keys form a dictionary??

total_keys = dict2.keys()  
print(total_keys)           #--> dict_keys(['name', 'age', 'skills', 'State_Visited', 45, 'Other_Details'])

# OR

total_keys = list(dict2.keys())
print("Total Keys in Dictionary :", total_keys) #-->Total Keys in Dictionary : ['name', 'age', 'skills', 'State_Visited', 45, 'Other_Details']


# How to get values form a Dictionary?

total_values = dict2.values()
print(total_values)
# OR

total_values = list(dict2.values())
print("Total Values in a Dictionary:", total_values)

# how ro Iterate on Dictionary?? 
# In this Iteration we have use 'Key-value' pair

for k,v in dict2.items():  # In this items method returns a view object which contains 'key-value pair'of dictionary
    print("Key is =", k ,"and Value is =", v)
# ---> Output is  Key is = name and Value is = Pritish
                # Key is = age and Value is = 30
                # Key is = skills and Value is = ['Python', 'Java', 'Power-BI', 'SQL', 'Communication']
                # Key is = State_Visited and Value is = ('MH', 'TS', 'Karnatak', 'Ladak')
                # Key is = 45 and Value is = Random Key
                # Key is = Other_Details and Value is = {'Gender': 'Male', 'Color': 'Brown', 'Nationality': 'Indian'}


# Compare Dicrionary 

dict3 = {1,2,5,6,7,4,8,0}
dict4 = {'a','b','c','d','e','f'}
print(dict3 == dict4)  # --> False

dict5 = {'a': 1, 'b': 2, 'c': 3}
dict6 = {'b': 2, 'c': 3, 'a': 1}
print(dict5 == dict6)  # --> True

# How to delete specific key value pair of Dictionary

print(dict2)

del (dict2['age'])
del (dict2[45])

print(dict2)


# How to check If Key exist in dictionary or not ?

keys_in_dictionary = list(dict2.keys())
if 'skills' in keys_in_dictionary:
    print(True)
else:
    print(False)

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*
# What If we have to Update the "Key" in the dictionary without chnanign it's Value part
# i.e. --> for ex:- 'Anand': 23  to 'Ishant': 23

initial_dict = { 'Abhailash': 21 , 'Bhavesh': 43 ,
                'Rohit': 90 , 'Anand' : 23}
print("Initial Dictionary:",initial_dict)   # Output:- {'Abhailash': 21, 'Bhavesh': 43, 'Rohit': 90, 'Anand': 23}

# Edit/Remove Key without changing Value

initial_dict ['Ishant'] = initial_dict ['Anand']

del initial_dict ['Anand']

print("Final Dictionary:", initial_dict)   # Output:- {'Abhailash': 21, 'Bhavesh': 43, 'Rohit': 90, 'Ishant': 23}
    
