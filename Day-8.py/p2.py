def BubbleSort(nums):
    c=0
    L=len(nums)
    for j in range(L):
        swapped=False
        for i in range(L-1-j):
            c+=1
            if nums[i] < nums[i+1]:
                nums[i], nums[i+1]=nums[i+1], nums[i]
                swapped=True
            print(c,j,i,nums)
        if not swapped:
            break
    return nums
nums=[1,5,3,4,2]
print(BubbleSort(nums))