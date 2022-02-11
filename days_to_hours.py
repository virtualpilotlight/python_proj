# this is a comment

# variable assignment of an int 
total = 24
# variable assignment of a string
units = "hours"
# a function is assigned with def name_of_func(params):
def days_to_units(num_of_days):
	# return returns the value, for concat use f
	return f"{num_of_days} days are {num_of_days * total} {units}."

def validate_and_execute():
	try:
		# int() converts the str to an int,
		user_num = int(num_of_days_element)
		if user_num > 0:	
			# this runs the function
			calculated_value = days_to_units(user_num)
			# this prints the results of the finished function
			print(calculated_value)
		elif user_num == 0:
			print("zero doesn't makes sense. positives only.")
		else:
			print("no negatives.")
	except ValueError:
		print("whole positive numbers only.")	

user_input = ""
while user_input != "exit":
	# user input is storred as a string
	user_input = input("Enter days as CSV (comma seperated values) to be converted to hours:\n")
	# split() splits on a space by default but can split on a tab with '\t'
	for num_of_days_element in user_input.split(","):		
		validate_and_execute()
