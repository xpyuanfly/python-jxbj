import random as rd

def one_arg(func):
    def wrapper(mix_args):
        return func(mix_args[0],mix_args[1],mix_args[2])

    return wrapper

@one_arg
def isInCircle(point, R1=1, R2=10):
    if R1**2<= point[0]**2+point[1]**2 <= R2**2:
        return True
    else:
        return False
        
#isInCircle = one_arg(isInCircle)
if __name__ == "__main__":
    n = 100000
    R1=0
    R2=1
    ls = [[[rd.uniform(0, 10), rd.uniform(0, 10)],R1,R2] for _ in range(0, n)]
    #
    res = list(map(isInCircle,ls))
    mzl = sum(res)/len(res)
    #print(res)
    print(mzl)