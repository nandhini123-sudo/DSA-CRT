#print all unique pair combinations
nums=input().split(",")
l=len(nums)
for j in range(l):
    for i in range(j+1,l):
        print(nums[j],nums[i])
