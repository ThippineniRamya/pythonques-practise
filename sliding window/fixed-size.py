'''Maximum Sum of K Consecutive Elements'''
# arr=[2,1,5,1,3,2]
# k=3
# window_sum=0
# for i in range(k):
#     window_sum+=arr[i]
# max_sum=window_sum
# for  i in range(k,len(arr)):
#     window_sum=window_sum-arr[i-k]+arr[i]
#     if window_sum>max_sum:
#         max_sum=window_sum
# print(max_sum)
'''minmum summ of k consequtive element'''
# arr=[2,1,5,1,3,2]
# k=3
# window_sum=0
# for i in range(k):
#     window_sum+=arr[i]
# min_sum=window_sum
# for  i in range(k,len(arr)):
#     window_sum=window_sum-arr[i-k]+arr[i]
#     if window_sum<min_sum:
#         min_sum=window_sum
# print(min_sum)
'''. Average of Every K Elements'''
# arr=[1,3,2,6,-1,4,1,8,2]
# k=5
# l=[]
# window_sum=0
# for i in range(k):
#     window_sum+=arr[i]
# avg=window_sum/k
# l.append(avg)
# for i in range(k,len(arr)):
#     window_sum=window_sum-arr[i-k]+arr[i]
#     avg=window_sum/k
#     l.append(avg)
# print(l)
'''max element in every window'''
# arr = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
# l=[]
# for i in range(len(arr)-k+1):
#     max_ele=arr[i]
#     for j in range(i,i+k):
#         if arr[j]>  max_ele:
#             max_ele=arr[j]
#     l.append(max_ele)
# print(l)
'''Count Even Numbers in Every Window'''
# arr=[2,1,4,6,3,8]
# k=3
# res=[]
# for i in range(len(arr)-k+1):
#     count=0
#     for j in range(i,i+k):
#         if arr[j]%2==0:
#             count+=1
#     res.append(count)
# print(res)
'''Count Vowels in Every Window'''
# s = "abcaeiou"
# k = 3
# l=[]
# for i in range(len(s)-k+1):
#     count=0
#     for j in range(i,i+k):
#         if s[j] in "aeiou":
#             count+=1
#     l.append(count)
# print(l)
'''Count Occurrences of a Given Character in Every Window'''
# s = "aabbaba"
# ch = "a"
# k = 3
# result = []
# for i in range(len(s) - k + 1):
#     count = 0
#     for j in range(i, i + k): 
#         if s[j] == ch:
#             count += 1
#     result.append(count)
# print(result)