# import heapq
# nums=[10,8,20,7,6,15]
# nums=[-num for num in nums]
# heapq.heapify(nums)
# print(nums)
# nums=[-num for num in nums]
# print(nums)

# import heapq
# nums=[10,8,20,7,6,15]
# max_heap=[]
# nums=[-num for num in nums]
# for i in nums:
#     heapq.heappush(max_heap,i)
#     print(max_heap)
# max_heap=[-j for j in max_heap]
# print(nums)

import heapq
nums=[10,8,20,7,6,15]
max_heap=[]
nums=[-num for num in nums]
for i in nums:
    heapq.heappush(max_heap,i)
    print(max_heap)
for i in nums:
    heapq.heappop(max_heap)
    print(max_heap)