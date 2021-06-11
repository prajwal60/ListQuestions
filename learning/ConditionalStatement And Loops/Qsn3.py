# Write a Python program to guess a number between 1 to 9.



for i in range(3):
    guess= int(input("Enter your guess below 9"))
    
    if 7 == guess:
        print("You are lucky")
        break
    elif guess < 7:
        print("You have to increase your number")
    elif guess >7:
        print("You have to decrease your number")
    else:
        print(" above 0 and below 10")
else:
    print('Game Over')