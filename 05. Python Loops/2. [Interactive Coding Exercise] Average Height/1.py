# Don't change the code below
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# Don't change the code above


# Write your code below this row 👇
totalHeight = 0
for height in student_heights:
    totalHeight += height
avgHeight = totalHeight / len(student_heights)
print("Average Height : ",round(avgHeight,2))
print("Total Height : ",totalHeight)
print("Total Heights : ",len(student_heights))
