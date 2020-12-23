class news:
    def __init__(self,id,title,time,link):
        self.id =id
        self.title=title
        self.time = time
        self.link = link
    def setContent(self,content):
        self.content = content
        
# step1 request获取新闻列表
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

url = 'http://www.zzrcbank.cn/dibulanmu/gywh/'
res = requests.get(url, headers = headers)
res.encoding = 'gbk'

htmlstr = res.text
# step2 解析新闻列表到对象news

from lxml import etree
selector = etree.HTML(htmlstr)
# ls = selector.xpath('//head/title')
ls_time = selector.xpath('//div[@class = "right_list"]/ul/li/span')
ls_a = selector.xpath('//div[@class = "right_list"]/ul/li/a')

import re
news_ls = []
for index in range(0,len(ls_a)):
    time = ls_time[index].text
    title = ls_a[index].text
    link = "http://www.zzrcbank.cn/{}".format(ls_a[index].attrib['href'])
    num = "".join(re.findall('\d+',link) )
    
    news_object = news(num,title,time,link)

# step3 拿到某个具体的新闻的link去获取新闻的内容
    content_res = requests.get(link,headers=headers)
    content_res.encoding = 'gbk'
    news_content = content_res.text
    
    news_content_selector =  etree.HTML(news_content)
    search_ls= news_content_selector.xpath('//div[@class="xqy_zw"]/p/text()')
    news_object.setContent(''.join(search_ls))
    
    news_ls.append(news_object)

# step4 写磁盘
dir_path = 'c:\\news\\'
import os
if not os.path.isdir(dir_path):
    os.mkdir(dir_path)

for item in news_ls:
    # print('{},{},{},{},{}'.format(item.id,item.title,item.time,item.link,item.content))
    file_path = dir_path+item.id+item.title+'.txt'
    with open(file_path,'w+',encoding='utf-8') as f_obj:
        f_obj.write(item.title+'\r\n'+item.time+'\r\n'+item.link+'\r\n'+item.content)