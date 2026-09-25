students = {
    "Ali": {"math": 85, "physics": 90, "english": 78},
    "Aysel": {"math": 95, "physics": 88, "english": 91},
    "Murad": {"math": 60, "physics": 72, "english": 68},
    "Leyla": {"math": 100, "physics": 98, "english": 95}
}
for students,scores in students.items():
    average = sum(scores.values())/len(scores)
    print(students,":", average)