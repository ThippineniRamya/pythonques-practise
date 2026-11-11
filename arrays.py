'''Find the largest element in a list.'''
# l1=[1,23,4,5,6,7]
# large=l1[0]
# for i in l1:
#     if i >large:
#         large=i
# print(large)
'''seconf largest element in a list'''
# l1=[1,23,4,5,6,7]
# large=float('-inf')
# second=float('-inf')
# for nums in l1:
#     if nums>large:
        
#         second=large
#         large=nums
        
#     elif nums>second and nums!=large:
#         second=nums
# print(second)
'''len of list without using len'''
# lst=[1,2,3,4,5]
# count=0
# for i in lst:
#     count+=i
# print(i)
'''sum od elemnst in  a list'''
# lst=[1,2,3,4,5]
# total=0
# for i in lst:
#     total+=i
# print(total)
'''Count even and odd numbers.'''
# l1=[2,3,4,5,7,8,9,10,5]
# count_e=0
# count_o=0
# for i in l1:
#     if i%2==0:
#         count_e+=1
#     else:
#         count_o+=1
# print("even",count_e)
# print("odd",count_o)
'''linear search'''
# arr=[10,20,30,440,50,60]
# target=int(input("enter your target element"))
# found=False
# for i in arr:
#     if i==target:
#         found=True
#         break
# if found:
#     print("element found")
# else:
#     print("element not found")
'''Find the first occurrence'''
# arr = [10, 20, 30, 20, 40, 20]
# target = 20

# for i in range(len(arr)):
#     if arr[i] == target:
#         print("First occurrence:", i)
#         break
'''find last occurence reverse index'''
# arr = [10, 20, 30, 20, 40, 20]
# target = 20

# for i in range(len(arr) - 1, -1, -1):
#     if arr[i] == target:
#         print("Last occurrence:", i)
#         break
'''elemnt serch liner search at index'''
# arr=[10,20,30,40,50]
# target=int(input("element to find"))
# found=False
# for i in range(len(arr)):
#     if arr[i]==target:
#         print("element found at index ",i)
#         found=True
#         break   
# if not found:
#     print("element not found")
'''reverse  a list '''
# l1=[10,20,30,40,50]
# rev=[]
# for i in l1:
#     rev=[i]+rev
# print(rev)

# l1=[10,20,30,40,50]
# left=0
# right=len(l1)-1
# while left<right:
#     l1[left],l1[right]=l1[right],l1[left]
#     left+=1
#     right-=1
# print(l1)
'''Remove duplicate elements from a list.
Find duplicate elements in a list.'''

# list=[10,2,3,4,5,5,6]
# dup=[]
# for i in list:
#     if i not in dup:
#         dup.append(i)
# print(dup)

# print(set(list))# order not preserverd
# using set printitng duplicate elements
# arr = [1, 2, 3, 2, 4, 5, 1, 3]

# seen = set()

# for num in arr:
#     if num not  in seen:
#         seen.add(num)
#     else:
#         print(num)

'''printing only duplicate elemts using nested loops'''
# arr=[1,2,2,44,4,4,5]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):#j=i+1
#         if arr[i]==arr[j]:
#             print(arr[i])
#             break                              
        
# Once I find that this element has a duplicate, stop searching for more duplicates of the same element
'''frequency count'''
# l1 = [10, 20, 10, 30, 20, 40, 30]
# freq={}
# for i in l1:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# print(freq)
'''move all zeros at end'''
# l1 = [10, 20, 0,0,0 ,40, 30]
# list=[]
# for i in l1:
#     if i!=0:
#         list.append(i)
# for i in l1:
#     if i==0:
#         list.append(i)
# print(list)
# l1 = [10, 20, 0,0,0 ,40, 30]
# point=0
# for i in range(len(l1)):
#     if l1[i]!=0:
#         l1[i],l1[point]=l1[point],l1[i]
#         point+=1
# print(l1)
               
'''missing number'''
# list=[1,3,4,5,6]
# n=len(list)+1
# original=n*(n+1)//2
# actual=sum(list)
# missing=original-actual
# print(missing)
'''common elemnts in a list'''
# l1=[1,2,3,4]
# l2=[1,2,67,8]
# common=[]
# for i in l1:
#     for j in l2:
#         if i ==j:
#             common.append(i)
# print(common)

