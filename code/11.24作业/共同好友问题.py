'''
假设A有好友B,D,C；B有好友D,E,A,C；C有好友A,B,D,E；D有好友A,C,B,E;E有好友B,C,D。
A:B,D,C
B:D,E,A,C,
C:A,B,D,E
D:A,C,B,E
E:B,C,D
'''

if __name__ == "__main__":
    fo = open(
        'C:\\Users\\yxp\\Desktop\\PYTHON\\python-jxbj\\code\\11.24作业\\friends_input.txt', "rb")
    input_ls = fo.readlines()
    input_ls = list(map(lambda x: str(x, encoding='utf-8').replace("\r\n",""), input_ls))

    friend_dic = {}
    for item in input_ls:
        item_ls = item.split(":")
        common = item_ls[0]
        friends_ls = item_ls[1].split(",")
        friends_ls = sorted(friends_ls)
        for i in range(len(friends_ls)):
            for j in range(i+1,len(friends_ls)):
                key = "{}-{}".format(friends_ls[i],friends_ls[j])
                if key in friend_dic:
                    friend_dic[key].append(common)
                else:
                    friend_dic[key] = [common]
    for key,value in friend_dic.items():
        print("{},{},{}".format(key,len(value),value))
        
    # print(friend_dic)