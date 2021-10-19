right_friend_ans = int(input())
my_ans = input()
friend_ans = input()
same = 0
not_same = 0
for my_ans,friend_ans in zip(my_ans,friend_ans):
    if my_ans == friend_ans:
        same+=1
    else:
        not_same+=1
print(min(same,right_friend_ans) + min(not_same,same+not_same- right_friend_ans))
