
#default arguments in function

#function is defined here
# def print_Info(name,age= 20):
# 	print "Name: ", name # this prints a passed info into the function
# 	print "Age", age
# 	return;

# #Now call the function 
# print_Info(age=10, name="fabio")
# print_Info(name="fabio")



#function definition
# def Add(arg1,arg2):
# 	#add both parameters and return them.
# 	total = arg1+arg2
# 	print "Inside the function: ", total
# 	return
# #Call function 
# total =Add(10,10);
#print "Outside function: ", total

#functions and variables Global and local
#variables defind inside a function body have a local scope
#variables defined outside have a global scope
#this means local variables can be accessed only inside a function in which they declared
#global variables can be accessed throught out the program

#example
total = 0; #this  a global variable
#define function
def sum(arg1,arg2):
	#add both parameters and retutn them
	total = arg1+arg2 # total is a global variable
	print "inside the fucntion locall total: ", total
	return total
sum(2,2);
print "outside the function total :", total

