import random

#list of students in the class
students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]

#pick a random student to call on
pick = random.choice(students)
print(pick)

#pick multiple random students for group work
group = random.sample(students, 3)
print("Group members: " + ", ".join(group))