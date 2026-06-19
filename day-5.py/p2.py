#print numbers
nums=[1,2,3,1,2,3]
nums.append(4)
x=nums.copy()
print(nums)
nums.clear()
print(nums,x)
print(x.count(1))