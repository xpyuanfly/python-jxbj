'''
你的班级有10个学生的成绩，你希望给出top k个成绩
例如输入ls=[5,1,42,12,34,52,77,88,13,23]
如果k=5，那么求出最高的5个成绩，要求不能使用sorted()函数,提示：冒泡排序法是个时间复杂度很高的算法，请尽量使用分治法的思想，实现快速排序算法。
'''

def quicksort(ls):
    if len(ls) <= 1:
        return ls
    pivot = ls[0]
    left = [item for item in ls[1:] if item >= pivot]
    mid = [pivot]
    right = [item for item in ls[1:] if item < pivot]
    return quicksort(left) + mid + quicksort(right)
    
if __name__ == "__main__":
    ls=[5,1,42,12,34,52,77,88,13,23]
    k=5
    print(quicksort(ls)[0:k])
