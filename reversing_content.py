file_name = "original.txt"
file_data = ["line1","line2","line3"]
with open(file_name,"w") as file:
  for line in file_data:
    file.write(line + "\n")
with open(file_name,"r") as file:
  content = file.readlines()     
file_name2 = "reversed.txt"
with open(file_name2,"w") as file:
  for line in content[::-1]:
    file.write(line.strip() + "\n")
print(f"{file_name} reversed successfully")

#This script creats a file containing reversed content of current file