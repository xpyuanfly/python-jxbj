'''
你的班级有10个学生的成绩，你希望给出top k个成绩
例如输入ls=[5,1,42,12,34,52,77,88,13,23]
如果k=5，那么求出最高的5个成绩，要求不能使用sorted()函数,提示：冒泡排序法是个时间复杂度很高的算法，请尽量使用分治法的思想，实现快速排序算法。
'''
arr = [5, 1, 42, 12, 34, 52, 77, 88, 13, 23]
 
def partition(arr, low, high):
    i = (low-1)         # 最小元素索引
    pivot = arr[high]

    for j in range(low, high):

        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    if low < high:

        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


if __name__ == "__main__":
    k = 5
    quickSort(arr, 0, len(arr)-1)
    print(arr)
