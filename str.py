'''Reverse a String'''
# s="python"
# rev=""
# for i in s:
#     if i not in rev:
#         rev=i+rev
# print(rev)
'''Check Palindrome'''
# s=input("enter your number")
# n=len(s)
# left=0
# right=n-1
# while left<right:
#     if s[left]!=s[right]:
#         print("not palindrome")
#         break
#     left+=1
#     right-=1
# else:
#     print("palindrom")
'''Count Characters  ,Input: hello,Output: 5'''
# str=input("enter your str")
# count=0
# for i in str:
#     count+=1
# print(count)

'''4. Count Vowels,Input: programming,Output: 3'''
# s="programming"
# c=0
# for i in s:
#     if i in "aeiou":
#         c+=1
# print(c)

'''5. Count Consonants       Input: hello,Output: 3'''
# s="programming"
# c=0
# for i in s:
#     if i not in "aeiou":
#         c+=1
# print(c)

'''# 6. Count Spaces  Input: python is easy   Output: 2'''
# s="python is easy"
# c=0
# for i in s:
#     if i.isspace():
#         c+=1
# print(c)

'''# 8. Remove Spaces  Input: python is easy   Output: pythoniseasy'''
# s=" python is easy "
# s.replace(" ","")
# print(s.replace(" ",""))

# s="python is easy"
# str=""
# for i in s:
#     if i!=" ":
#         str+=i
# print(str)
'''Count Number of Words      Input: Python is very easy  Output: 4'''
# s="Python is very easy"
# split=s.split()
# count=0
# for i in split:
#     count+=1
# print(count)
'''Find Longest Word   Input: Python programming is easy Output: programming'''
# s="Python programming is easy"
# longest=""
# for i in s.split():
#     if len(i)>len(longest):
#         longest=i
# print(longest)
'''Reverse Each Word  Input: python is easy Output: nohtyp si ysae'''
# s = "python is easy"
# result = " ".join(word[::-1] for word in s.split())
# print(result)

# s = "python is easy"
# word = ""
# result = ""
# for ch in s:
#     if ch != " ":
#         word += ch
#     else:
#         result += word[::-1] + " "
#         word = ""
# result += word[::-1]
# print(result)
'''reverse words order'''
# s="python is easy to learn"
# result = " ".join(s.split()[::-1])
# print(result)
'''Find Word with Maximum Vowels  Input: apple orange sky Output: orange'''
s="apple orange sky"
max=""
vowel_count=0
for i in s.split():
    count=0
    for ch in i:
        if ch in "aeiou":
            count+=1
    if count>vowel_count:
        vowel_count=count
        max=i
print(max)
'''Count Vowels in Each Word  Input: python is easy  Output:python → 1
is → 1
easy → 2'''
# s="python is easy"

# for i in s.split():
#     count=0
#     for ch in i:
#         if ch in "aeiou":
#             count+=1
#     print(f"{i}->{count}")
'''Count Letters and Digits Input: abc123'''
# s="abc123"
# count_l=0
# count_d=0
# for i in s:
#     if i.isalpha():
#         count_l+=1
#     else:
#         count_d+=1
# print(f"""count letter{count_l} 
# count digits {count_d}""")
'''freauency od each cahrectre'''
# s="hello"
# fre={}
# for i in s:
#     if i not in fre:
#         fre[i]=1
#     else:
#         fre[i]+=1
# print(fre)
'''Find Frequency of a Given Character  Input: programming, g Output: 2'''
# s="programming"
# target="g"
# count=0
# for i in s:
#     if i==target:
#         count+=1
# print(count)
'''Find Most Frequent Character Input: aabbccc Output: c'''
# s="aabbcccc"
# freq={}
# for i in s:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# max_freq=0
# max_word=""
# for  key in freq:

#     if freq[key]>max_freq:
#         max_freq=freq[key]
#         max_word=key
# print(max_word,max_freq)
'''Find Least Frequent Character'''
# s="aabbc"
# freq={}
# for i in s:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# least_freq=float('inf')

