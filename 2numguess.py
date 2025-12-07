import random
num=random.randint(1,10)
attempts=7
print("\t---NUMBER GUESSING GAME---")
print("\tMaximum attempts: 7")
for i in range(0,attempts):
    user=int(input(f"Attempt{i+1}:Enter the number you guessed:"))
    if user==num:
        print("You WIN!!! The number is:",num)
        break
    elif i==6:
        print("YOU LOSE!! Out of attempts the number was:",num)
    elif user!=num:
        if user>num:
            print("TOO HIGH")
        elif user<num:
            print("TOO LOW")
        print("TRY AGAIN!!!")
        continue
    
