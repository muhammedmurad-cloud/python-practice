import json
file_name = "student.json"
try:
    with open(file_name,"r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = []       
def add_student():
    for i in range(1):
        name = input("Enter the name:")
        age = int(input("Enter the age:"))
        grade = int(input("Enter the grade:"))

        student = {"name" : name,
                "age" : age,
                "grade" : grade}
        data.append(student)

        with open(file_name,"w") as file:
            json.dump(data,file,indent=4)
            print("student added succesfully!")
            

def show_students():
    if not data:
        print("data not found")
        return
    for student in data:
        print(student["name"],student["age"],student["grade"])
def search_student():
    name = input("Enter the name:")
    found = False
    for student in data:
        if student["name"] == name:
            print(student)
            found = True
    if not found:
            print("Student not found")
def delete_student():
    name = input("Enter the name:").strip()
    found = False

    for student in data:
        if student["name"] == name:
            data.remove(student)
            found = True
            break

    if found:
        with open(file_name,"w") as file:
            json.dump(data,file,indent=4)
            print("student deleted succesfully")
    else:
        print("student not found")        


               
while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add student")
    print("2. Show students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")                          
               