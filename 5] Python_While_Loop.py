# While Loop :- Use when number of itration is not specified.
# WHile Loop SYNTAX
#  while exp :
# 		statements

#  Write a program to print the table of 9 using while loop
num = 9
counter = 1                        # for 1 multiplication at a time.

while counter <= 10:               # not more than 10 Itirations. This statement Either True or Flase 

	ans = num * counter
	print (num,'*',counter,'=',ans)
	counter = counter + 1            # Each time loop execute it will increment by 1

# What will happend if counter is not incremented???
# Answer:----> Program will stuck in infinite Loop, until system get Crashed.
num = 10
counter = 1

while counter <= 10:

    ans = num * counter
    print (num,'*',counter,'=',ans)
    counter = counter + 1            # For this we have to eliminate this statement to get infinite loop .

# What will Happen to this???

# while True :                       # Here is the Boolen experssion explicitily given without any expression or condition or stratement.
#     print("iNeuron")               #that's why it will keep on printing iNeuron infinitly until system gets crashed.

       
