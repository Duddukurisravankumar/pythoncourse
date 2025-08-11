import random
num = random.randint(1,50)
trail=0
while True:
    guss = int(input(" guss the random number "))
    if(num == guss):
        trail+=1
        print(f"you won the game in {trail} trail")
    elif guss < num:
        trail+=1
        print("try some larger number")
    elif guss > num:
        trail=+1
        print(f"try some smaller number")
    if(trail > 5):
        print("chances are completed")
        print(f"u loss the game the number is{num}")
        break
    