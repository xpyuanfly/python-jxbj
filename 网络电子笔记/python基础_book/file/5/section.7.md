# 模块

## 1. Python中的模块

有过C语言编程经验的朋友都知道在C语言中如果要引用`sqrt函数`，必须用语句`#include <math.h>`引入math.h这个头文件，否则是无法正常进行调用的。

那么在Python中，如果要引用一些其他的函数，该怎么处理呢？

在Python中有一个概念叫做模块（module），这个和C语言中的头文件以及Java中的包很类似，比如在Python中要调用`sqrt函数`，必须用import关键字引入math这个模块，下面就来了解一下Python中的模块。

说的通俗点：模块就好比是工具包，要想使用这个工具包中的工具\(就好比函数\)，就需要导入这个模块

## 2. import

在Python中用关键字`import`来引入某个模块，比如要引用模块math，就可以在文件最开始的地方用import math来引入。

形如:

```python
    import module1,mudule2...
```

当解释器遇到import语句，如果模块在当前的搜索路径就会被导入。

在调用math模块中的函数时，必须这样引用：

```python
　　模块名.函数名
```

* 想一想:

  > 为什么必须加上模块名调用呢？

* 答:

  > 因为可能存在这样一种情况：在多个模块中含有相同名称的函数，此时如果只是通过函数名来调用，解释器无法知道到底要调用哪个函数。所以如果像上述这样引入模块的时候，调用函数必须加上模块名

```python
    import math

    #这样会报错
    print sqrt(2)

    #这样才能正确输出结果
    print math.sqrt(2)
```

有时候我们只需要用到模块中的某个函数，只需要引入该函数即可，此时可以用下面方法实现：

```python
    from 模块名 import 函数名1,函数名2....
```

不仅可以引入函数，还可以引入一些全局变量、类等

* 注意:

  > * 通过这种方式引入的时候，调用函数时只能给出函数名，不能给出模块名，但是当两个模块中含有相同名称函数的时候，后面一次引入会覆盖前一次引入。也就是说假如模块A中有函数function\( \)，在模块B中也有函数function\( \)，如果引入A中的function在先、B中的function在后，那么当调用function函数的时候，是去执行模块B中的function函数。
  >
  > * 如果想一次性引入math中所有的东西，还可以通过from math import \*来实现

## 3. from…import

Python的from语句让你从模块中导入一个指定的部分到当前命名空间中

语法如下：

```python
    from modname import name1[, name2[, ... nameN]]
```

例如，要导入模块fib的fibonacci函数，使用如下语句：

```python
    from fib import fibonacci
```

### 注意

* 不会把整个fib模块导入到当前的命名空间中，它只会将fib里的fibonacci单个引入

## 4. from … import \*

把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：

```python
    from modname import *
```

### 注意

* 这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。

## 5. as

```python
    In [1]: import time as tt

    In [2]: time.sleep(1)
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-2-07a34f5b1e42> in <module>()
    ----> 1 time.sleep(1)

    NameError: name 'time' is not defined

    In [3]: 

    In [3]: 

    In [3]: tt.sleep(1)

    In [4]: 

    In [4]: 

    In [4]: from time import sleep as sp

    In [5]: sleep(1)
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-5-82e5c2913b44> in <module>()
    ----> 1 sleep(1)

    NameError: name 'sleep' is not defined

    In [6]: 

    In [6]: 

    In [6]: sp(1)

    In [7]:
```

## 6. 定位模块

当你导入一个模块，Python解析器对模块位置的搜索顺序是：

1. 当前目录
2. 如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。
3. 如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
4. 模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。



