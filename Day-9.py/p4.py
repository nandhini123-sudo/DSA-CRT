# # arr1=[1,3,4,6]
# # arr2=[2,5,7,8]
# # arr3=arr1+arr2
# # print(arr3)
# # def insertion_sort(arr):
# #     n = len(arr)
# #     for i in range(1, n):
# #         key = arr[i]
# #         j = i - 1
        
# #         while j >= 0 and arr[j] > key:
# #             arr[j + 1] = arr[j]
# #             j -= 1
            
# #         arr[j + 1] = key
        
# #     return arr

# # print(insertion_sort(arr3))


# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     leftHalf = arr[:mid]
#     rightHalf = arr[mid:]

#     sortedLeft = mergeSort(leftHalf)
#     sortedRight = mergeSort(rightHalf)

#     return merge(sortedLeft, sortedRight)

# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result

# unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
# sortedArr = mergeSort(unsortedArr)
# print("Sorted array:", sortedArr)


def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def mergeSort(arr):
    step = 1  # Starting with sub-arrays of length 1
    length = len(arr)
    
    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]
            
            merged = merge(left, right)
            
            # Place the merged array back into the original array
            for j, val in enumerate(merged):
                arr[i + j] = val
                
        step *= 2  # Double the sub-array length for the next iteration
        
    return arr

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)
