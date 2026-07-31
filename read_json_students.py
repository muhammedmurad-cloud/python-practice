import json

file_path = "C:/Users/user/Downloads/File_Handling/input.json"
with open(file_path,"r") as file:
    content = json.load(file)
    a = []
    b = []
    c = 1
    for students in content.get("students"):
        print(c,".",students["name"],":",students["grade"])
        c = c+1
        b.append(students["name"])
        a.append(students["grade"])
        k = k+1
    print("max score",":",max(a),b[a.index(max(a))])

        

