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
    
Output
    Sample Space of rolling 2 dice:
[1][1]
[1][2]
[1][3]
[1][4]
[1][5]
[1][6]
[2][1]
[2][2]
[2][3]
[2][4]
[2][5]
[2][6]
[3][1]
[3][2]
[3][3]
[3][4]
[3][5]
[3][6]
[4][1]
[4][2]
[4][3]
[4][4]
[4][5]
[4][6]
[5][1]
[5][2]
[5][3]
[5][4]
[5][5]
[5][6]
[6][1]
[6][2]
[6][3]
[6][4]
[6][5]
[6][6]
How many rolls you want 10
 1)  (1  , 1)  
 2)  (1  , 1)  
 3)  (1  , 5)  
 4)  (2  , 6)  
 5)  (3  , 2)  
 6)  (3  , 6)  
 7)  (5  , 2)  
 8)  (2  , 5)  
 9)  (6  , 3)  
 10)  (4  , 2)  
2 - 2 =0.06%
3 - 0 =0.00%
4 - 0 =0.00%
5 - 1 =0.03%
6 - 2 =0.06%
7 - 2 =0.06%
8 - 1 =0.03%
9 - 2 =0.06%
10 - 0 =0.00%
11 - 0 =0.00%
12 - 0 =0.00%
