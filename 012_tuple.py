# tuple

marks = (95, 98, 97, 97, 97)  # by this, () => tuple
# marks[0] = 99  # this line give error
                 # because 'tuple' doesn't allow change of objects.

print(marks.count(95))
print(marks.index(97))

# set

marks_2 = {95, 98, 97, 97, 97} # by this, {} => set
for score in marks:
    print(score)