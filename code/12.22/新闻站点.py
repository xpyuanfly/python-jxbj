class news:
    def __init__(self,id,title,time,link):
        self.id =id
        self.title=title
        self.time = time
        self.link = link
    def setContent(self,content):
        self.content = content
    def __repr__(self):
        return "{}-{}".format(self.id,self.title)
    
#step1 : 读取磁盘中的所有新闻
news_ls=[]
dir_path = 'c:\\news\\'
import os
files = os.listdir(dir_path)
for filename in files:
    id= filename[0:3]
    title = filename.split('.')[0][3:]
    with open(dir_path+filename,'r',encoding='utf-8') as f_obj:
        filecontent = f_obj.read()
    # print(filecontent)
    new = news(id,title,None,None)
    new.setContent(filecontent)
    # print(n)
    news_ls.append(new)

#step2 : 启动站点
from flask import Flask,request,escape,redirect,url_for
app = Flask(__name__)

@app.route('/')
def showAllNews():
    res = ''
    # str_news_ls = list(map(lambda x: '<a href = {}> {}</a>'.format(x.link ,x.__repr__()),news_ls))
    for item in news_ls:
        res+= '<a href="/{}/show">{}</a> <a href="/{}/del">【删除】</a>|<a href="/{}/edit">【修改】</a><br>'.format(item.id,item.id+item.title,item.id,item.id)
    
    return '<a>添加</a><br>'+res

@app.route('/<id>/show')
def showOneNews(id):
    res = ''
    for item in news_ls:
        if item.id == escape(id):
            res+= item.content.replace("\n",'<br>')
    print(res)        
    return res

@app.route('/<id>/del')
def delOneNews(id):
    res = '<alert>删除成功</alert>'
    for i in range(0,len(news_ls)):
        if news_ls[i].id == escape(id):
            news_ls.pop(i)
            break
   
    return redirect(url_for('showAllNews'),code=302)

@app.route('/<id>/edit')
def editOneNews(id):
    for i in range(0,len(news_ls)):
        if news_ls[i].id == escape(id):
            news=news_ls[i]
            break
     
    res = '\
    <form action="/{}/update" method="POST">\
    标题：<br>\
    <input type="text" name="title" style="width:550px" value="{}">\
    <br>\
    <input type="submit" value="修改">\
    </form>'.format(news.id,news.title)
    print(res)
    return res

@app.route('/<id>/update', methods=['POST'])
def updateOneNews(id):
    if request.method == 'POST':
        # print(id)        
        title = request.form.get('title')
        # print(title)
        for i in range(0,len(news_ls)):
            if news_ls[i].id == escape(id):
                news_ls[i].title= title
                break
        return redirect(url_for('showAllNews'),code=302)

app.run(port=5000, debug=True)