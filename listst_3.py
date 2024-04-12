students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]




for iteration in range(len(grades)):
    if grades[iteration] < 80:
        print("Name: " + students[iteration] + ", Grade: " + str(grades[iteration]) + ", Activity: " + activities[iteration])

#since the lists are in the same order, we cam grab the indecy of the  student who scored 80, and that indecy will also be the same as there activity and name
    
for iteration in range(len(grades)):
    if grades[iteration] > 80:
        print("Name: " + students[iteration] )   #i know i dont need this whole block. but im getting lazy and i wanted to copy and paste the other block to save time