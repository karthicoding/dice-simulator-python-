#dice rolling simukator 
import random
import time

user_choice = "yes"

while  user_choice =="yes" or user_choice =="y":
    print("dice is rolling...")
    time.sleep(1)
    
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    total=dice1+dice2
    
    print("value of dice 1:-",str(dice1))
    print("value of dice 2:-",str(dice2))
    print("total value:-",str(total))
    
    user_choice=input("do you want to roll the dice again:-")