# l1=[1,2,3,4]
# l2=[1,2,67,8]
# common=[]
# s=set(l2)
# for i in l1:
#     if i in s:
#         common.append(i)
# print(common)
'''elements that are present in List 1 but NOT in List 2, then:'''
# l1 = [1, 2, 3, 4]
# l2 = [1, 2, 67, 8]
# s=set(l2)
# for i in l1:
#     if i not in s   :
#         print(i)
'''Check whether two lists contain the same elements'''
# list1=[1,2,3,1,1,1]
# list2=[1,2,3]
# if set(list1) == set(list2):
#     print("Same elements")
'''merge two sorted arrays'''
# num1=[1,1,2,4,6,7]
# num2=[1,2,3,6,7,8,9,10]
# i=0
# j=0
# res=[]
# n=len(num1)
# m=len(num2)
# while i<n and j<m:
#     if num1[i]<num2[j]:
#         if len(res)==0 or res[-1]!=num1[i]:
#             res.append(num1[i])
#         i+=1
#     else:
#         if len(res)==0 or res[-1]!=num2[j]:
#             res.append(num2[j])
#         j+=1

#     while i < n:
#         if len(res) == 0 or res[-1] != num1[i]:
#             res.append(num1[i])
#         i += 1

#     while j < m:
#         if len(res) == 0 or res[-1] != num2[j]:
#             res.append(num2[j])
#         j += 1

# print(res)
'''two sum problems'''
# num=[1,2,3,4,5]
# target=9
# for i in range(len(num)):
#     for j in range(1,len(num)):
#         if num[i]+num[j]==target:
#             print(i,j)
'''frequency of each element'''
# arr=[1,2,1,2,3,4,5,6,]
# freq={}
# for i in arr:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# print(freq)
'''Find frequency of a given number'''
# arr = [2, 3, 2, 5, 3, 2, 4, 5, 3]

# target = 5
# count = 0

# for num in arr:
#     if num == target:
#         count += 1

# print("Frequency:", count)
'''Find the most frequent element'''
# arr = [2, 3, 2, 5, 3, 2, 4, 5, 3]
# count = {}
# for num in arr:
#     if num in count:
#         count[num] += 1
#     else:
#         count[num] = 1
# maximum = 0
# most_frequent = 0
# for num in count:
#     if count[num] > maximum:
#         maximum = count[num]# how many times
#         most_frequent = num # which elemnet

# print("Most frequent:", most_frequent)
# print("Frequency:", maximum)
'''Element that appears only once and non repaeting elemnts'''
# l = [1, 2, 3, 2, 1, 4, 3]
# freq={}
# for i in l:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# for i in l:
#     if freq[i]==1:
#         print(i)

'''repeteting elemts'''
# list=[10,10,20,20,30,50,50,50,78]
# freq={}
# for i in list:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1

# for i in list:
#     if freq[i]>1:
#         print(i)

'''first repeating elemnt '''
# list=[10,10,20,20,30,50,50,50,78]
# freq={}
# for i in list:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1

# for i in list:
#     if freq[i]>1:
#         print(i)
#         break

'''check weather the list is sorted or not'''
# def is_sorted(arr):
#     for i in range(len(arr) - 1):
#         if arr[i] > arr[i + 1]:
#             return False

#     return True
# arr=[1,2,3,6,5]
# print(is_sorted(arr))
'''sort  alist without using sort function'''
# arr=[2,3,1,6,5]
# sort_occr=0# if you want t o know how many times it will sort
# for i in range(len(arr)):
#     for j in range(0,len(arr)-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#             sort_occr+=1
#             # print(arr)
            
# print("sorted",arr)
# print("number of time the list will sort",sort_occr)
'''right rotation of a n arrya k=3 using burte force methid '''
# arr=[2,3,4,5,6,7,8,9,10]
# n=len(arr)
# k=3
# rotations=k%n
# for i in range(rotations):
#     e=arr.pop()
#     arr.insert(0,e)
# print(arr)
'''using slicing right rotation using k=4'''
# arr=[2,3,4,5,6,7,8,9,10]
# k=4
# n=len(arr)
# k=k%n
# arr[:]=arr[n-k:]+arr[:n-k]
# print(arr)
'''Find all pairs with a given sum'''
# arr=[1,2,3,4,5,6]
# target=10
# for i in range(1,len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]+arr[j]==target:
#             print(arr[i],arr[j])

'''find triplet sum fro given number'''
# arr = [1, 2, 3, 4, 5, 6]
# target = 10
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         for k in range(j+1,len(arr)):
#             if arr[i]+arr[j]+arr[k]==target:
#                 print(arr[i] ,arr[j] ,arr[k])
'''print elemts ina  areverse order'''
# arr = [10, 20, 30, 40, 50]

# for i in range(len(arr)-1 , -1, -1):
#     print(arr[i])
'''reverse  a list using loop'''
# arr = [10, 20, 30, 40, 50]
# rev=[]
# for i in arr:
#     rev=[i]+rev
# print(rev)
'''maximum and minum element in a list'''
# arr = [10, 5, 25, 3, 18]

# maximum = arr[0]
# minimum = arr[0]

