# loop is controlled sturucture which can allow to use block of code repeatedly'
# There are 2 Types 1] FOR, 2]While
# 1] FOR :- Use when number of iteretions are Known.
for i in range(1,11):	   # Here we can see that '11' is the exclusive vale which is it is not considerd by range.
	print(i)

# Print only ODD Numbers within the range:--
for i in range(1,11,2):    # Here we can see that 3rd value {Step increament value} in range function is selecting rang in desire output.
	print(i) 

# Write a program to print the numbers from 10 to 1.
for i in range(10,0,-1):
	print(i)

# Write a program to calculate the sum of give list elements using FOR Loop
# Output=25
int_list = [4,8,-2,10,5]          # Here to build logic we ahve to inititate the value.

list_sum = 0
for num in int_list:              # Now every Itration we have to add the initial value to elements of list.
	list_sum = list_sum + num
print("Total Sum Of Elements =",list_sum)


