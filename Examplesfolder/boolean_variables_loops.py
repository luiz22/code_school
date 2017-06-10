#Assing some Boolean variables

# a = True
# b = False

# print("a=", a ,"b=", b )

# #Reassigns a 
# a = False;
# print ("a=", a , "b", b)


# A,B = int(input("Enter a number to divide: "))
# if B!=0:
# 	print(A,"/",B, "=", A / B)
# else:
# 	Print("This is value is not allowed: ")



#example of if and else statement

#d_1= 1.11 - 1.10
# d_2= 2.11 - 2.11
# print("d_1=",d_1,"d_2=",d_2)
# if d_1 == d_2:
# 	print("Same")
# else:
# 	print("different")
# 	

#Nested condition
# Val = input("Enter an integer value:")
# if val >= 0:
# 	if val <=10:
# 		print("In range")
# print("Not Accepted")

#Examples of Compound boolean Expressions
# operation = int(input("Enter value from 0...10: "))
# if operation >= 0 and	operation <= 20:
# 	print("value was ok")
# else:
# 	print("Not in range")
# print("done")


# for letter in "Python":
# 	print "current letter:" letter


i = 2
while(i < 100):
	j = 2
	while(j <= (i/j)):
		if not (i%j): break
		j = j + i
	if (j > i/j): print i, "is a prime"
	i = i + 1
	print "Good bye"