import sys

"""
import os
print(os.getcwd())
"""

# 模拟文章
docu_set={'d1':'i love shanghai',
          'd2':'i am from shanghai now i study in tongji university',
          'd3':'i am from lanzhou now i study in lanzhou university of science  and  technolgy',}
# 得到文章词向量集合
all_words=[]
for i in docu_set.values():
    cut=i.split()
    all_words.extend(cut)
    
set_all_words=set(all_words)
# print(set_all_words)

# 构建倒排索引
invert_index=dict()
for b in set_all_words:
    temp=[]
    for j in docu_set.keys():
        field=docu_set[j]
        split_field=field.split()
        
        if b in split_field:
            temp.append(j)
    invert_index[b]=temp

# 接收参数
if len(sys.argv) < 2:
    print("使用方法：python3 search.py [search_content] - return document")
    sys.exit()
search_content = sys.argv[1]
# 开始搜索
try:
    invert_index[search_content]         
    print(invert_index[search_content]) 
except KeyError:
    print("未查找到相关文件...")  
