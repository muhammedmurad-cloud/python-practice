score=int(input("Enter your score:"))
while score <= 0 or score >= 100:
    print("Invalid score!Enter valid score:")
    score=int(input())
    if score >= 91:
        print("You passed: A")
    elif score >= 81:
        print("You passed: B")
    elif score >= 71:
        print("You passed: C") 
    elif score >= 61:
        print("You passed: D")  
    elif score >= 51:
        print("You passed: E")
    else:
        print("You failed,Keep trying!")  
if score >= 91:
    print("You passed: A")
elif score >= 81:
    print("You passed: B") 
elif score >= 71:
    print("You passed: C") 
elif score >= 61:
    print("You passed: D")  
elif score >= 51:
    print("You passed: E")
else:
    print("You failed,Keep trying!")             



