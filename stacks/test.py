'''reverse a string using stack'''
# s="hello"
# stack=[]
# for ch in s:
#     stack.append(ch)
# rev=""
# while stack:
#     rev+=stack.pop()
# print(rev)
'''palindrome using stack'''
# s="madamr"
# stack=[]
# for ch in s:
#     stack.append(ch)
#     is_palin=True
# for ch in s:
#     top=stack.pop()
#     if ch!=top:
#         is_palin=False
#         break
# print(is_palin)

# if is_palin:
#     print("palindrome")
# else:
#     print("not palindrome")
'''valid parenthesisi'''
# def valid(s):
#     stack=[]
#     for i in s:
#         if i=='(' or i=='{' or i=='[':
#             stack.append(i)
#         else:
#             if not stack:
#                 return False
#             top=stack.pop()
#         if i==')' and top!='(':

#             return False
#         if i=='}' and top!='{':
#             return False
#         if i==']' and top!='[':
#             return False
#     return len(stack)==0
# print(valid("{}()[]"))

'''minimum additions to make valid brackets'''
s="()((("
stack=[]
for i in s:
    if i=='(':
        stack.append(i)
    else:
        if len(stack)!=0:
            stack.pop()
        else:
            stack.append(i)
print(len(stack))

