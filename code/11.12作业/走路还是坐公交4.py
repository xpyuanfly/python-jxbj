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
'''优化：将之前抵达过的位置存储一下'''

class node:
    def __init__(self, n, cost):
        self.n = n
        self.parent=None
        self.cost = cost

    def search(self, goal):
        if self.n == goal:
            return True
        else:
            return False

    def generate_child_node(self):
        self.left = node(self.n-1, self.cost+3)
        self.mid = node(self.n*2 , self.cost+2)
        self.right = node(self.n+1, self.cost+3)

        self.left.parent = self
        self.mid.parent = self
        self.right.parent = self

        self.childs = [self.left, self.mid, self.right]

    # def searchchild(self, goal):
    #     return self.left.search(goal) or self.mid.search(goal) or self.right.search(goal)


def search_nodes(node_ls, goal):
    res = False
    print("该层:",end="")
    for x in node_ls:
        print(x.n,end=",")
        if x.search(goal):            
            print()
            return x
    print()
    return res


if __name__ == "__main__":
    n, k = 5, 17
    min = 0
    
    if n > k:
        min += (n-k)
    else:
        print("开始搜索：{}->{}".format(n, k))
        root = node(n,0)
        print("根节点是:{}".format(root.n))

        if root.search(k):
            min += 1
        else:
            root.generate_child_node()
            ls_node = root.childs

            while True:
                res_node = search_nodes(ls_node, k) 
                min += 1
                if bool(res_node):
                    break
                tmp_ls_node = []
                for x in ls_node:
                    x.generate_child_node()
                    tmp_ls_node.extend(x.childs)
                ls_node = tmp_ls_node
           
    print("用时为：{}".format(min))
    print("显示搜索路径：")
    res_path =[]
    while res_node.parent != None :
        res_path.append(str(res_node.n))
        res_node = res_node.parent
    print('->'.join( res_path[::-1] ))
