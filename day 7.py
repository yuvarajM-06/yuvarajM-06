# exercise 1
#(simple function for arithmetic operations)

# creating a function
def my_function (operand_1, operand_2):
		print ("Addition of two numbers is", operand_1+operand_2)
		print ("Subtraction of two numbers is",operand_1-operand_2)
		print ("Division of two numbers is", operand_1/operand_2)
		print ("Multiplication of two numbers is", operand_1*operand_2)
		return ("invalid entry")

#calling the function		
my_function (2,-5)

print ("\n")
# exercise 2

def covid(patient_number):
		print("patient number", patient_number)
		name=input("name: \n")
		body_temp = input ("body_temp: ")
		if len (body_temp) == 0:
			print ("98 F")
		return("invalid input")
		
# calling the function
covid(1)