#Gradebook Example

#Last terms grades
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

#Classes taken
subjects = ["Physics", "Calculus", "Poetry", "History"]

#Grades for these subjects
grades = [ 98, 97, 85, 88]

subjects.append("Computer Science")
grades.append(100)

gradebook = list(zip(subjects, grades))

gradebook.append(("Visual Arts", 93))

print(gradebook)
