#1
a=int(0b11111100100)
b=int(0x7e3)
c=int(0o3742)
d=2021
print(a,b,c,d)
#最大为d,最小为c
#2
print(int(0b1011001))
print(hex(0o7463))
print(int(0xf7ac))
print(oct(2020))
#89,0xf33,63404,0o3744
#3
ls=list()
x=int(input('请输入需要求和的多项式n的值：（请输入正整数）'))
for i in range(1,x+1):
    if i%2==1:#判断符号位
        i=1/i
    elif i%2==0:#判断符号位
        i=-1/i
    ls.append(i)#放入求和容器
su=sum(ls)
print(su)
#4
#定义判断函数，利用filter放入容器再切片求和
def isss(x):
    a=0
    for i in range(2,x):
        if x%i==0:
            a+=1
        else:
            a+=0
    if a==0:
        return True
ls=list(range(2,1000))
lz=list(filter(isss,ls))#返回素数列表
su=sum(lz[0:50])#对前50个素数进行求和
print(su)
#设置两层循环，第一层进行累加，第二层进行寻找
ls=list()#容器
a=0#标志
for i in range (2,1000):#第一层做找数累加
    o=2 #每次新循环对变量o进行重置
    for o in range(2,i):#第二层判断素数
        if i%o==0:
            break#找到因数后，此数非素数，退出第二层循环，开始遍历第一层循环
    else:#当第二层循环中未执行break，即此数为素数，开始执行第一层循环中的else模块
        ls.append(i)
        a+=1
    if a==50:#判断是否已累加50个素数
        break#累加到第50个素数后退出第一层循环
su=sum(ls)
print(su)
#5
def amstl(x):
    n=len(str(x))
    if int(x/100%10)**n+int(x/10%10)**n+int(x%10)**n==int(x):
        return True
    else:
        return False

ls=list(range(0,1001))
a=list(filter(amstl,ls))
print(a)


