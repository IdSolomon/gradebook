last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# I've created a list called subjects and filled it with the classes I'm taking.
subjects = ["physics", "calculus", "poetry", "history"]

# Next I created a list called grades and filled it with my scores.
# NOT calling myself a genius.
grades = [98, 97, 85, 88]

# This is a two-dimensional list with subjects and grades combined
# And it's assigned to a variable called gradebook.
gradebook = [
  ["physics", 98],
  ["calculus", 97],
  ["poetry", 85],
  ["history", 88]
]

# I've added more to the list by appending the values and their associated grades.
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Accessing the index of the grade for my visual arts class
# and making it 5 points greater.
gradebook[5][1] = 98

# Here I decided to switch from a numerical grade value to a Pass/Fail option
# This is how I protect my GPA. With a Pass grade.
gradebook[2].remove(85)
gradebook[2].append("Pass")

# If you noticed at the start, I also have my grades from last semester.
# This is the full gradebook.
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)