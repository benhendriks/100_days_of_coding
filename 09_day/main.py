student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for key, value in student_scores.items():
    if value >= 91:
        value = 'Outstanding'
    elif value >= 81:
        value = 'Exceeds Expactations'
    elif value >= 71:
        value = 'Acceptable'
    else:
        value = 'Failed'

    student_grades[key] = value

print(student_grades)

