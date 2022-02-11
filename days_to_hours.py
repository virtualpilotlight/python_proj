# this is a comment

# variable assignment of an int 
total = 24
# variable assignment of a string
units = "hours"
# a function is assigned with def name_of_func(params):
def days_to_units(num_of_days):

	condition_check = num_of_days > 0
	print(type(condition_check))
	#conditional statments like if get a :
	if num_of_days > 0:
		# return returns the value, for concat use f
		return f"{num_of_days} days are {num_of_days * total} {units}."
	elif num_of_days  == 0:
		return "zero doesn't makes sense. positives only."


# user input is storred as a string
user_input = input("pick a number:\n")

if user_input.isdigit():
	# int() converts the str to an int,
	user_num = int(user_input)
	# this runs the function
	calculated_value = days_to_units(user_num)
	# this prints the results of the finished function
	print(calculated_value)
else:
	print("whole positive numbers only.")