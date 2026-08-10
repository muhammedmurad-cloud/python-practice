file_name = "paragraph.txt"
file_data = "the cat sat on the mat the cat"
a = []
with open(file_name,"w") as file:
    file.write(file_data)
with open(file_name,"r") as file:
    content = file.read() 
for word in content.split():
    if word not in a:
        a.append(word)
print(sorted(a))                  

#This script chooses unique words from file and sorts them for alphabet