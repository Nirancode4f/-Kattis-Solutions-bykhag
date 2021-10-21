list_right= []
list_wrong = []
score = 0
count_right = 0
nums = ''
while nums != "-1":
    nums = input()
    if nums != "-1":
        if "right" in nums.split() and nums.split()[1] not in list_right:
            count_right += 1
            score += int(nums.split()[0])      
            x = list_wrong.count(nums.split()[1])
            score+= 20*x
            list_right.append(nums.split()[1])
        else :
            list_wrong.append(nums.split()[1])       
print(str(count_right), str(score))
