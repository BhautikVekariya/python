import random

num=random.randint(1,1000)

tries=0

while True:
      guess=int(input("please guess your number 1 to 1000:- "))

      if guess==num:
            tries+=1
            print(f"🎉 Correct! You guessed the number in {tries} tries.")
      elif guess < num:
            tries+=1
            print("To low! Try again.")
      elif guess > num:
            tries+=1
            print("To high! Try again.")
      else:
            tries+=1
            print("you guess the wrong number")      
