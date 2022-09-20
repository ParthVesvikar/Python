# Average Height of Student#
student_height = (input("Enter list of student height \n")).split()
for i in range(0,len(student_height)):
    student_height[i]=int(student_height[i])
print(f"Student Heights{student_height}")
sum_height = sum(student_height)
print(f"Sum of student height {sum_height}")
number_of_student = len(student_height)
print(f"Number of students {number_of_student}")
Average = sum_height/number_of_student
print(f"Average of Student heights {Average}")