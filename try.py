import random
#printing the sample space
def throwdice(turn, n):
    if n==0:
        print(turn)
        return
    throwdice(turn+"[1]", n-1)
    throwdice(turn+"[2]", n-1)
    throwdice(turn+"[3]", n-1)
    throwdice(turn+"[4]", n-1)
    throwdice(turn+"[5]", n-1)
    throwdice(turn+"[6]", n-1)
print("Sample Space of rolling 2 dice:")
throwdice("", 2)

num =int(input("How many rolls you want "))
first=[num]
second=[num]
rolls = {}  #dictionary

for outcomes in range(2,13): 
    rolls[outcomes]=0

for i in range(num):
    f=random.randint(1,6)
    s=random.randint(1,6)
    first.append(f)
    second.append(s)
    rolls[f+s]+=1

#printing thw rolled dice
for i in range(num):
    print(" {})  ({}  , {})  "  .format(i+1,first[i+1], second[i+1]) )


for k in rolls:
    print('%d - %d %.2f%%' %(k,rolls[k],float(rolls[k])/36))
