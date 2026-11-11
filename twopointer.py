'''Reverse an Array
Input:
[1,2,3,4,5]
Output:
[5,4,3,2,1]'''
# arr=[1,2,3,4,5]
# r=len(arr)-1
# l=0
# while l<r:
#     arr[l],arr[r]=arr[r],arr[l]
#     l+=1
#     r-=1
# print(arr)
'''reverse a string'''
# st="python"
# word=list(st)
# l=0
# r=len(word)-1
# while l<r:
#     word[l],word[r]=word[r],word[l]
#     l+=1
#     r-=1
# print("".join(word))
'''Check Palindrome
Input:
"madam"
Output:
Palindrome'''
# s="madam"
# ispalin=True
# l=0
# r=len(s)-1
# while l<r:
#     if s[l]!=s[r]:

#         ispalin=False
#         break
#     l+=1
#     r-=1
# print(ispalin)
'''Array = [1,2,3,4,6]
Target = 6'''
# arr=[1,2,3,4,6]
# target=6
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]+ arr[j]==target:
#             print([arr[i],arr[j]])

'''9. Count Pairs With Target Sum
Input:
Array = [1,2,3,4,5,6]
Target = 7'''
# arr=[1,2,3,4,5,6]
# target=7
# c=0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]+arr[j]==target:
#             c+=1
#             print((arr[i],arr[j]),end="")

# print(c)
'''remove duplicates from sorted array'''
'''Pair With Given Difference
Input:
Array = [1,3,5,8,10]
Difference = 5'''
# arr=[1,3,5,8,10]
# diff_target=5
# res=[]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[j]-arr[i]==diff_target:
#             res.append((arr[i],arr[j]))
# print(res)
'''move zeros'''
# l=[1,2,0,3,0,5,0]
# n=len(l)
# j=0
# for i in range(n):
#     if (l[i]!=0):
#         l[i],l[j]=l[j],l[i]
#         j+=1
# print(l)
'''3 sum'''
# nums = [-1,0,1,2,-1,-4]
# n=len(nums)
# res=[]
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             sum_three=nums[i]+nums[j]+nums[k]
#             if sum_three==0:
#                 trip=[nums[i],nums[j],nums[k]]
#                 trip.sort()
#                 if trip not in res:
#                     res.append(trip)
# print(res)
'''two sum 2'''
# nums=[2,7,11,15]
# target=9
# n=len(nums)
# left=0
# right=n-1
# while left<right:
#     current_sum=nums[left]+nums[right]
#     if current_sum==target:
#         print([nums[left],nums[right]])
#         break
#     elif current_sum<target:
#         left+=1
#     else:
        # right-=1
'''sort colours'''
# nums=[0,1,2,0,1,2,1,1]
# n=len(nums)
# zero=[]
# one=[]
# two=[]
# for num in nums:
#     if num==0:
#         zero.append(num)
#     elif num==1:
#         one.append(num)
#     else:
#         two.append(num)
# nums[:]=zero+one+two
# print(nums)
'''boats to save the people'''
# people=[3,2,2,1]
# limit=3
# n=len(people)
# boat_count=0
# left=0
# right=n-1
# while left<right:
#     if people[left]+people[right]<=limit:
#         left+=1
#     right-=1
#     boat_count+=1
# print(boat_count)
'''container with most water'''
# ht=[1,8,6,2,5,4,8,3,7]
# n=len(ht)
# max_area=0
# for i in range(n):
#     for j in range(i+1,n):
#         dis=j-i
#         min_area=min(ht[i],ht[j])
#         area=dis*min_area
#         if area>max_area:
#             max_area=area
# print(max_area)
# def trap(height):
#     left = 0
#     right = len(height) - 1
#     left_max = 0
#     right_max = 0
#     water = 0
#     while left < right:
#         if height[left] <= height[right]:
#             if height[left] >= left_max:
#                 left_max = height[left]
#             else:
#                 water += left_max - height[left]
#             left += 1
#         else:
#             if height[right] >= right_max:
#                 right_max = height[right]
#             else:
#                 water += right_max - height[right]
#             right -= 1
#     return water
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trap(height))

'''merge two sorte arrays or union'''
# num1=[1,1,1,2,3,4]
# num2=[1,2,3,5,6,7,8,9,10]
# n=len(num1)
# m=len(num2)
# i=0
# j=0
# res=[]
# while i<n and j<m:
#     if num1[i]<=num2[j]:
#         if len(res)==0 or res[-1]!=num1[i]:
#             res.append(num1[i])
#         i+=1
#     else:
#         if len(res)==0 or res[-1]!=num2[j]:
#             res.append(num2[j])
#         j+=1
# while i<n:
#         if len(res)==0 or res[-1]!=num1[i]:
#             res.append(num1[i])
#         i+=1
# while j<m:
#      if len(res)==0 or res[-1]!=num2[j]:
#           res.append(num2[j])
#      j+=1
# print(res)        

'''Check Anagram
Input:  
String 1 = listen
String 2 = silent
Output:
Anagram'''
# from collections import Counter
# s1="listen"
# s2="silent"
# if Counter(s1)==Counter(s2):
#     print("anagram")
# else:
#     print("not an angram")
'''Reverse Only Letters
Input:
"a-bC-dEf-ghIj"
Output:
"j-Ih-gfE-dCba"'''
# a="a-bC-dEf-ghIj"
# s=list(a)
# i=0
# j=len(s)-1
# while i<j:
#     if not s[i].isalpha():
#         i+=1
#     elif not s[j].isalpha():
#         j-=1
#     else:
#         s[i],s[j]=s[j],s[i]
#         i+=1
#         j-=1
# print("".join(s))
'''38. Squares of Sorted Array
Input:
[-4,-1,0,3,10]'''
# arr=[-4,-1,0,3,10]
# for i in range(len(arr)):
#     arr[i]=arr[i]*arr[i]
# arr.sort()
# print(arr)