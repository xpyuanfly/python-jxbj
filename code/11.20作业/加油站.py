'''
Q3加油站:
一辆汽车加满油后可行驶n公里。旅途中有若干加油站。设计一个有效算法,指出应在哪些加油站停靠加油,使沿途加油次数最少。请对于给定的n和k个加油站位置，计算最少加油次数。
输入:输入包含多组测试用例。
对于每一组数据，其第1行有2个正整数n（1≤n≤5000）和k（1≤k≤5000）。表示汽车加满油后可行驶n公里，且旅途中有k个加油站。接下来的1行中，有k+1个整数，表示第k个加油站与第k-1个加油站之间的距离。第0个加油站表示出发地，汽车已加满油。第k+1个加油站表示目的地。
输出:数据输出一行。如果所对应的输入数据数据可以到达，将计算的最少加油次数输出。如果无法到达目的地，则输出“NoSolution”。
样例输入
7 7
1 2 3 4 5 1 6 6 
样例输出
4
'''
fulloil = 7
n = fulloil
ls = [1, 2, 3, 4, 5, 1, 6, 6]
count = 0

def oiling():
    global n
    global count
    global fulloil
    n = fulloil
    count += 1

oiling_position = []

for i in range(len(ls)):
    if fulloil < ls[i]:
        print("到达不了，n:{}<ls[{}]:{}".format(n, i, ls[i]))
        break

    if n < ls[i]:
        oiling()
        oiling_position.append(i-1)
    n -= ls[i]

print("加油次数：{}".format(count))
print("加油站位置：{}".format(ls))
print("加油位置：{}".format(oiling_position))
