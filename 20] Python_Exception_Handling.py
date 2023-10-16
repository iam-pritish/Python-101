# How to Handle exceptions in Python

# Senarios:-

# a = 10
# print("Bye...!!")
# print(a/0)              ##---> ERROR- ZeroDivisionError: division by zero
# print("Hello..!!!")
# 
# list_a = [2,4,8,1,32,23]          
# print( list_a[7])         ---> list index out of range

# a = 5
# try:
#     result = a/0
#     print(result)

# except:
#     print("Some Error Has occured!!!")    ##--> Some Error Has occured!!!

# print("Bye...!!")                         ##--> Bye...!!


num = 5 
list_a = [1,2,3,4,7,20,90]
dict_a = {"Shashank": 20 , "Rahul": 30}

try:
    print("Divide numbers in list by Zero")
    results = num/0
    
    result = num/5
    print(result)
    print("Step 1 completed")

    
    print("Access 10'th element form a List")
    #print(list_a[10])

    print(list_a[3])
    print("Step 2 Done..!!")

    
    print("Access value of Amit form Dictionary")
    #print(dict_a['Amit'])

    print(dict_a['Rahul'])
    print("Step 3 Done..!!!")

# except:
#     print("Some Error has Happend...!!")

# To cappture Individual tpy of Errors
# 1]
except ZeroDivisionError:
    print("This error occured because of Number got divied by 0 ")

# 2]
except IndexError:
    print("This Error occured coz out of bound Index is getting accessed.!!")

# 3]
except KeyError:
    print("Search key Doesn't Exists..!!")

## To capture All types of Error
except Exception as ERROR:
    print("Error occured and Message:", ERROR )

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

## Use of Else Block:-

