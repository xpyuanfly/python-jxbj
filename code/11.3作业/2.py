import random as rd
import math

def isInSection(point):
    if point[1] <= math.sin(point[0]):
        return True
    else:
        return False  

if __name__ == "__main__":
    n = 10000  
    ls = [[rd.uniform(0, math.pi), rd.uniform(0, 1)] for _ in range(0, n)]
    res = list(map(isInSection,ls))
    bieli = sum(res)/len(res)
    computedvalue = math.pi*1 *bieli
    #print(res)
    print(computedvalue)

    # -cos pi + C -(-cos 0 + C )
    truevalue = -math.cos(math.pi)+ math.cos(0)
    print(truevalue)