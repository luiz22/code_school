
# take input from the user

print("Simple CAlcutor!:")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

new = raw_input("Enter choice(1/2/3/4):")

num1 = int(raw_input("Enter first number: "))
num2 = int(raw_input("Enter second number: "))

if new == '1':
   print(num1,"+",num2,"=", num1+num2)

elif new == '2':
   print(num1,"-",num2,"=", num1-num2)

elif new == '3':
   print(num1,"*",num2,"=",num1*num2)

elif new == '4':
   print(num1,"/",num2,"=",num1/num2)
else:
   print("Invalid input")