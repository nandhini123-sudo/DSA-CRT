nums =list(map(int,input().split()))

for i in range(1,len(nums)):
    if i*i>=len(nums):
        break
    nums[i*i]=nums[i*i]**2

print(nums)