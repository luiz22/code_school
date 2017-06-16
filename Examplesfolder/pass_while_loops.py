#while loops
# While loops are known as indefinite or conditional loops. 
# They will keep iterating until certain conditions are met
# The while loop, like the if statement, includes a boolean expression that evaluates to true or false.
# The code inside the loop will be repeatedly executed until the boolean expression is no longer true.


#accept input from the user
#if & else condition combine with while loops
# password = ""
# while password != "secret":
#     password = raw_input("Please eneter the password: ")
#     if password == "secret":
#         print("Thank you. you are far too kind entered the correct password")
#     else:
#         print("Sorry the value you enetered is incorrect")



 #Second Example on while loops
 #if and else statement combined

 value = True 
 	while value:
 		number = int(input("Please enter a number is the rande of 50 t0 100:"))
 	if number >= 50 and number <=100:
 		value = False
 	else:
 		print("Sorry number must be within the range above")
 		print("Please try again")

 print("you have entered{0}".format(number))
 print("This number si valid")
