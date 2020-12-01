# Python3 函数

函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。

------

## 定义一个函数

你可以定义一个由自己想要功能的函数，以下是简单的规则：

- 函数代码块以 **def** 关键词开头，后接函数标识符名称和圆括号 **()**。
- 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
- 函数内容以冒号 : 起始，并且缩进。
- **return [表达式]** 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。

![img](https://www.runoob.com/wp-content/uploads/2014/05/py-tup-10-26-1.png)

------

Python 定义函数使用 def 关键字，一般格式如下：

```
def 函数名（参数列表）:
    函数体
```

默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。

让我们使用函数来输出"Hello World！"：

```
def hello() :
   print("Hello World!")
hello()
```

 更复杂点的应用，函数中带上参数变量:
```
def max(a, b):
    if a > b:        
    	return a   
    else:        
    	return b  
a = 4 b = 5 
print(max(a, b))
```
以上实例输出结果：

```
5
```

定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。

这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。



在 python 中，变量是没有类型的：

```
a=[1,2,3]
a="Runoob"
```

以上代码中，**[1,2,3]** 是 List 类型，**"Runoob"** 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。

## 可更改(mutable)与不可更改(immutable)对象

在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

- **不可变类型：**变量赋值 **a=5** 后再赋值 **a=10**，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
- **可变类型：**变量赋值 **la=[1,2,3,4]** 后再赋值 **la[2]=5** 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

- **不可变类型：**类似 C++ 的值传递，如 整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a)）内部修改 a 的值，则是新生成来一个 a。
- **可变类型：**类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

### python 传不可变对象实例

通过 **id()** 函数来查看内存地址变化：

```
def change(a):
    print(id(a))   # 指向的是同一个对象
    a=10
    print(id(a))   # 一个新对象
 
a=1
print(id(a))
change(a)
id(a)
```
以上实例输出结果为：

```
140730715027232
140730715027232
140730715027520
140730715027232
```

可以看见在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），在函数内部修改形参后，形参指向的是不同的 id。

### 传可变对象实例

可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：

```
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30]
print ("函数外取值: ", mylist)
changeme( mylist )
print ("函数外取值: ", mylist)
```

传入函数的和在末尾添加新内容的对象用的是同一个引用。故输出结果如下：

```
函数外取值:  [10, 20, 30]
函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
函数外取值:  [10, 20, 30, [1, 2, 3, 4]]
```

------

## 参数

以下是调用函数时可使用的正式参数类型：

- 必需参数
- 关键字参数
- 默认参数
- 不定长参数

### 必需参数

必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

调用 printme() 函数，你必须传入一个参数，不然会出现语法错误：

```
def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return
 
# 调用 printme 函数，不加参数会报错
printme()

以上实例输出结果：
Traceback (most recent call last):
  File "test.py", line 10, in <module>
    printme()
TypeError: printme() missing 1 required positional argument: 'str'
```

### 关键字参数

关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

以下实例在函数 printme() 调用时使用参数名：

```
def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return
 
#调用printme函数
printme( str = "12345")
```

以下实例中演示了函数参数的使用不需要使用指定顺序：

```
def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )
```

### 默认参数

调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：

```
#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="11" )
print ("------------------------")
printinfo( name="22" )
```

### 不定长参数

你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：

```
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。

```
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )
```

如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：

```
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )
```

还有一种就是参数带两个星号 **基本语法如下：

```
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

加了两个星号 ** 的参数会以字典的形式导入。

```
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)
```

声明函数时，参数中星号 * 可以单独出现，例如:

```
def f(a,b,*,c):
    return a+b+c
```

如果单独出现星号 * 后的参数必须用关键字传入。

```
>>> def f(a,b,*,c):
...     return a+b+c
... 
>>> f(1,2,3)   # 报错
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes 2 positional arguments but 3 were given
>>> f(1,2,c=3) # 正常
6
>>>
```

------

## 匿名函数

python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

- lambda 只是一个表达式，函数体比 def 简单很多。
- lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
- lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
- 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

### 语法

lambda 函数的语法只包含一个语句，如下：

```
lambda [arg1 [,arg2,.....argn]]:expression
```

```
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))
```

------

## return语句

**return [表达式]** 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。之前的例子都没有示范如何返回数值，以下实例演示了 return 语句的用法：

```
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total
 
# 调用sum函数
total = sum( 10, 20 )
print ("函数外 : ", total)
```

------

##      			 	        典型案例    

1. 默认参数必须放在最后面，否则会报：

     ```
SyntaxError: non-default argument follows default argument
    ```

    ```
# 可写函数说明
   def printinfo( age=35,name):   # 默认参数不在最后，会报错
    "打印任何传入的字符串"
       print("名字: ", name)
       print("年龄: ", age)
       return
```
   
   
   
