# temp=[73,74,75,71,69,72,76,73]
# stack=[]
# n=len(temp)
# ans=[0]*n
# for i in range(n):
#     while len(stack)!=0 and temp[stack[-1]]<temp[i]:
#         prev=stack.pop()
#         ans[prev]=i-prev
#     stack.append(i)
# print(ans)