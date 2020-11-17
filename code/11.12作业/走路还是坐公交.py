'''
你收到通知被农商银行录取了，高兴的来到了株洲，很快你就来到了天台路上，已知你的位置是N，农商银行的位置是K。为了去农商银行，你有两种移动方式：走路或者坐公交。
走路：你可以从位置X移动到X+1或者X-1
搭公交车：你可以从位置X移动到2X
每次走路或者搭公交车所需要的时间都是1分钟，你想尽快到达农商银行，所需的时间是多少呢？

样例输入
5 17
样例输出
4
'''
'''该实例是贪心方法，但是确实是错误的，计算的答案是错误的'''

def walk(n, k):
    if n < k:
        n += 1
    else:
        n -= 1
    return n


def bus(n):
    return n*2

min = 0

if __name__ == "__main__":
    n, k = 5, 17
    
    if n > k:
        min += (k-n)
    while n != k:
        if n*2 == k:
            min += 1
        elif abs(n*2 - k) < abs(n-k):
            n = bus(n)
            min += 1
        else:
            n = walk(n, k)
            min += 1

    print(min)
