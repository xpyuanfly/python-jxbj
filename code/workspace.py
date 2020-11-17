# 你的班级有10个学生的成绩，你希望给出top k个成绩
# 例如输入ls=[5,1,42,12,34,52,77,88,13,23]
# 如果k=5，那么求出最高的5个成绩，要求不能使用sorted()函数,提示：冒泡排序法是个时间复杂度很高的算法，请尽量使用分治法的思想，实现快速排序算法。

ls = [5, 1, 42, 12, 34, 52, 77, 88, 13, 23]
def partition(ls, low, up):
    pivot = ls[up]
    i = low-1
    for j in range(low, up):
        if ls[j] > pivot:
            i += 1
            #[42, 34, 52, 77, 88, 23, 12, 1, 13, 5]
            ls[i], ls[j] = ls[j], ls[i]
    ls[i+1], ls[up] = ls[up], ls[i+1]
    return i+1


def quicksort(ls, low, up):
    # if len(ls) <= 1:
    #     return ls
    if low< up:
        i = partition(ls, low, up)
        quicksort(ls, low, i-1)
        quicksort(ls, i+1, up)


quicksort(ls, 0, len(ls)-1)
print(ls)