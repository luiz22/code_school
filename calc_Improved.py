#Simple Calculator


#Select your operation symbol
# operation = input('''
# Please type in the math operation you would like to complete:
# + for addition
# - for subtraction
# * for multiplication
# / for division 
# ''')
#Select your opeartion symbol

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# val = raw_input("eneter first number")
# operator = raw_input ("operator eg. +,/,-")
#Prompts user for an input

number_1 =int(input("Enter first Value: "))
number_2 =int(input("Enter Second Value: "))

#print number_1+number_2
#string formatters makes it user friendly

#Addition
if operation == "+":
	print("{}+{}=" .format(number_1,number_2))
	print number_1 + number_2
# if operation == "+":
# 	print("{} + {}=" .format(number_1,number_2)) 
# print number_1+number_2

#Subtraction
elif operation == "-":
	print("{}+{}=".format(number_1,number_2))
	print number_1 - number_2
# elif operation =="-":
# 	print("{}-{}=".format(number_1,number_2))
# print number_1 - number_2

#division
elif operation =="/":
	print("{}/{}=".format(number_1,number_2))
	print number_1/number_2
# elif operation == "/":
# 	print("{}/{}=".format(number_1,number_2))
# print number_1 / number_2

#Multiplication
elif operation == "*":
	print("{}*{}=".format(number_1,number_2))
	print number_1 * number_2
# elif operation == "*":
# 	print("{}*{}=".format(number_1,number_2))
# print	number_1 * number_2

#Modula
elif operation == "%":
	print("{}+{}=".format(number_1,number_2))
	print number_1 % number_2
# elif operation == "%":
# 	print("{}%{}=".format(number_1,number_2))
# print number_1 % number_2

#Square
elif operation == "**":
	print("{}**{}=".format(number_1,number_2))
	print number_1 ** number_2
# elif operation == "**":
# 	print("{}**{}".format(number_1,number_2))
# print number_1 ** number_2

else:
	print("That is not a valid operation, try again!" )