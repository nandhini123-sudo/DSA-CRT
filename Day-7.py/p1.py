#find min and max
nums=input().split()
print(nums)
#nums[0]=int(nums[0])
#nums[1]=int(nums[1])
#nums[2]=int(nums[2])
#nums[3]=int(nums[3])
#nums[4]=int(nums[4])
#nums[5]=int(nums[5])
#nums[6]=int(nums[6])
#nums[7]=int(nums[7])
for i in range (len(nums)):
    nums[i]=int(nums[i])
    if i%2==0:
        nums[i]=nums[i]**2
    else:
        nums[i]=nums[i]**3
print(nums)


