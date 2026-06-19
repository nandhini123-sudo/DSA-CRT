nums = input().split()
l = len(nums)
c = 0

for i in range(l):
    c += 1
    print(c, i, nums[l - i - 1])