my_set = {"January", "Febuary", "March"}
# sets can't be indexed like lists can be
for element in my_set:
	print(element)

my_set.add("April")
print(my_set)
my_set.remove("January")
print(my_set)