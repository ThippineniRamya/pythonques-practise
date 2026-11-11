# nums = [1, 3, 5, 7, 9]
# target = 7
# l=0
# r=len(nums)-1
# found=False
# while l<r:
#     mid=(l+r)//2
#     if nums[mid]==target:
#         print("element found at index",mid)
#         found=True
#         break
#     elif nums[mid]<target:
#         l=mid+1
#     else:
#         r=mid-1
# if not found:
#     print("element not fount")
'''binary search'''
# nums = [1, 3, 5, 10, 9]
# target = 7
# res=-1 
# left=0
# right=len(nums)-1
# while left<right:
#     mid=(left+right)//2
#     if nums[mid]<target:
#         left=mid+1
#     elif nums[mid]>target:
#         right=mid-1
#     else:
#         res=mid
#         break
# if res !=-1:
#     print("element found at index",mid)
# else:
#     print("element not found",res)
'''linaer search'''
# nums = [1, 3, 5, 7, 9]
# target = 10
# for i in range(len(nums)):
#     if nums[i]==target:
#         print("elemnt found at indes",i)
#         break
# else:
#     print("element not found")
'''linears search first occurence'''
# arr=[2,4,2,6,2]
# target=2
# for i in range(len(arr)):
#     if arr[i]==target:
#         print("element found at index",i)
#         break
# else:
#     print("element not found")
'''liner search element found at last occurence'''
# arr=[2,4,2,6,2]
# target=2
# for i in range(len(arr)-1,-1,-1):
#     if arr[i]==target:
#         print("element found at index",i)
#         break
# else:
#     print("element not found")
'''linear search count occurences'''
# arr = [1, 2, 3, 2, 4, 2]
# target = 2
# count=0
# for i in range(len(arr)):
#     if arr[i]==target:
#         count+=1
# print(count)
'''maximum elemt in a n arr'''
# arr=[1,2,3,4,5,6]
# max_ele=0
# for i in arr:
#     if i>max_ele:
#         max_ele=i
# print(max_ele)
'''index of an smallest element'''
# arr=[7,3,9,2,5]	
# small=arr[0]
# index=0
# for i in range(len(arr)):
#     if arr[i] <small:
#         small=arr[i]
#         index=i
# print("smallest numde",small)
# print("index of smallest number",index)
'''find all occurences'''
# arr = [1, 2, 3, 2, 4, 2]
# x = 2
# res = []
# for i in range(len(arr)):
#     if arr[i] == x:
#         res.append(i)
# print("All occurrences:", res)
'''fiind duplicaete element'''
# arr = [1, 3, 4, 2, 3,2]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]==arr[j]:
#             print("duplicate elemt ",arr[i])
#             break
'''Find Peak Element'''
# arr = [1, 3, 20, 4, 1, 0]
# n=len(arr)
# for i in range(n):
#     if (i==0 or arr[i]>arr[i-1] ) and (i==n-1 or arr[i]>arr[i+1]):
#         print("peak element",arr[i])
#         print("peka element index",i)
'''peak elemnt using binary search'''
# arr = [2, 4, 8, 10, 6, 3]
# left = 0
# right = len(arr) - 1
# while left <right:
#     mid = (left + right) // 2
#     if arr[mid] < arr[mid + 1]:
#         left = mid + 1
#     else:
#         right = mid
# print(arr[left])#we can print right
# print(left)#right also 
'''first and last occurence of an element'''
# arr = [1, 2, 3, 3, 3, 3, 4, 5]
# target = 3
# first=-1
# last=-1
# n=len(arr)
# for i in range(n):
#     if arr[i]==target:
#         if first==-1:
#             first=i
#         last=i
# print(first,last)
'''first and last occurence of an element using binary search'''
# arr = [1, 2, 2, 2, 2, 3, 4, 5]
# x = 2
# n = len(arr)

# # First occurrence
# left = 0
# right = n - 1
# first = -1

# while left <= right:
#     mid = (left + right) // 2

#     if arr[mid] == x:
#         first = mid
#         right = mid - 1

#     elif arr[mid] < x:
#         left = mid + 1

#     else:
#         right = mid - 1

# # Last occurrence
# left = 0
# right = n - 1
# last = -1

# while left <= right:
#     mid = (left + right) // 2

#     if arr[mid] == x:
#         last = mid
#         left = mid + 1

#     elif arr[mid] < x:
#         left = mid + 1

#     else:
#         right = mid - 1

# print("First occurrence:", first)
# print("Last occurrence:", last)
'''median of two sorted arrays'''
# arr1 = [1, 2]
# arr2 = [3, 4]
# arr=arr1+arr2
# arr.sort()
# n=len(arr)
# mid=n//2
# if n%2==1:
#     median=arr[mid]
# else:
#     median=(arr[mid]+arr[mid-1])/2
# print("median",median)
'''search 2D matrix'''
# matrix=[
#     [1,3,5,7],
#     [10,11,16,20],
#     [23,30,34,60]
# ]
# found=False
# target=13
# for i in matrix:
#     for j in matrix:
#         if j==target:
#             found=True
#             break
# print(found)

'''search 2d matric using binary search '''
# matrix=[
#     [1,3,5,7],
#     [10,11,16,20],
#     [23,30,34,60]
# ]
# target=16
# row=len(matrix)
# col=len(matrix[0])
# left=0
# right=(row*col)-1
# found=False
# while left <=right:
#     mid=(left+right)//2
#     r=mid//col
#     c=mid%col
#     mid_value=matrix[r][c]
#     if mid_value==target:
#         found=True
#         break
#     elif mid_value<target:
#         left=mid+1
#     else:
#         right=mid-1
# # print(found)
# print(r,c,mid_value,mid)
'''search array in rotated sorted array  brute force'''
nums=[4,5,6,7,0,1,2,]
target=10
n=len(nums)
res=-1
for i in range(n):
    if nums[i]==target:
        res=i
        print(res)
        break
else:
    print(res)