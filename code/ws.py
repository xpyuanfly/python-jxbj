html="""
    <div id="a">
    left
        <span id="b">
        right
            <ul>
            up
                <li>down</li>
            </ul>
        east
        </span>
        west
    </div>
"""
#下面是没有用string方法的输出
from lxml import etree
sel=etree.HTML(html)
con=sel.xpath('//div[@id="a"]/text()')
for i in con:
    print(i)   #输出内容为left west

data=sel.xpath('//div[@id="a"]')[0]
info=data.xpath('string(.)')
content=info.replace('\n','').replace(' ','')
for i in content:
    print(i)
    #输出为 全部内容