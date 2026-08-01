fav_movies = ["Interstellar","Inception","Zodiac"]
file_path = "output.txt"
with open(file_path,"w") as file:
    for movie in fav_movies:
        file.write(movie + "\n")
    print(f"txt file {file_path} was created")
    