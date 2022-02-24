from user import User
from post import Post

app_user_one = User("omega.x.rae@gmail.com", "omega rae", "passwd", "DevOps Engineer")
app_user_one.get_user_info()
app_user_one.change_job_title("Cobra Commander")
app_user_one.get_user_info()
new_user = User("yesilostmymind@gmail.com", "omega x rae", "lakjfd", "hacker")
new_user.get_user_info()
app_user_two = User("user@email", "other user", "psw", "job title")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_one.name)
new_post.get_post_info()