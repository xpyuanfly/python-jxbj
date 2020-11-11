'''
Q2: 给定几个字符串，输入一个字符，如果第一个字符相同，再输入第二个，同样情况，继续输入，直到找到唯一的字符串。
示例1:
输入：ls=["flower","flow","flight"]
输入：f
输出："flower","flow","flight"
接着输入：fl
输出："flower","flow","flight"
接着输入：flo
输出："flower","flow"
接着输入：flow
输出："flower","flow"
接着输入：flowe
输出："flower"
'''
import re
ls=["flower","flow","flight"]
while 1==1:
    input_str = input("输入:")
    parttern = re.compile(input_str)
    #print(list(map(parttern.search,ls)))
    for string in ls:
        res = parttern.search(string)
        if res :
            print('\"'+string+'\"',sep='',end=',')
    print()