
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades = sorted(grades, reverse=True)
print (sorted_grades)


avg = sum(sorted_grades) / len(sorted_grades)
print (avg)


grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades = sorted(grades, reverse=True)
average_grade = sum(sorted_grades) / len(sorted_grades)


graded_grades = []
if sorted_grades[0] < 80:
    graded_grades.append("failed")
else:
    graded_grades.append(sorted_grades[0])

if sorted_grades[1] < 80:
    graded_grades.append("failed")
else:
    graded_grades.append(sorted_grades[1])

if sorted_grades[2] < 80:
    graded_grades.append("failed")
else:
    graded_grades.append(sorted_grades[2])

if sorted_grades[3] < 80:
    graded_grades.append("failed")
else:
    graded_grades.append(sorted_grades[3])

if sorted_grades[4] < 80:
    graded_grades.append("failed")
else:
    graded_grades.append(sorted_grades[4])

if sorted_grades[5] < 80:
    graded_grades.append("failed")
else:
    graded_grades.append(sorted_grades[5])

if sorted_grades[6] < 80:
    graded_grades.append("failed")
else:
    graded_grades.append(sorted_grades[6])

if sorted_grades[7] < 80:
    graded_grades.append("failed")
else:
    graded_grades.append(sorted_grades[7])

if sorted_grades[8] < 80:
    graded_grades.append("failed")
else:
    graded_grades.append(sorted_grades[8])

if sorted_grades[9] < 80:
    graded_grades.append("failed")
else:
    graded_grades.append(sorted_grades[9])


print (graded_grades) 


