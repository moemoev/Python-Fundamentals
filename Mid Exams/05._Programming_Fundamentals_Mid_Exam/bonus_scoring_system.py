import math
students = int(input())
lectures = int(input())
add_bonus = int(input())
attendances = []
if 0 < students:
    for _ in range(students):
        attendances.append(int(input()))
    total_bonus = []
    for i in range(students):
        total_bonus.append(attendances[i] / lectures * (5 + add_bonus))
else:
    attendances = [0]
    total_bonus = [0]

print(f"Max Bonus: {math.ceil(max(total_bonus))}.")
print(f"The student has attended {math.ceil(max(attendances))} lectures.")


'''
TASK:
Create a program that calculates bonus points for each student enrolled in a course. On the first line, you are going to 
receive the number of students. On the second line, you will receive the total number of lectures in the course. The 
course has an additional bonus, which you will receive on the third line. On the following lines, you will be receiving 
the count of attendances for each student.
The bonus is calculated with the following formula:
{total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
Find the student with the maximum bonus and print them, along with his attendance, in the following format:
"Max Bonus: {max bonus points}."
"The student has attended {student attendances} lectures."
Round the bonus points at the end to the nearest larger number.
Input / Constraints
On the first line, you are going to receive the number of the students – an integer in the range [0…50].
On the second line, you will receive the number of the lectures – an integer number in the range [0...50].
On the third line, you will receive the additional bonus – an integer number in the range [0….100].
On the following lines, you will be receiving the attendance of each student.
There will never be students with equal bonuses.
Output
Print the maximum bonus points and the attendance of the given student, rounded to the nearest larger number, scored by 
a student in this course in the format described above.
'''