from datetime import datetime

user_input = input("Enter your goal and a deadline seperated by a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()

time_left = deadline_date - today_date
print(f"you've got {int(time_left.total_seconds() / 60 / 60)} hours left to acheive your goal of {goal}, sort it out!")