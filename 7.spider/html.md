# Html 简易教程

 	HTML称为超文本标记语言Hyper Text Markup Language，是一种标识性的语言。它包括一系列标签．通过这些标签可以将网络上的文档格式统一，使分散的Internet资源连接为一个逻辑整体。HTML文本是由HTML命令组成的描述性文本，HTML命令可以说明文字，图形、动画、声音、表格、链接等。 [1] 
	超文本是一种组织信息的方式，它通过超级链接方法将文本中的文字、图表与其他信息媒体相关联。这些相互关联的信息媒体可能在同一文本中，也可能是其他文件，或是地理位置相距遥远的某台计算机上的文件。这种组织信息方式将分布在不同位置的信息资源用随机方式进行连接，为人们查找，检索信息提供方便。

## html文档结构

```
 1 <!DOCTYPE html> 
 2 <html lang="zh-CN">   #这个lang表示语言，zh-CN中文的意思，整个文档的内容以中文为主，如果以英文为主，就写成lang='en'
 3 
 4 <head> 
 5   <meta charset="UTF-8">
 6   <title>css样式优先级</title>
 7 </head>
 8 <body> 
 9 
10 </body>
11 </html>
```
1.<!doctype html>声明为html5文件，必须是html文档的第一行，在<html>标签之前;

2.<html>、</html>是文档开始和结束的标记,是HTML页面的根元素，在它们之间是文档的头部（head）和主体（body);

3.<head>、</head>定义HTML文档开头部分,内容不会在浏览器窗口显示,包含文档元（meta）数据，配置信息等，是给浏览器看的;

4.<title>、</title>定义了网页标题，在浏览器标题栏显示（修改一下title中的内容，然后看一下浏览器，你就会发现title是什么了）;

5.<body>、</body>之间的内容是可见的网页主体内容;

注意：中文网页需要使用 <meta charset="utf-8"> 声明编码，否则会出现乱码;有些浏览器是gbk，需手动设置为 <meta charset="gbk">；

##  html标签格式

1.html标签是由尖括号包围的关键字，如：<html>,<div>,<span>等;

2.html标签通常是成对出现，如：<div></div>,第一个是开始，第二个有斜线的是结束；

3.有些标签是单独呈现的，如：

<br/> <hr/>

4.标签里面带有若干属性，也有不带的；

标签语法：

<标签名 属性1=“属性值1” 属性2=“属性值2”……>内容部分</标签名>
<标签名 属性1=“属性值1” 属性2=“属性值2”…… />

html注释：

```
<!--注释内容--> #找到一行内容ctrl+/能快捷注释，注释的内容不会在网页上显示出来
```

## head内常用标签

### meta 标签

```
<meta>元素可提供有关页面的元信息（meta-information），针对搜索引擎和更新频度的描述和关键词。
<meta>标签位于文档的头部，不包含任何内容。
<meta>提供的信息是用户不可见的
```

#### http-equiv属性

​	相当于http的文件头作用，它可以向浏览器传回一些有用的信息，以帮助正确地显示网页内容，与之对应的属性值为content，content中的内容其实就是各个参数的变量值。

​	设置页面编码
```
<meta charset="UTF-8"> 
<meta http-equiv="content-type" content="text/html;charset=utf-8"> 刷新和调整
<meta http-equiv="Refresh" content="3">  # 每隔3秒自动刷新
<meta http-equiv="Refresh" content="3; Url=https://www.baidu.com">  # 每隔3秒自动跳转到百度
```
​	name属性: 主要用于描述网页，与之对应的属性值为content，content中的内容主要是便于搜索引擎机器人查找信息和分类信息用的。
　　关键字：搜索引擎搜索
```
<meta name="keywords" content="Html学习,meta学习,head学习">
　　描述：说明网站做什么的
<meta name="description" content="前端知识学习">
```
​	X-UA-Compatible
　　微软的IE6是通过XP、win2003等操作系统发布出来，作为占统治地位的桌面系统，也使得IE占据了统治地位，许多网站开发的时候，就按照IE6的标准去开发，而IE6自身的标准也是微软公司内部定义的。到了IE7出来的时候，采用了微软公司内部标准以及部分W3C的标准，这个时候许多网站升级到IE7的时候，就比较痛苦，很多代码调整后，才能够正常运行。而到了微软的IE8这个版本，基本上把微软内部自己定义的标准都抛弃了，而全面的支持W3C的标准，由于基于对标准彻底的变化了，使得原先在IE版本上能够访问的网站，在IE8中无法正常的访问，会出现一些排版的错误、文字重叠、显示不全等各种兼容性错误。
　　与任何早期浏览器版本相比，IE8对行业标准提供了更加紧密的支持。因此，针对旧版本的浏览器设计的站点可能不会按预期显示。为了帮助减轻任何问题，IE8 引入了文档兼容性的概念，从而允许您指定站点所有支持IE的版本。文档兼容性在IE8中添加新的模式，这些模式将告诉浏览器如何解释和呈现网站。如果您的站点在IE8中无法中无法正确的显示，则可以更新改站点以支持最新的WEB的标准(首选方式)，也可以强制IE8按照就版本的浏览器中查看站点方式来显示内容。通过使用meta 元素将X-UA-Compatible 标头添加到网页中，可以实现这一点。
　　当IE8 遇到未包含X-UA-Compatible 标头的网页时，它将使用指令来确定如何显示网页。如果该指令丢失或未指定基于标准的文档类型，则IE8将以IE5模式（Quicks模式）显示该网页。　

