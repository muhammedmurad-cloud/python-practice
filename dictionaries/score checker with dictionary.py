student = {"name": "Muhammed",
            "age" : "17",
            "score": 86}
student.update({"score" : 92})
def calculate_grade(score):
    if score >= 91:
        return "A"
    elif score >= 81:
        return "B"
    elif score >= 71:
        return "C"
    elif score >= 61:
        return "D"  
    elif score >= 51:
        return "E" 
    else:
        return"You failed"
score = student.get("score")
print(calculate_grade(score))                