# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr    
  
# arr = [64, 34, 25, 12, 22, 11, 90]
# sorted_arr = bubble_sort(arr)
# print(sorted_arr)

# #insertion sort

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr

# arr = [64, 34, 25, 12, 22, 11, 90]
# sorted_arr = insertion_sort(arr)
# print(sorted_arr)


# #selection sort
# def selection_sort(arr):    
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr


# #quick sort
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[len(arr) // 2]
#         left = [x for x in arr if x < pivot]
#         middle = [x for x in arr if x == pivot]
#         right = [x for x in arr if x > pivot]
#         return quick_sort(left) + middle + quick_sort(right)

# arr = [64, 34, 25, 12, 22, 11, 90]
# sorted_arr = quick_sort(arr)
# print(sorted_arr)

#merge sort


def merge_sort(arr):    
    
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr  

arr = [64, 34, 25, 12, 22, 11, 90]
(merge_sort(arr))
print(arr)

# arr1 = [11,7,13,2,5,9,10,4]

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
        
        #division of array into halves
        
#         left_half = arr[:mid]
#         right_half = arr[mid:]
        
#         #recursive call on each half
#         merge_sort(left_half)
#         merge_sort(right_half)
        
#         #iterators for traversing the two halves and main list
#         i = j = k = 0
        
#         #copy of the data to temp arrays left half and right half
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1
            
#         #checking if any element was left in left half
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1
            
#         #checking if any element was left in right half
#         while j < len(right_half):  
#             arr[k] = right_half[j]
#             j += 1
#             k += 1    
    
# (merge_sort(arr1))
# print(arr1)

