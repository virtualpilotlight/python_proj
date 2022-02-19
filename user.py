class User:
	def __init__(self, email, name, password, job_title):
	self.email = email
	self.name = name
	self.password = password
	self.job_title = job_title

	def change_password(self, new_password):
		self.password = new_password

	def change_job_title(self, new_job):
		self.job_title = new_job

	def get_user_info(self):
		print(f"User {self.name} works as a {self.job_title}. contact them at {self.email}")


User("omega.x.rae@gmail.com", "omega rae")