```
<meta http-equiv="X-UA-COMPATIBLE" content="IE=edge; IE=IE11; chrome=1">
```
#### Title标签
　　　网页头部标签　

```
<title>我是标题</title>
```

#### Link 标签
​	图标

```
<link rel="icon" href="http://www.jd.com/favicon.ico">
或
<link rel="icon" href="images/favicon.ico">
```
​	加载css样式文件
```
<head>
    <meta charset="UTF-8">
    <title>一起嗨起来</title>
    <!--<link rel="icon" href="http://www.jd.com/favicon.ico">-->
    <link rel="icon" href="images/favicon.ico">
    <link rel="stylesheet" type="text/css" href="css/common.css">
</head>
```

## body常用标签

### 基本标签

```
不加标签的纯文字也是可以在body中写的
<b>加粗</b>
<i>斜体</i>
<u>下划线</u>
<s>删除</s>

<p>段落标签</p> #独占一个段落

<h1>标题1</h1>
<h2>标题2</h2>
<h3>标题3</h3>
<h4>标题4</h4>
<h5>标题5</h5>
<h6>标题6</h6>

<!--换行-->
<br>
<!--水平线-->
<hr> #就是单独个一个水平线
```

### 常用特殊字符

![img](https://img2018.cnblogs.com/blog/1513655/201812/1513655-20181213230717655-327936300.png)

### div标签和span标签

这两个标签没有特别的样式,<div>xxxx</div>，<span>xxx</span>这是两个标签最大的特点，可以通过CSS来控制,网站中多数是他们;

div标签用来定义一个块级元素，并无实际的意义。主要通过CSS样式为其赋予不同的表现;

span标签用来定义内联(行内)元素，并无实际的意义。主要通过CSS样式为其赋予不同的表现;

块级元素与行内元素的区别：

块元素，是另起一行开始渲染的元素，行内元素则不需另起一行。单独在网页中插入这两个元素，不会对页面产生任何的影响；

这两个元素是专门为定义CSS样式而生的；

###  img标签 

```
<img src="图片的路径" alt="图片未加载成功时的提示" title="鼠标悬浮时提示信息" width="宽" height="高(宽高两个属性只用一个会自动等比缩放)">
```

src的路径分为两种：网上的图片路径和本地的图片路径(本地路径又包括相对路径和绝对路径)

```
"." -- 代表目前所在的目录，相对路径。 如：<a href="./abc">文本</a> 或 <img src="./abc" />
".." -- 代表上一层目录，相对路径。 如：<a href="../abc">文本</a> 或 <img src="../abc" />
"../../" -- 代表的是上一层目录的上一层目录，相对路径。 如：<img src="../../abc" />
"/" -- 代表根目录,绝对路径。 如：<a href="/abc">文本</a> 或 <img src="/abc" />
"D:/abc/" -- 代表根目录,绝对路径
```

![img](https://img2018.cnblogs.com/blog/1513655/201812/1513655-20181222100657475-1232279840.png)

![img](https://img2018.cnblogs.com/blog/1513655/201812/1513655-20181222100900346-1041321850.png)

### a标签 

 超链接标签:指从一个网页指向一个目标的连接关系，这个目标可以是另一个网页，也可以是相同网页上的不同位置，还可以是一个图片，一个电子邮件地址，一个文件，甚至是一个应用程序。

```
<a href="http://www.baidu.com" target="_blank" >点我</a>
```

 target:

　　_blank表示在新标签页中打开目标网页

　　_self表示在当前标签页中打开目标网页

href属性指定目标网页地址。该地址可以有几种类型：

　　绝对URL - 指向另一个站点（比如 href="http://www.jd.com）
　　相对URL - 指当前站点中确切的路径（href="index.htm"）
　　锚URL - 指向页面中的锚（href="#top"），博客的目录经常用到，还可以跳转到 name属性为p1的a标签上，

### 列表 

1.无序列表

```
<ul type="disc">
  <li>第一项</li>
  <li>第二项</li>
</ul>
```

type属性：

　　disc（实心圆点，默认值）
　　circle（空心圆圈）
　　square（实心方块）
　　none（无样式）

2.有序列表

```
<ol type="1" start="2">
  <li>第一项</li>
  <li>第二项</li>
</ol>
```

type属性： start是从数字几开始

　　1 数字列表，默认值
　　A 大写字母
　　a 小写字母
　　Ⅰ大写罗马
　　ⅰ小写罗马

3.标题列表

```
<dl>
  <dt>标题1</dt>
  <dd>内容1</dd>
  <dt>标题2</dt>
  <dd>内容1</dd>
  <dd>内容2</dd>
</dl>
```

### 表格 

​	表格是一个二维数据空间，一个表格由若干行组成，一个行又有若干单元格组成，单元格里可以包含文字、列表、图案、表单、数字符号、预置文本和其它的表格等内容。

​	表格最重要的目的是显示表格类数据。表格类数据是指最适合组织为表格格式（即按行和列组织）的数据。

​	表格的基本结构：

```
<table border="1">
            <thead> <!-- 标题部分 -->
                <tr> <!-- 表示一行 -->
                    <th>序号</th> <!-- 一个单元表格 -->
                    <th>姓名</th>
                    <th>爱好</th>
                </tr>
            </thead>
            <tbody> <!-- 内容部分 -->
                <tr>
                    <td>1</td> <!-- 一个单元表格 -->
                    <td>老张</td>
                    <td>足球</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>老王</td>
                    <td>篮球</td>
                </tr>
            </tbody>
        </table>
```

 属性:
　　border: 表格边框.
　　cellpadding: 内边距 （内边框和内容的距离）
　　cellspacing: 外边距.（内外边框的距离）
　　width: 像素 百分比.（最好通过css来设置长宽）
　　rowspan: 单元格竖跨多少行
　　colspan: 单元格横跨多少列（即合并单元格）

### input标签 

<input>元素会根据不同的 type 属性，变化为多种形态

![img](https://img2018.cnblogs.com/blog/1513655/201812/1513655-20181222115859566-65553819.png)

input属性说明：

　　name：表单提交时的“键”，注意和id的区别
　　value：表单提交时对应项的值
　　　　type="button", "reset", "submit"时，为按钮上显示的文本年内容
　　　　type="text","password","hidden"时，为输入框的初始值
　　　　type="checkbox", "radio", "file"，为输入相关联的值
　　checked：radio和checkbox默认被选中的项
　　readonly：text和password设置只读
　　disabled：所有input均适用

代码示例：

```
<div>
        <!-- input输入、单选、多选、文件上传、日期时间、下拉选项 -->
        <div>
            <!-- label for属性和id一样就关联在一起 点击获得光标-->
            <label for="username">账户</label>
            <!-- disabled放在form表单中提交后得不到该值
            将disabled="disabled" 改为 readonly = "readonly"只读即可
            -->
            <input id="username" type="text" name="zh">
        </div>
        <div>
            <!-- label另一种转到光标方法 -->
            <label>密码
                <!-- password不显示明文 -->
            <input type="password" name="mm">
            </label>
        </div>
        <div>
            <label>头像
                <input type="file" name="avatar">
            </label>
        </div>

        <div>日期
            <input type="date" name="date">
        </div>
        <p>时间
            <input type="time" name="time">
        </p>
        <P>性别
            <!-- type="radio"单选框 -->
            <input type="radio" name="boy">男
            <input type="radio" name="girl">女
        </P>
        <p>爱好
            <!-- type="checkbox"复选框 checked设置默认选项-->
            <input type="checkbox" name="hobby" checked value="girl">女
            <input type="checkbox" name="hobby" value="boy">男
            <input type="checkbox" name="hobby" value="baoj">宝剑
            <input type="checkbox" name="hobby" value="dy">电影
        </p>
        <input type="submit" value="提交">
        <input type="reset" value="重置">
        <input type="button" value="普通按钮">
        <input type="hidden" value="隐藏输入框">
        <input type="file" name="文本框">
    </div>

​```
```

显示效果：

![img](https://img2018.cnblogs.com/blog/1513655/201812/1513655-20181222115700921-50987480.png)

 

 综合练习代码：

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>qd0201</title>
    <!-- <link rel="stylesheet" type="text/css" href="qd0203.css"> -->
    <style type="text/css">
        ul{
        background: #3CDAE5;color: #FBF9F9
    }

    </style>
</head>
<body>
    <!-- form标签实现与服务器数据交流 -->
    <form action="http://127.0.0.1:8001" method="post" enctype="multipart/form-data">
        <a href="https://www.mi.com" target="_blank">点我传送</a>
        <a href="#username" target="_self">点我传送</a>
        <div>我是div</div>
        <span>我是span</span>

        <!-- ul无序、ol有序、dl标题 列表 -->
        <ul type="disc">
            <li>Mysql从删库到跑路</li>
            <li>C++从入门到入土</li>
        </ul>
        <!-- <ul type="circle"> -->
        <ul type="square">
            <li>大数据</li>
            <li>Python</li>
        </ul>
        <ol type="I" start="2">
            <li>我信你个鬼</li>
            <li>下水道三帅</li>
        </ol>
        <dl>
            <dt>标题1</dt>
            <dd>内容1  <>©&¥®</dd>
            <dt>标题2</dt>
            <dd>内容2  ><&©¥®</dd>
        </dl>

        <!-- 表格 -->
        <table border="1" cellpadding="3" cellspacing="3" >
            <thead>
                <tr>
                    <th>序号</th>
                    <th>姓名</th>
                    <th>爱好</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>狗子</td>
                    <td>宝剑</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td colspan="2">二蛋</td>
                    <!-- <td>日天</td> -->
                </tr>
            </tbody>

        </table>

        <!-- input输入、单选、多选、文件上传、日期时间、下拉选项 -->
        <div>
            <!-- label for属性和id一样就关联在一起 点击获得光标-->
            <label for="username">账户</label>
            <!-- disabled放在form表单中提交后得不到该值
            将disabled="disabled" 改为 readonly = "readonly"只读即可
            -->
            <input id="username" type="text" name="zh">
        </div>
        <div>
            <!-- label另一种转到光标方法 -->
            <label>密码
                <!-- password不显示明文 -->
            <input type="password" name="mm">
            </label>
        </div>
        <div>
            <label>头像
                <input type="file" name="avatar">
            </label>
        </div>

        <div>日期
            <input type="date" name="date">
        </div>
        <p>时间
            <input type="time" name="time">
        </p>
        <P>性别
            <!-- type="radio"单选框 -->
            <input type="radio" name="boy">男
            <input type="radio" name="girl">女
        </P>
        <p>爱好
            <!-- type="checkbox"复选框 checked设置默认选项-->
            <input type="checkbox" name="hobby" checked value="girl">女
            <input type="checkbox" name="hobby" value="boy">男
            <input type="checkbox" name="hobby" value="baoj">宝剑
            <input type="checkbox" name="hobby" value="dy">电影
        </p>
        <input type="submit" value="提交">
        <input type="reset" value="重置">
        <input type="button" value="普通按钮">
        <input type="hidden" value="隐藏输入框">
        <input type="file" name="文本框">

        <!-- select下拉选项 -->
        <div>
            <!-- <select name="city" id="city" multiple> 设置成多选-->
            <select name="city" id="city">
                <option value="1">北京</option>
                <!-- selected="selected"设置成default-->
                <option selected="selected" value="2">上海</option>
                <option value="3">广州</option>
                <option value="4">深圳</option>
            </select>
        </div>

        <!-- textarea 多行文本 rows行数 cols列数 disabled="disabled" 禁用-->
        <textarea name="多行文本" rows="10px" cols="20px" >
            ...
        </textarea>
    </form>

</body>
</html>
```



 