nums=[1,2,5,4,3,7]
#def partition(nums):
 ##  return [nums[0:l//2],nums[l//2:l]]
#print(partition(nums))
def S(nums):
    if len(nums)<=1:   return nums
    L=len(nums)
    left=nums[:L//2]
    right=nums[L//2: ]
    print(S(left),S(right))
    return nums
S(nums)