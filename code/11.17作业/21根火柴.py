# 现有21根火柴,两人轮流取,每人每次可取走1- 4根,不可多取,也不能不取,谁取最后一根谁输
# 现在由你设计机器人的程序，在人先取的情况下，保证机器人必胜。

if __name__ == "__main__":

    n = 21
    while n!=0:
        p = int(input('你：'))
        while p > 4 or p < 1 or n-p < 0:
            print('error, input again:')
            p = int(input('你：'))
        n -= p
        if n == 0:
            print('pc win')
            break
        
        c = 5-p
        print('机：{}'.format(c))
        n -= c
        if n == 0:
            print('你 win')
            break
        print('剩余：{}'.format(n))
