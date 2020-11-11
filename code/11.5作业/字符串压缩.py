'''
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）
示例1:
输入："aabcccccaaa"
输出："a2b1c5a3"
示例2:
输入："abbccd"
输出："abbccd"
解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。

'''
# input ：2个示例
# input = 'aabcccccaaa'
input = 'abbccda'

input_ls = list(input)

print(input_ls)
output_ls = []
for i in range(0, len(input)):
    if len(output_ls) == 0:
        output_ls.append([input[i], 1])
    else:
        if output_ls[-1][0] == input[i]:
            output_ls[-1][1] += 1
        else:
            output_ls.append([input[i], 1])
print(output_ls)
ls_map_out = list(
    map(lambda x: x[0]+(str(x[1]) if x[1]>=1 else ''), output_ls))
print(ls_map_out)
print(
    ''.join(ls_map_out) if len(ls_map_out) < len(input) else input
)
