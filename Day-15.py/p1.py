# #Min heap
# import heapq
# nums=[7,1,4,3]
# heapq.heapify(nums)
# print(nums)


#find kth min
# import heapq
# nums=[8,1,2,3,6,7]
# k=2
# min_heap=[]
# for i in nums:
#     heapq.heappush(min_heap,i)
#     print(min_heap)


import heapq
nums=[1,2,4,3,5]
k=2
min_heap=[]
for i in nums:
    heapq.heappush(min_heap,i)  #push
for i in min_heap:
    heapq.heappop(min_heap)   #pop
    print(min_heap[0],min_heap)

