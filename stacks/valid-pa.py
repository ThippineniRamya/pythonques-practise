'''valid parenthesis or balanced parenthesis'''
# def valid(s):
#         stack=[]
#         for ch in s:
#             if ch == '(' or ch == '{' or ch == '[':
#                 stack.append(ch)
#             else:
#                 if len(stack)==0:
#                     return False
#                 else:
#                     top = stack.pop()
#                 if ch == ')' and top != '(':
#                     return False
#                 if ch == '}' and top != '{':
#                     return False
#                 if ch == ']' and top != '[':
#                     return False
#         return len(stack) == 0
# print(valid("{}[]()")) 
'''minimum adition to make valid'''
# s="()(("
# stack=[]
# addition=0
# for i in s:
#     if i =='(':
#         stack.append(i)
#     else:
#         if len(stack)!=0:
#             stack.pop()
#         else:
#             addition+=1
# addition+=len(stack)

# print(addition)


             