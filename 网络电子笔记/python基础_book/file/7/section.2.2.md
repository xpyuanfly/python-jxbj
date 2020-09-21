# 异常的传递

## 1. try嵌套中

```python
	
import time
try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print('关闭文件')
except:
    print("没有这个文件")
```

运行结果:

```python
In [26]: import time
    ...: try:
    ...:     f = open('test.txt')
    ...:     try:
    ...:         while True:
    ...:             content = f.readline()
    ...:             if len(content) == 0:
    ...:                 break
    ...:             time.sleep(2)
    ...:             print(content)
    ...:     finally:
    ...:         f.close()
    ...:         print('关闭文件')
    ...: except:
    ...:     print("没有这个文件")
    ...: finally:
    ...:     print("最后的finally")
    ...:     
xxxxxxx--->这是test.txt文件中读取到信息
^C关闭文件
没有这个文件
最后的finally


```

## 2. 函数嵌套调用中

```python
	def test1():
		print("----test1-1----")
		print(num)
		print("----test1-2----")


	def test2():
		print("----test2-1----")
		test1()
		print("----test2-2----")


	def test3():
		try:
			print("----test3-1----")
			test1()
			print("----test3-2----")
		except Exception as result:
			print("捕获到了异常，信息是:%s"%result)

		print("----test3-2----")



	test3()
	print("------华丽的分割线-----")
	test2()
```

运行结果:

![](../Images/Snip20170102_9.png)

总结：
* 如果try嵌套，那么如果里面的try没有捕获到这个异常，那么外面的try会接收到这个异常，然后进行处理，如果外边的try依然没有捕获到，那么再进行传递。。。
* 如果一个异常是在一个函数中产生的，例如函数A---->函数B---->函数C,而异常是在函数C中产生的，那么如果函数C中没有对这个异常进行处理，那么这个异常会传递到函数B中，如果函数B有异常处理那么就会按照函数B的处理方式进行执行；如果函数B也没有异常处理，那么这个异常会继续传递，以此类推。。。如果所有的函数都没有处理，那么此时就会进行异常的默认处理，即通常见到的那样
* 注意观察上图中，当调用test3函数时，在test1函数内部产生了异常，此异常被传递到test3函数中完成了异常处理，而当异常处理完后，并没有返回到函数test1中进行执行，而是在函数test3中继续执行