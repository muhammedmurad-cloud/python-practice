import random
a = random.randint(0,50)
attempts = 0
while attempts < 3:
    b = int(input("enter the number:"))
    attempts = attempts + 1
    if a > b:
        print("number is too high!")
        
    elif b > a:
        print("number is too low!")
        
    else:
        print(f"Well Done!,You guessed in {attempts} attempts")
        break
else:
    print(f"Game Over!,Number was {a}")              