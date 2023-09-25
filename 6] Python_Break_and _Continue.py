# How to use break statement.

int_list = [1,5,7,8,19,13,17,3]

# Find the Even value in the given list??

for num in int_list:
	print("Current Element of the list =",num)
	if num%2 == 0:                            # If we want even number in result we have to divide a number by '2'.
		print("Even Number In The List =",num)
		break
# What if break is removed?
# answer:- It unnesserly process the remaining elements of the list.

for num in int_list:
	print("Current Element of the list =",num)
	if num%2 == 0:
		print("Even Number In The List =",num)



# How to use Continue kyeword?

# Print the number from for loop and start them from the value '1'
# But print value on terminal if number is greater than '10'

for num in range (1,31):  # Range(1,31)->[1,2,3,4.....30]
	if num<10:
		continue
	print(num)
