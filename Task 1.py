import random

minimum = -9999 
maximum = 9999
node = []
min_point = 0
s = 0
points = []
string=""

#Taking ID as input

a= input("Enter your ID: ")

#changing 0s to 8
for i in a:
    if i=="0":
        string+="8"
    else:
        string+=i

#Get min point from input
for i, j in enumerate(string):
    if i == 4:
        min_point = int(j)
    
#take number of shuffles from input 
for i, j in enumerate(string):    
    if i == 3:
        s = int(j)


#Reverse
#maximum
#target
        
t = string[-1] + string[-2]
t = int(t)
m = int(t * (150/100))


for i in range(0,8):
    node.append(random.randint(min_point, m))


#main function for min and max
def mn(d, idx, ply,valo, alpha, beta):
  
    if d == 3:
        return valo[idx]
 
    if ply:
      
        n = minimum  
        for i in range(0, 2):
             
            x = mn(d + 1, idx * 2 + i,False, valo, alpha, beta)
            n = max(n, x)
            alpha = max(alpha, n)
 
            
            if beta <= alpha:
                break
          
        return n    
    else:
        n = maximum
 
        
        for i in range(0, 2):
          
            x = mn(d + 1, idx * 2 + i,
                            True, valo, alpha, beta)
            n = min(n, x)
            beta = min(beta, n)
 
            if beta <= alpha:
                break
          
        return n

x = mn(0,0,True,node,minimum,maximum)
print("=================================")
print()
print("Task1")
print()
print("Generated 8 random points between the minimum and maximum point limits: ",node)
print("Total points to win: ",t)
print("Achieved point by applying alpha-beta pruning = ",x)
#print win if value is greater than target
if x >= t:
    print("The winner is Optimus Prime")
#print for Megatron otherwise
else:
    print("The winner is Megatron")

win = 0

for i in range(s):
    arr2 = []
    for j in range(0,8):
        arr2.append(random.randint(min_point, m))

    sc = mn(0,0,True,arr2,minimum,maximum)
    points.append(sc)


    if sc >= t:
        win += 1

maxS = points[0]
for i in points[1:]:
    if i > maxS:
        maxS = i
        
print()
print("=================================")
print()
print("Task2")
print()
print("After the shuffle:")
print("List of all points values from each shuffles: ",points)
print("The maximum value of all shuffles: ",maxS)
print(f"Won {win} times out of {s} number of shuffles")
