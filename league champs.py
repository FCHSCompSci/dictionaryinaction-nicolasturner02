#Nicolas Turner
#league champ
#09/24/2018
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
Y=("yes")
N=("no")
def play_shen():
    user_input=input("did you win the fight [Y]es/[N]o")
    if user_input == Y:
        shen['kills']+1 and shen['exp']+100
    if user_input == N:
        shen['deaths']+1
        
        
        
        
    


