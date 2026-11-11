# for i in range(6,1,-1):
'''print 1 to 5 using recurssion'''
# def num(n):
#     if n==0:
#         return 
    
#     num(n-1)
#     print(n)
# num(5)

'''print 5 to 1 using recurssion'''
# def num(n):
#     if n==0:
#         return 
#     print(n)
#     num(n-1)
   
# num(5)

"""get none valeu"""
# def num(n):
#     if n==0:
#         return 
#     print(n)
#     num(n-1)
   
# print(num(5))

'''Find the sum of numbers from 1 to N.using recurssion'''
# def sum_num(n):
#     if n==1:
#         return 1
#     return n+sum_num(n-1)
# print(sum_num(5))
'''factorial of function'''
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))
'''power of a number using recursion'''
# def pow(base,exp):
#     if exp==0:
#         return 1
#     return base*pow(base,exp-1)
# print(pow(2,5))
'''coutn of digits'''
# def count_digit(digit,count):
#     if digit==0:
#         return count
#     return count_digit(digit//10,count+1)
# print(count_digit(51235,0))

# l=[10,20,30,40]
# sum=0
# for i in l:
#     sum+=i
# print(sum)

# '''even number suisng recursisio'''''

'''fibnocci using recursion'''
# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1)+fib(n-2)
# n=int(input("enter number"))
# res=[]
# for i in range(n):
#     res.append(fib(i))
#     # print(fib(i),end=" ")
# print(res)

# lis=[12,3,4,5,6,1,7]
# target=10
# res=[]
# for i in range(len(lis)):
#     for j in range(i+1,len(lis)):
#         if lis[i]+lis[j]==target:
#             res.append((lis[i],lis[j]))
# print(res)