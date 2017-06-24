#Example of simple calculator


print("Welcome to Code School Simple Calculator ")

#declares a variable / Users choice

typeofsum = str(raw_input("would you like:  Addition(+), Subtraction(-), multiplication(*), Division(/) or Modula(%)  \n"))

#if statement 
if typeofsum == "+": 
	number1 = int(input("Enter the first Value: "))  #input first number
	number2	=int(input("Enter the second value: "))  #input second number
	print number1 + number2							 #Compute the sum of the values

#elif statement
elif typeofsum == "-":
	number1 = int(input("Enter the first value: ")) #input first number
	number2 = int(input("Enter the second value: ")) #input second number
	print number1 - number2

#elif statement
elif typeofsum == "*":
	number1 = int(input("Enter the first value: ")) #input first number
	number2 = int(input("Enter the second value"))  #input second number
	print number1 * number2

#elif statement
elif typeofsum =="%":
	number1= int(input("Enter the first value")) #input first number
	number2= int(input("Enter the second value")) #input second number
	print number1 % number2

#esle statement
else:
	print("Not an operator, try again!  ")
