h,w,n = map(int,input().split())
brick = list(map(int,input().split()))
width,complete=w,False
i = 0
for b in brick:
    if complete == False:
        if b>w:
            complete = -1            
        else: 
            w -= b
            if w == 0:
                w = width
                if h == 0:
                    complete = -2
                h -= 1
            if h == 0 :
                complete = 2    
if complete == -1:
    print("No")
else:
    print("Yes")
