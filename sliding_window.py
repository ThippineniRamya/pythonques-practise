'''Maximum Sum of K Consecutive Elements
Input:
[2,1,5,1,3,2], k=3
Output:
9
5 + 1 + 3 = 9'''
# arr=[2,1,5,1,3,2]
# k=3
# window_sum=sum(arr[:k])
# max_sum=window_sum
# for  i in range(k,len(arr)):
#     window_sum=window_sum-arr[i-k]+arr[i]#newsum=prev_sum-outgoing+incoming

#     max_sum=max(max_sum,window_sum)
# print(max_sum)
'''Minimum Sum of K Consecutive Elements
Input:
[2,1,5,1,3,2], k=3
Output:
6
2 + 1 + 3 = 6'''
# arr=[2,1,5,1,3,2]
# k=3
# window_sum=sum(arr[:k])
# min_sum=window_sum
# for i in range(k,len(arr)):
#     window_sum=window_sum-arr[i-k]+arr[i]
#     min_sum=min(window_sum,min_sum)
# print(min_sum)