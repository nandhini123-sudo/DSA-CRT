def BubbleSort(nums):
    c=0
    L=len(nums)
    for j in range(L):
        for i in range(L-1-j):
            c+=1
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1]=nums[i+1], nums[i]
            print(c,j,i,nums)
    return nums
nums=list(range(80))
print(BubbleSort(nums))