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

# import heapq
# nums=[10,8,20,7,6,15]
# max_heap=[]
# nums=[-num for num in nums]
# for i in nums:
#     heapq.heappush(max_heap,i)
#     print(max_heap)
# for i in nums:
#     heapq.heappop(max_heap)
#     print(max_heap)


import heapq
nums=[3,2,1,7,5,6,4]
k=2
min_heap=[]
for i in nums:
    heapq.heappush(min_heap,i)
    if len(min_heap)>k:
        heapq.heappop(min_heap)
    print(min_heap)