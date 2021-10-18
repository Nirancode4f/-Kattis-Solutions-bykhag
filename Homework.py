nums = input().split(";")
L = []
F = 0
for i in nums:
    try:        
        L.append(int(i))
        F+=1    
        
    except:
        n = i.split("-")      
        for p in range(int(n[0]),int(n[1])+1):
            F+=1  
              
print(F)
