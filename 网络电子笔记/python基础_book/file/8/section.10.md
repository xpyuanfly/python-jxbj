# 高阶函数

* 函数的参数是一个函数类型那么我们称为这样的函数为高阶函数
* 函数的返回值是一个函数类型那么这样的函数也可以称为是高阶函数

**示例代码:**

```py
def calc_num(new_func):
    a = 1
    b = 2

    # 执行外界传入过来的函数
    result = new_func(a, b)

    return result


def sum_num(num1, num2):
    return num1 + num2


# 调用函数
result = calc_num(sum_num)
print(result)


def show():

    # 在python里面可以函数里面在定义一个函数
    def print_info():
        print("哈哈， 我是一个子函数")

    # 函数的返回值是一个函数类型
    return print_info

new_func = show()

print(new_func, type(new_func))

# 调用返回的函数
new_func()
```

## 1. reduce 用法

**reduce\(\)**  根据函数对容器类型中每一个数据进行计算.

* 第一个参数功能函数，函数需要带有两个参数
* 第二个参数是要操作的容器类型


**计算列表中的累加和:**

```python
import functools

my_list = [1, 2, 3, 4, 5]


def f(x1, x2):
    return x1 + x2


result = functools.reduce(f, my_list)
print(result)
```

输出结果:

```python
15
```

## 2. filter 用法

**filter\(\)** 根据函数对容器类型中数据进行过滤, 返回一个 filter 对象, 如果要转换为列表, 可以使用 list\(\) 来转换.

* 第一个参数带有过滤功能的函数
* 第二个参数是要操作的容器类型


**过滤列表中的偶数:**

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def f(x):
    return x % 2 == 0


result = filter(f, my_list)
print(list(result))
```

输出结果:

```python
[2, 4, 6, 8, 10]
```

**过滤列表中首字母为大写的单词:**

```python
my_list = ['edward', 'Smith', 'Obama', 'john', 'tom']


def f(x):
    return x[0].isupper()


result = filter(f, my_list)
print(list(result))
```

输出结果:

```pythjon
['Smith', 'Obama']
```



