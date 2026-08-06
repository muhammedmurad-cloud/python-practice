file_name = "print_spesific_lines"
file_data = ["line1","line2","line3","line4","line5","line6"]
with open(file_name,"w") as file:
    for data in file_data:
        file.write(data + "\n")
target_lines = {1,3,5}        
with open(file_name,"r") as file:
    for i,line in enumerate(file,start = 1):
        if i in target_lines:
            print(line,end = "")
        