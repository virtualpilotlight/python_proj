# this is a comment
from helper import validate_and_execute, user_input_message

user_input = ""
while user_input != "exit":
	# user input is storred as a string
	user_input = input(user_input_message)
	days_and_unit = user_input.split(":")
	# split() splits on a space by default but can split on a tab with '\t'
	print(days_and_unit)
	days_and_unit_dictionary = {
 		"days": days_and_unit[0], 
 		"unit": days_and_unit[1]
 	}
	print(days_and_unit_dictionary)
	validate_and_execute()