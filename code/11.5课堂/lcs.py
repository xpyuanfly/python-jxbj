def longSubStr(str1,str2):
    len1 = len(str1)
    len2 = len(str2)
    longest,start1,start2 = 0,0,0
    c = [[0 for i in range(len2+1)]for i in range(len1+1)]
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                c[i][j] = c[i-1][j-1]+1
            else:
                c[i][j] = 0
            if (longest < c[i][j]):
                longest = c[i][j]
                start1 = i-longest
                start2 = j-longest

    return str1[start1:start1+longest],start1,start2

print(longSubStr('34abc','123abc'))