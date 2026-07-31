file_path = "C:/Users/user/Downloads/File_Handling/movies.txt"
with open(file_path,"r") as file:
   k = 1
   for line in file.readlines():
      print(k,".",line.rstrip())
      k = k+1   