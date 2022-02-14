# this is a comment


# a function is assigned with def name_of_func(params):
def days_to_units(num_of_days, conversion_unit):
	if conversion_unit == "hours":
		return f"{num_of_days} days are {num_of_days * 24} hours"
	elif conversion_unit == "minutes":
		return f"{num_of_days} days are {num_of_days * 24 * 60} hours"
	# return returns the value, for concat use f
	else:
		return "unsupported unit."

def validate_and_execute():
	try:
		# int() converts the str to an int,
		user_num = int(days_and_unit_dictionary["days"])
		if user_num > 0:	
			# this runs the function
			calculated_value = days_to_units(user_num, days_and_unit_dictionary["unit"])
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
	user_input = input("Enter number days and conversion unit!\n")
	days_and_unit = user_input.split(":")
	# split() splits on a space by default but can split on a tab with '\t'
	print(days_and_unit)
	days_and_unit_dictionary = {
 		"days": days_and_unit[0], 
 		"unit": days_and_unit[1]
 	}
	print(days_and_unit_dictionary)
	validate_and_execute()