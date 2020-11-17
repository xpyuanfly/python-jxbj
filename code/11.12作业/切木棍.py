'''
你有一根长度为n的木棍(n是整数)，现在需要你用这个木棍做一个矩形（但是不能是正方形），矩形的每条边的长度为整数。你可以将这个木棍切成四份，作为矩形的四条边，请问你组成多少种不同的矩形？
输入
对于每组数据，输入一个整数，即为木棍的长度n（1<=n<=105）
输出
对于每组数据，输出一个整数，表示能组成的矩形种数。
样例输入
6
20
样例输出
1
4
'''
import math

def cutnumber(n):
    if n<6 or n%2 ==1:
        return 0
    else:
        count=0
        harf = n//2
        for _ in range(1, math.ceil(harf/2)):
            count+=1
        return count

if __name__ == "__main__":
    n = int(input("请输入长度："))
    print(cutnumber(n))