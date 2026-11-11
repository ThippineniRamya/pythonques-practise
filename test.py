'''3 sum'''
# nums=[-1,0,1,2,-1,-4]
# res=[]
# n=len(nums)
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
'''best time to buy and sell stockss'''
# prices = [7,1,5,3,6,4]
# min_price=prices[0]
# max_profit=0
# for i  in range(len(prices)):
#     min_price=min(min_price,prices[i])
#     max_profit=max(max_profit,prices[i]-min_price)
# print(max_profit)

# def con_dup(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]==arr[j]:
#                 return True
#         return False
# arr=[1,2,3,4]
# print(con_dup(arr))
'''product except itself'''
# l=[1,2,3,4]
# n=len(l)
# res=[]
# for i in range(n):
#     pro=1
#     for j in range(n):
#         if i!=j:
#             pro*=l[j]
#     res.append(pro)
# print(res)
'''maximum sub array sum'''
# def sub(nums):
#     max_sub=nums[0]
#     total=0
#     for i in range(len(nums)):
#         total=total+nums[i]
#         max_sub=max(max_sub,total)
#         if total<0:
#             total=0
#     return max_sub
# nums=[-2,1,-3,4,-1,2,1,-5,4]
# print(sub(nums))

'''container with most water'''
# ht=[1, 8, 6, 2, 5, 4, 8, 3, 7]
# n=len(ht)
# max_area=0
# left=0
# right=n-1
# while left<right:
#     dis=right-left
#     min_ht=min(ht[left],ht[right])
#     area=dis*min_ht
#     if area>max_area:
#         max_area=area
#     if ht[left]<ht[right]:
#         left+=1 
#     else:
#         right-=1
# print(max_area)

'''move all zero at end'''
# nums=[0, 1, 0, 3, 12]
# pointer=0
# for i in range(len(nums)):
#     if nums[i]!=0:
#         nums[i],nums[pointer]=nums[pointer],nums[i]
#         pointer+=1
# print(nums)
'''reverse  astring '''
# string="hello"
# word=list(string)
# l=0
# r=len(word)-1
# while l<r:
#     word[l],word[r]=word[r],word[l]
#     l+=1
#     r-=1
# print("".join(word))
'''chcek palindrome number'''
# s="madam"
# l=0
# r=len(s)-1
# ispalin=True
# while l<r:
#     if s[l]!=s[r]:
#         ispalin=False
#         break
#     l+=1
#     r-=1
# print(ispalin)
'''first non repeating charecter'''
# s="swiss"
# fre={}
# for i in s:
#     if i not in fre:
#         fre[i]=1
#     else:
#         fre[i]+=1
# for key  in fre:
#     if fre[key]==1:
#         print(key)
#         break
'''remove all duplicate charecters from a string '''
# string="programming"
# dup=""
# for i in string:
#     if i not in dup:
#         dup+=i
# print(dup)
'''longest word in a string'''
# s="I love programming"
# word=s.split()
# longest=""
# for i in word:
#     if i >longest:
#         longest=i
# print(longest)
'''string compression '''
s = "aaabbccccd"
res=""
count=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        res+=s[i-1]+str(count)
        count=1
res+=s[-1]+str(count)
print(res)