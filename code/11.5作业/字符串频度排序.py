'''
给定一个字符串，根据字符出现的频度排序，例如"abcc"，排序后的结果为"ccba"或者"ccab"
'''
string = "abcc"

dic={}
# for char in string:
#     # if char in dic.keys():
#     #     dic[char] +=1
#     # else:
#     #     dic[char] = 1
#     #:优化：
#     dic[char]= (dic[char] + 1) if (char in dic) else (1)

#方法2：
# for i in set(string):
#     dic[i]=string.count(i) #dic的添加
#     print(i,string.count(i))

#方法3：
dic={i:string.count(i) for i in string}

    
print(dic)
ls_tup = sorted(dic.items(),key=lambda x: x[1],reverse=True)
print(ls_tup)

print("".join(map(lambda x:x[0]*x[1],ls_tup)))
