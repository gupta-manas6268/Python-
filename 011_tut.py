# list

marks = [95, 98, 97, "maths"]
print(marks)
print(marks[0])


marks.append(99)
print(marks)

marks.insert(0, 99)
print(marks)

print(99 in marks) # checks whether element is present or not.

print(len in marks) # len -> length

marks.clear()
print(marks)


# break

student = ["ram", "shyam", "radha", "radhika"]

for student in student:
    if student == "kishan":
        continue;
    print(student)