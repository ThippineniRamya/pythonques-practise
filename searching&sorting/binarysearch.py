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
# nums = [1, 3, 5, 7, 9]
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
#     print("element not found")
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
arr = [1, 3, 4, 2, 3,2]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            print("duplicate elemt ",arr[i])
            break