# element=""
# for i in freq:
#     if freq[i]<least_freq:
#         least_freq=freq[i]
#         element=i
# print(least_freq,element)
'''Characters Appearing Once'''
# s="aabbce"
# freq={}
# for i in s:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# for i in freq:
#     if freq[i]==1:
#         print(i)
'''Characters Appearing More Than Once
Input: programming
Output: r g m'''
# s="programming"
# freq={}
# for i in s:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# for key in freq:
#     if freq[key]>1:
#         print(key,end=" ")
'''remove duplicate values  oputput "progamin"'''
# s="programming"
# dup=[]
# for i in s:
#     if i not in dup:
#         dup.append(i)
# print("".join(dup))
'''Print Duplicate Characters
Input: programming
Output: r g m'''
# s="programming"
# seen = set()
# for num in s:
#     if num not  in seen:
#         seen.add(num)
#     else:
#         print(num)
'''contain duplicates'''
# def dup(s):
#     n=len(s)
#     for i in range(n):
#         for j in range(i+1,n):
#             if s[i]==s[j]:
#                 return True
#     return False
# obj=dup("programming")
# print(obj)
'''all charecters are unique or unique charecters in optimal'''
# s="programming"
# seen=set()
# for i in s:
#     if i in seen:
#         print('not uniques')
#         break
#     seen.add(i)
# else:
#     print("all are unique")
'''print only duplicates'''
# s="aabbccdef"
# seen=set()
# for i in s:
#     if i not in seen:
#         seen.add(i)
#     else:
#         print(i)

# s="abc"
# seen=set()
# for i in s:
#     if i in seen:
#         print("not uniue and duplicates")
#         break
# else:
#     print("uniques not duplicates")
'''First Non-Repeating Character
Input: aabbcde
Output: c'''
# s="aabbcde"
# freq={}
# for i in s:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# for key in freq:
#     if freq[key]==1:
#         print(key)
#         break
'''First Repeating Character
Input: abcdbea
Output: b'''
# s="abcdbea"
# freq={}
# for i in s:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# for key in freq:
#     if freq[key]>1:
#         print(key)
#         break 
'''check palindrome'''
# s="madam"
# is_palindrome=True
# left=0
# right=len(s)-1
# while left<right:
#     if s[left]!=s[right]:
#         is_palindrome=False
#         break
#     left+=1
#     right-=1
# print(is_palindrome)
'''Minimum Characters to Remove to Make Palindrome
Input: abca
Output: 1'''
# s="abca"
# left=0
# n=len(s)
# right=n-1
# count=0
# while left<right:
#     if s[left]!=s[right]:
#         count+=1
#         left+=1
#     else:
#         left+=1
#         right-=1
# print(count)
'''Minimum Characters to Add to Make Palindrome
Input: abc
Output: 2'''
# s = "abc"
# for i in range(len(s)):
#     part = s[i:]
#     if part == part[::-1]:
#         print(i)
#         break


'''Longest Palindromic Substring
Input: babad
Output: bab'''
# s="babad"
# n=len(s)
# longest=""
# def expandroundcenter(left,right):
#     while left>=0 and right<n and s[left]==s[right]:
#         left-=1
#         right+=1
#     return s[left+1:right]
# for i in range(n):
#     odd_palind=expandroundcenter(i,i)
#     even_palind=expandroundcenter(i,i+1)
#     if len(odd_palind)>len(longest):
#         longest=odd_palind
#     if len(even_palind)>len(longest):
#         longest=even_palind
# print(longest)
'''Count Number of Words
Input: Python is very easy
Output: 4'''
# s="Python is very easy"
# c=0
# for i in s.split():
#     c+=1
# print(c)
'''Find Longest Word
Input: Python programming is easy
Output: programming'''
# s="Python programming is easy"
# word=s.split()
# longest=word[0]
# for i in word:
#     if i >longest:
#         longest=i
# print(longest)
'''Reverse Each Word
Input: python is easy
Output: nohtyp si ysae'''
# s = "python is easy"
# words = s.split()
# result = []
# for word in words:
#     result.append(word[::-1])
# print(' '.join(result))
'''Reverse Word Order
# Input: python is easy
# Output: easy is python'''
# s="python is easy"
# print(" ".join(s.split()[::-1]))
'''. Count Vowels in Each Word
Input: python is easy'''
# s="python is easy"
# word=s.split()

