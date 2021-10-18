k,f,i = 1,1,1
nums = int(input())
running = True
while running:   
    if nums > k:
        k+= (f+2)**2
        f+=2 
        i+=1  
         
    elif k>nums:
        i-=1
        break
    else:
        break

print(i) 
