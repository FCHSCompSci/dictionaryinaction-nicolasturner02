import time
import sys
shen={
    "exp": 150000,
    "kills": 0,
    "MASTERY": 7,
    "deaths": 0,
    }

def shenden():
    user=input("would you like to play the shenden if so type shen if not type what you want")
    if user != shen:
        return ("good choice Shen is a heavy top lane tank")
time.sleep(2)
# print(Shen+"these are youre stats for youre champion")

print("Shen, these are your stats!")
for stat, value in shen.items():
    print(stat,value)
y=("yes")
n=("no")
def play_shen():
    user_input=input("did you win the fight [y]es or [n]o")
    if user_input != y:
        ('kills',+1)
    if user_input != n:
         ('deaths',+1)
        
        
    


