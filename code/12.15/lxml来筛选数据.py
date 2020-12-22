from lxml import etree

foj = open('C:\\Users\\yxp\\Desktop\\PYTHON\\python-jxbj\\code\\12.15\\1.html','r',encoding='utf-8')
strhtml = foj.read()
# print(strhtml)


selector=etree.HTML(strhtml) #将源码转化为能被XPath匹配的格式

ls_time = selector.xpath('//ul/li/span[@class="float_right"]/text()') #返回为一列表
ls_a = selector.xpath('//div[@class="right_list"]/ul/li/a[starts-with(@href,"/dibulanmu/gywh")]/@href') #返回为一列表

for item in ls_a:
    print(item)
print(len(ls_a))