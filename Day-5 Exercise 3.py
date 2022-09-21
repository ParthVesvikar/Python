student_height = input("Enter the heights of students \n").split( )
for n in range(0,len(student_height)):
    student_height[n]=int(student_height[n])
print(f'Student height {student_height}')
#print(type(student_height))
'''sum of heights'''
total_height =0
for i in student_height:
    total_height = total_height+i
print(f'Sum of students height {total_height}')
'''Length of list'''
number_of_height =0
for p in student_height:
    number_of_height = number_of_height+1
print(f'Number of students {number_of_height}')
'''Average height of students'''
Average_height = total_height/number_of_height
Round_Average_height = (round(Average_height))
print(f'Average height is all students {Round_Average_height}')