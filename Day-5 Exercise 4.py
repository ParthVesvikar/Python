student_score = input("Enter the score of students\n").split( )
for i in range(0,len(student_score)):
    student_score[i]=int(student_score[i])
print(student_score)
#maximum_score = max(student_score)
#print(f"Maximum score of student is {maximum_score}")
max_score = 0
for p in student_score:
    if p>max_score:
        max_score = p
print(max_score)