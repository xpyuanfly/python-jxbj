import time

for i in range(101):
    time.sleep(0.1)
    # 转义字符\r表示将行首，end=''表示输出不换行
    #print('\r{:2}%'.format(i), end='')
    print('\r{:=^10}%'.format(i), end='')
