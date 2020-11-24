# Q2二分搜索：
# 程序员必备的分治法经典例子，无论什么场合，都要非常熟练地写出。比如在list中查找元素x，请写出该函数defbinarysearch(x)，思路是每次在列表的中间查找，如果相等则返回，如果小于目标，则查找左边的部分，如果大于目标，则查找右边的部分。

def binarysearch(x,ls,low,up):
    if low > up:
        return -1

    if low == up and ls[low] ==x:
        return low
   
    mid = (up+low)//2
    if ls[mid] == x:
        return mid
    else:
        res = binarysearch(x,ls,low,mid-1)
        if res != -1:
            return res
        else:
            res = binarysearch(x,ls,mid+1,up)
            if res !=-1:
                return res
        return -1


if __name__ == "__main__":
    ls = [5, 3, 42, 13, 45, 67, 32, 13, 45, 67, 34, 656]
    ls = sorted(ls)  # [3,5,13,13,32,34,42,45,45,67,67,656]
    print(ls)
    x = 13
    print("search：{}".format(x))
    res = binarysearch(x,ls,0,len(ls)-1)
    print("res:ls[{}]:{}".format(res,ls[res]))