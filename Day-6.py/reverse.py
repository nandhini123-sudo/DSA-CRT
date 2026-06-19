#print all unique pair combinations
nums=input().split()
l=len(nums)
#nums.reverse()     #1st method
#nums=nums[::-1]    #2nd method
#for i in range(l):
    #print(nums[l-i-1])#3rd method
for i in range(1,l+1):  #4th method
    print(nums[l-i])
#print(nums)
#for j in range(l):
 #   for i in range(j+1,l):
  #      print(nums[j],nums[i])