# for i in range(len(arr)):
#     if arr[i] > maximum:
#         maximum = arr[i]

#     if arr[i] < minimum:
#         minimum = arr[i]

# print("Maximum:", maximum)
# print("Minimum:", minimum)
'''Count pairs whose sum equals target'''
# arr=[1,2,3,4,5,6,7,8]
# target=int(input("enter your target element"))
# count=0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]+arr[j]==target:
#             count+=1
#             print(arr[i],arr[j])

# print("pair count ",count)
'''right rotate by k=2'''
# num=[3,9,5,6,7,2,10,9]
# n=len(num)
# k=5
# k=k%n
# num[:]=num[n-k:]+num[:n-k] #for left num[k:]+num[:k]
# print(num)
'''rotate right by one '''
# num=[3,4,5,6,7,8,0]
# n=len(num)
# num[:]=num[-1:]+num[:n-1]
# print(num)
'''rotate left by one '''
# num = [3, 9, 5, 6, 7, 2, 10, 9]

# num[:] = num[1:] + num[:1]

# print(num)
'''Find the minimum subarray sum'''
# nums = [3, -4, 2, -3, -1, 7]
# min_sub = float("inf")
# n = len(nums)
# for i in range(n):
#     total = 0
#     for j in range(i, n):
#         total = total + nums[j]
#         min_sub = min(min_sub, total)
# print(min_sub)
'''Find the Majority Element/elements taht appreaing more tahn n/2'''
# nums = [2, 2, 1, 1, 1, 2, 2]
# freq={}
# n=len(nums)
# for i in nums:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# for i in freq:
#     if freq[i]>n/2:
#         print(i)
'''Find the Maximum Difference Between Two Elements'''
# nums = [7, 1, 5, 3, 6, 4]

# min_element = nums[0]
# max_diff = 0

# for num in nums:
#     min_element = min(min_element, num)
#     max_diff = max(max_diff, num - min_element)
# print(max_diff)
# '''find longest subarray sum'''
# arr= [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# longest=0
# total=0
# n=len(arr)
# for i in range(n):
#     total+=arr[i]
#     longest=max(longest,total)
#     if total<0:
#         total=0
# print(longest)
# '''find smallest sub array sum'''
# arr=[3, -4, 2, -3, -1, 7, -5]
# small=0
# total=0
# n=len(arr)
# for i in range(n):
#     total+=arr[i]
#     small=min(small,total)
#     if total>0:
#         total=0
# print(small) 

# '''sub array with given sum'''
# arr=[1,2,3,7,5]
# target=3
# # count=0
# left=0
# total=0
# for right in range(len(arr)):
#     total+=arr[right]
#     while total>target:
#         total-=arr[left]
#         left+=1
#     if total==target:
#         print(arr[left:right+1])
#         break
#         # count+=1
# # print(count)
# '''longest sub array with sum k '''
# arr = [10, 5, 2, 7, 1, 9]
# k = 15
# freq = {}
# total = 0
# longest = 0
# for i in range(len(arr)):
#     total += arr[i]
#     if total == k:
#         longest = i + 1
#     if total - k in freq:
#         length = i - freq[total - k]
#         longest = max(longest, length)
#     if total not in freq:
#         freq[total] = i
# print(longest)
# '''Find the Maximum-Length Subarray Containing Only Positive Numbers'''
# arr = [1, 2, 3, -1, 4, 5, 6, 7, -2, 8]
# current = []
# max_subarray = []
# for num in arr:
#     if num > 0:
#         current.append(num)
#         if len(current) > len(max_subarray):
#             max_subarray = max(max_subarray,current)
#     else:
#         current = []
# print("Maximum length:", len(max_subarray))
# print("Subarray:", max_subarray)
# '''Find the maximum difference between two elements'''
# arr = [7, 1, 5, 3, 6, 4]

# minimum = arr[0]
# maximum = arr[0]
# for num in arr:
#     minimum = min(minimum, num)
#     maximum = max(maximum, num)
# print(maximum - minimum)
# '''move positives and negitives alternatly'''
# nums = [1, 2, -3, -4, 5, -6]
# positive = []
# negative = []
# for x in nums:
#     if x >= 0:
#         positive.append(x)
#     else:
#         negative.append(x)
# result = []
# for i in range(max(len(positive), len(negative))):
#     if i < len(positive):
#         result.append(positive[i])
#     if i < len(negative):
#         result.append(negative[i])
# print(result)

'''merge two sorted arays uisng two pointers'''
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
i = 0
j = 0
res = []
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1
while i < len(a):
    res.append(a[i])
    i += 1
while j < len(b):
    res.append(b[j])
    j += 1
print(res) 
# print without list and commas use print(*res)