2. **def(\**kwargs)** 把N个关键字参数转化为字典:

     ```
>>> def func(country,province,**kwargs):
    ...     print(country,province,kwargs)
... 
    >>> func("China","Sichuan",city = "Chengdu", section = "JingJiang")
China Sichuan {'city': 'Chengdu', 'section': 'JingJiang'}
    >>> 
```
   

   
3. lambda 匿名函数也是可以使用"**关键字参数**"进行参数传递

   ```
   >>> g= lambda x,y : x**2+y**2
   >>> g(2,3)
   13
   >>> g(y=3,x=2)
   13
   ```

   同样地，lambda 匿名函数也可以设定默认值

   ```
   >>> g= lambda x=0,y=0 : x**2+y**2
   >>> g(2,3)
   13
   >>> g(2)
   4
   >>> g(y=3)
   9
   ```

   **注意：**如果只打算给其中一部分参数设定默认值，那么应当将其放在靠后的位置（和定义函数时一样，避免歧义），否则会报错。

4. 对于变量作用域，变量的访问以 **L（Local） –> E（Enclosing） –> G（Global） –>B（Built-in）** 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。

   观察以下几个例子，均从内部函数输出变量 x：

   **1. 局部作用域**

   ```
   x = int(3.3)
   
   x = 0
   def outer():
       x = 1
       def inner():
           x = 2
           print(x)
       inner()
   
   outer()
   ```

   执行结果为 2，因为此时直接在函数 inner 内部找到了变量 x。

   **2.闭包函数外的函数中**

   ```
   x = int(3.3)
   
   x = 0
   def outer():
       x = 1
       def inner():
           i = 2
           print(x)
       inner()
   
   outer()
   ```

   执行结果为 1，因为在内部函数 inner 中找不到变量 x，继续去局部外的局部——函数 outer 中找，这时找到了，输出 1。

   **3.全局作用域**

   ```
   x = int(3.3)
   x = 0
   def outer():
       o = 1
       def inner():
           i = 2
           print(x)
       inner()
   outer()
   ```

   执行结果为 0，在局部（inner函数）、局部的局部（outer函数）都没找到变量 x，于是访问全局变量，此时找到了并输出。

5. **函数内可以访问全局变量，但不能更新(修改)其值！**

   ```
   a = 10
   def sum ( n ) :
      n += a
      print ('a = ', a, end = ' , ' )
      print ( 'n = ', n )
     
   sum(3)
   ```

   输出 :

   ```
   a =  10 , n =  13
   ```

   如果引用了还没更新的值则会报错 :

   ```
   a = 10
   def sum ( n ) :
      n += a
      a = 11
      print ('a = ', a, end = ' , ' )
      print ( 'n = ', n )
     
   sum(3)
   ```

   输出 :

   ...

   ```
   UnboundLocalError: local variable 'a' referenced before assignment
   ```

   可以加上 global 引用以更新变量值 :

   ```
   a = 10
   def sum ( n ) :
      global a
      n += a
      a = 11
      print ('a = ', a, end = ' , ' )
      print ( 'n = ', n )
   
   sum ( 3 )
   print ( '外 a = ', a )
   ```

   输出:

   a =  11 , n =  13 外 a = 11

   

6. 函数也可以以一个函数为其参数:

   ```
   def hello () :
     print ("Hello, world!")
   
   def execute(f):
     "执行一个没有参数的函数"
     f()
   
   execute(hello)
   ```

   输出：

   ```
   Hello, world!
   ```

   

7. 可以通过 函数名.__doc__ 的方式来显示函数的说明文档，感觉这个如果在阅读比较大的程序时应该会有用，同时也在提示自己在写函数时注意添加文档说明。

   ```
   def add(a,b):
       "这是 add 函数文档"
       return a+b
   
   print (add.__doc__)
   ```

   输出结果为：

   ```
   这是 add 函数文档
   ```

   

8. 函数返回值的注意事项: 不同于 C 语言，Python 函数可以返回多个值，多个值以元组的方式返回:

   ```
   def fun(a,b):    
       "返回多个值，结果以元组形式表示"
       return a,b,a+b
   print(fun(1,2))
   ```

   输出结果为：

   ```
   (1, 2, 3)
   ```

   

9. **函数的装饰器**

     在不改变当前函数的情况下, 给其增加新的功能:

     ```
     def log(pr):#将被装饰函数传入
         def wrapper():
             print("**********")      
             return pr()#执行被装饰的函数
         return wrapper#将装饰完之后的函数返回（返回的是函数名）
     @log
     def pr():
         print("我是小小洋")
     
     pr()
     ```

     回调函数和返回函数的实例就是装饰器。

     

10.  在编写函数的过程中，可以显式指定函数的参数类型及返回值类型：

     ```
     def function_demo(param_A: int, param_B: float, param_C: list, param_D: tuple) -> dict:
         pass
     ```

     这种 **“将数据类型写死在代码中”** 的行为在集成开发环境/代码编辑器时尤为方便，通过显式地指定函数的参数类型和返回值，能够让智能补全组件提前获知标识符的数据类型，提供有利的辅助开发功能。

     