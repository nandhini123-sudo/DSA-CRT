#min and max
#min
#nums=list(map(int,input().split()))
#curr_min=float('inf')
#for i in range(len(nums)):
 #   if curr_min>nums[i]:
  #      curr_min=nums[i]
#print(curr_min)
#max
nums=list(map(int,input().split()))
curr_max=float('-inf')
for i in range(len(nums)):
    if curr_max<nums[i]:
        curr_max=nums[i]
print(curr_max)