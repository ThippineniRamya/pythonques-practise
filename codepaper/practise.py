'''count frequency'''
s="programming"

freq={}
for i in s:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
# print(freq)
for key,value in freq.items():
    print(key,"->",value,end=" " )
'''largest number in a list'''
# list=[1,4,56,34,4]
# large=list[0]
# for i in list:
#     if large>list[i]:
#         large=i
# print(large)