# for i in word:
#     count=0
#     for ch in i:
#         if ch in "aeiou":
#             count+=1
#     print(f"{i}--{count}")
'''Find Word with Maximum Vowels
Input: apple orange sky
Output: orange'''
# s = "apple orange sky"
# words = s.split()
# max_word = ""
# max_vowels = 0
# for word in words:
#     count = 0
#     for ch in word:
#         if ch in "aeiou":
#             count += 1
#     if count > max_vowels:
#         max_vowels = count
#         max_word = word
# print(max_word)
# Count Uppercase and Lowercase
# s = "PyThOn"

# upper = lower = 0

# for ch in s:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1

# print("Uppercase:", upper)
# print("Lowercase:", lower)
# 36. Count Letters and Digits
# s = "abc123"

# letters = digits = 0

# for ch in s:
#     if ch.isalpha():
#         letters += 1
#     elif ch.isdigit():
#         digits += 1

# print("Letters:", letters)
# print("Digits:", digits)
# 37. Count Special Characters
# s = "abc@123#"

# count = 0

# for ch in s:
#     if not ch.isalnum():
#         count += 1

# print(count)
# 38. Print Only Digits
# s = "abc123xyz45"

# for ch in s:
#     if ch.isdigit():
#         print(ch, end="")

# Output:

# 12345
# 39. Print Only Alphabets
# s = "abc123xyz"

# for ch in s:
#     if ch.isalpha():
#         print(ch, end="")

'''rotate  a string right by one'''
# s="python"
# n=len(s)
# s=s[-1:]+s[0:n-1]
# print(s)
'''left by on position'''
# s = "python"
# s = s[1:] + s[0]
# print(s)
'''43. Right Rotate by K=2  Input: abcdef,    Output: efabcd'''
# s="abcdef"
# k=2
# n=len(s)
# k=k%n
# s=s[n-k:]+s[:n-k]
# print(s)
'''left rotate k=2'''
# s="abcdef"
# k=2
# n=len(s)
# k=k%n
# s=s[k:]+s[:k]
# print(s)
'''Check Whether One String Is Rotation of AnotherInput:
String 1: abcde
String 2: cdeab'''
# s1="abcde"
# s2="deabc"
# if len(s1)!=len(s2):
#     print("False") 
# double=s1+s1
# if s2 in double:
#     print("True")
# else:
#     print("false")
'''Check Palindrome Using Two Pointers     Input: racecar Output: Palindrome'''
# def palin(s):
#     is_palindrome=True
#     n=len(s)
#     l=0
#     r=n-1
#     while l<r:
#         if s[l]!=s[r]:
#             is_palindrome= False
#         l+=1
#         r-=1
#     return is_palindrome
# print(palin("racecar"))
'''Reverse String Using Two Pointers Input: abcdef  Output: fedcba'''
# str="abcdef"
# s=list(str)
# n=len(str)
# l=0
# r=n-1
# while l<r:
#     s[l],s[r]=s[r],s[l]
    
#     l+=1
#     r-=1
# print("".join(s))
'''Remove Duplicate Characters  Input: aabbcc  Output: abc'''
# s="aabbcc"
# dup=[]
# for i in s:
#     if i not in dup:
#         dup+=i
# print("".join(dup))
'''Count Occurrences of a Substring
String: abababa
Substring: aba'''

'''Check Whether Substring Exists
Input: programming
Substring: gram'''
# s="programming"
# sub="gram"
# if sub in s:
#     print("substring found")
# else:
#     print("not sub stringg")
'''Find First Occurrence
Input: hello
Character: l'''
# s="hello"
# char="l"
# for i in range(len(s)):
#     if s[i]==char:
#         print(i)
#         break         
'''check anagram'''
# s1="silent"
# s2="listeeen"
# if sorted(s1)==sorted(s2):
#     print("anagram")
# else:
#     print("not  an anagram")

# from collections import Counter
# s1="listen"
# s2="silent"
# if Counter(s1)==Counter(s2):
#     print("it is a anagram")
# else:
#     print("not an anagram")
'''sum of digits in string abc123'''
# str="abc123"
# sum=0
# for i in str:
#     if i.isdigit():
#         sum+=int(i)
# print(sum)
'''first occurence charter swiss'''
# s="swiss"
# freq={}
# for i in s:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# for i in freq:
#     if freq[i]==1:
#         print(i)
#         break
'''Character With Maximum Frequency
Input: mississippi
Output: i'''
# s="mississippi"
# freq={}
# for i in s:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# max=0
# max_word=""
# for i in freq:
#     if freq[i]>max:
#         max=freq[i]
#         max_word=i
# print(max,max_word)
'''minimum deletion made to make unique'''
# s="aabbcc"
# dup=[]
# for i in s:
#     if i not in dup:
#         dup.append(i)
# print(len(dup))
'''misising charecter'''
# s="abcdefghijklmnopqstuvwxyz"
# for i in "abcdefghijklmnopqrstuvwxyz":
#     if i not in s:
#         print(i)
'''find extra chaecter in two strings'''
# s1 = "abcde"
# s2 = "abxcde"

