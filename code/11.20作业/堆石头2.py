ls = [45, 13, 12, 16, 9, 5, 22]

res = 0 
while len(ls)>1:
    min = 5000000
    min_i = 0
    for i in range(len(ls)-1):
        temp = ls[i]+ls[i+1] #45+13
        if temp <min:
            min =temp
            min_i = i

    ls[min_i] = min
    ls.pop(min_i+1)
    res += min
    print(ls)
    print(res)
