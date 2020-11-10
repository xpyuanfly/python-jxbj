''''
字符串最长公共子串问题：获取实现两个字符串中最大的公共子串，比如str1 = "xyabcdefui"，str2 = "efdrabcdefghdef"，找到结果：公共字串"abcdef"
'''
'''解题思路：构建 len(str1) * len(str2)的表格
  x y a b c d e f u i
e 0 0 0 0 0 0 1 0 0 0
f 0 0 0 0 0 0 0 1 0 0
d 0 0 0 0 0 1 0 0 0 0
r 0 0 0 0 0 0 0 0 0 0
a 0 0 1 0 0 0 0 0 0 0
b 0 0 0 1 0 0 0 0 0 0
c 0 0 0 0 1 0 0 0 0 0
d 0 0 0 0 0 1 0 0 0 0
e 0 0 0 0 0 0 1 0 0 0
f 0 0 0 0 0 0 0 1 0 0
g 0 0 0 0 0 0 0 0 0 0
h 0 0 0 0 0 0 0 0 0 0
d 0 0 0 0 0 1 0 0 0 0
e 0 0 0 0 0 0 1 0 0 0
f 0 0 0 0 0 0 0 1 0 0
'''
str1 = "xyabcdefui"
str2 = "efxrabcdefghdef"
ls1 = list(str1)
ls2 = list(str2)
#构建matrix
matrix = []
for i in ls2 :
    tmp = []
    for j in ls1 :
        tmp.append(1 if i==j else 0)
    matrix.append(tmp) 

#打印matrix
for _ in matrix:
    print(_)

rownum=len(matrix)
colnum = len(matrix[0])

#从下往上扫描
diagonal_line=[]
rowindex = rownum-1
while rowindex >= 0:
    diagonal_line.append([])
    i = rowindex
    j = 0
    while j < colnum and i<rownum:
        diagonal_line[-1].append( ls1[j] if matrix[i][j] ==1 else '0')
        j+=1
        i+=1
    rowindex-=1

#从左往右扫
colindex = 1
while colindex < colnum:
    diagonal_line.append([])
    i = 0
    j = colindex
    while j < colnum and i<rownum:
        diagonal_line[-1].append( ls1[j] if matrix[i][j] ==1 else '0')
        j+=1
        i+=1
    colindex+=1

#打印diagonal_line
for _ in diagonal_line:
    print(_)

str_diagonal_line = []
#处理对角线
print('处理对角线:')
for x in diagonal_line:
    str_diagonal_line.append(''.join(x))

for _ in str_diagonal_line:
    print(_)

print('清理全为0的:')
str_diagonal_line = list(filter(lambda x: x.count('0') != len(x),str_diagonal_line))

for _ in str_diagonal_line:
    print(_)

print('过滤两头为0的:')
str_diagonal_line = list(map(lambda x: x.strip('0'),str_diagonal_line))

for _ in str_diagonal_line:
    print(_)

print('过滤中间为0的:')
def filter_0(string):
    return list(filter(lambda x:False if x=='' else True, string.split('0')) ) 

result = []
for string in str_diagonal_line:
    result.append(filter_0(string))

#扁平化
result = sum(result,[])
for _ in result:
    print(_)

print('最大公共子串为：')
print( max(result, key=len, default='') )