# for ch in s2:
#     if ch not in s1:
#         print(ch)
'''Longest Substring Without Repeating Characters'''
# s = "abcabcbb"
# left = 0
# max_len = 0
# seen = set()
# for right in range(len(s)):
#     while s[right] in seen:
#         seen.remove(s[left])
#         left += 1
#     seen.add(s[right])
#     max_len = max(max_len, right - left + 1)
# print(max_len)
'''Longest Substring With K Distinct Characters'''
# s = "aabacbebebe"
# k = 3
# left = 0
# max_len = 0
# freq = {}
# for right in range(len(s)):
#     freq[s[right]] = freq.get(s[right], 0) + 1
#     while len(freq) > k:
#         freq[s[left]] -= 1
#         if freq[s[left]] == 0:
#             del freq[s[left]]
#         left += 1
#     max_len = max(max_len, right - left + 1)
# print(max_len)
'''group of angrams'''
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# group={}
# for word in strs:
#     sort_word="".join(sorted(word))
#     if sort_word not in group:
#         group[sort_word]=[]
#     group[sort_word].append(word)
# print(list(group.values()))
'''is subsequence392'''

# def seq(s, t):
#     i = 0
#     j = 0
#     while i < len(s) and j < len(t):
#         if s[i] == t[j]:
#             i += 1
#         j += 1
#     return i == len(s)
# obj = seq("ace", "abcde")
# print(obj)
'''check is plaindrome two pointers '''
# s="madam"
# left=0
# right=len(s)-1
# is_palindrome=True
# while left<right:
#     if s[left]!=s[right]:
#         is_palindrome=False
#         break
#     left+=1
#     right-=1
# print(is_palindrome)
'''. Reverse String Using Two Pointers
Input: abcdef
Output: fedcba'''
# s="abcef"
# st=list(s)
# n=len(st)
# l=0
# r=n-1
# while l<r:
#     st[l],st[r]=st[r],st[l]
#     l+=1
#     r-=1
# print("".join(st))
'''. First Character That Occurs Once
Input: swiss
Output: w'''
# s="swiss"
# freq={}
# for i in s:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# for key in freq:
#     if freq[key]==1:
#         print(key)
#         break
'''sum of digits in a string'''
# s="abc123"
# c=0
# for i in s:
#     if i.isdigit():
#         c+=int(i)
# print(c)
'''Extract Numbers From String
Input: abc12def34
Output: 12 34'''
# s="abc12def34"
# num=""
# for i in s:
#     if i.isdigit():
#         num+=i
#     else:
#         if num:
#             print(num)
#             num=""
# if num:
#     print(num)
'''Sum All Numbers
Input: abc12def45
Output: 57'''
# s="abc12def45"
# num=""
# total=0
# for i in s:
#     if i.isdigit():
#         num+=i
#     else:
#         if num:
            
#             total+=int(num)
#         num=""
# if num:
#     total+=int(num)
# print(total)
'''Find Largest Number in String
Input: abc12def45xyz9
Output: 45'''
# s="abc12def45xyz9"
# num=""
# long=0
# for i in s:
#     if i.isdigit():
#         num+=i
#     else:
#         if num:
#             long=max(long,int(num))
#         num=""
# if num:
#     long=max(long,int(num))
# print(long)



'''find the missing charecter'''
# s="abcfghijklmnopqrstuvwxyz"
# for i in "abcdefghijklmnopqrstuvwxyz":
#     if i not in s:
#         print(i) 
'''Find Extra Character
Input:
String 1: abcde
String 2: abxcde'''
# s1="abcd"
# s2="abcde"
# for i in s2:
#     if i not in s1:
#         print(i)
'''if two string are equla without using =='''
s="ramya"
s1="ramya"
if s is s1:
    print("true")
else:
    print("false")



