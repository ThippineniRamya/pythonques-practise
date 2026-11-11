'''next greater element using brute force'''
# nums=[19,4,2,11,6,5,3,10]
# n=len(nums)
# ans=[-1]*n
# for i in range(0,n):
#     for j in range(i+1,n):
#         if nums[j]>nums[i]:
#             ans[i]=nums[j]
#             break
# print(ans)
# def great(nums):
#     n=len(nums)
#     ans=[-1]*n
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if nums[j]>nums[i]:
#                 ans[i]=nums[j]
#                 break
#     return ans
# a=[19,4,2,11,6,5,3,10]
# print(great(a))
'''next grater element using optimla '''
arr=[19,4,2,11,6,5,3,10]
n=len(arr)
stack=[]
ans=[-1]*n
for i in range(len(arr)-1,-1,-1):

    while len(stack)!=0 and stack[-1]<=arr[i]:
        stack.pop()
    if len(stack)!=0:
        ans[i]=stack[-1]
    
    stack.append(arr[i])
print(ans)
'''next privous greater element'''
# arr=[19,4,2,11,6,5,3,10]
# n=len(arr)
# stack=[]
# ans=[-1]*n
# for i in range(n):
#     while len(stack)!=0 and stack[-1]<=arr[i]:
#         stack.pop()
#     if len(stack)!=0:
#         ans[i]=stack[-1]
    
#     stack.append(arr[i])
# print(ans)