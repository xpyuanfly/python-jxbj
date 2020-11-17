# 有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

class pair_rabbit:
    def __init__(self):
        self.age = 1
        self.isMature = False

    def growup1month(self):
        self.age += 1
        self.isMature = True if self.age >= 3 else False

    def __repr__(self):
        return str(self.age)


def prn_obj(obj):
    print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))


if __name__ == "__main__":

    k = int(input("第几个月："))

    mature_ls = []
    small_ls = []
    first = pair_rabbit()
    small_ls.append(first)
    mature_num = len(mature_ls)
    small_num = len(small_ls)
    sum_ls = mature_num + small_num
    print("第{}月,sum:{} , mature pair rabbits:{}, small pair rabbits:{}, details:".format(
        1, sum_ls, mature_num, small_num))
    for small in small_ls:
        print(small, end=',')
    print()
    for month in range(2, k+1):
        tmp = []
        for mature in mature_ls:
            mature.growup1month()
            tmp.append(pair_rabbit())

        for small in small_ls:
            small.growup1month()
            if small.isMature:                
                tmp.append(pair_rabbit())
                mature_ls.append(small)                
            else:
                tmp.append(small)

        small_ls = tmp
        mature_num = len(mature_ls)
        small_num = len(small_ls)
        sum_ls = mature_num + small_num

        print("第{}月,sum:{} , mature pair rabbits:{}, small pair rabbits:{}, details:".format(
            month, sum_ls, mature_num, small_num))
        for small in small_ls:
            print('age:'+str(small), end=',')
        print()
