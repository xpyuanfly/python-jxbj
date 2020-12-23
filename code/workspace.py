from flask import Flask, redirect, url_for, request
import os


class news:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def setContent(self, content):
        self.content = content


app = Flask(__name__)

# step1 : 获取全部新闻
ls_news = []
dir_path = 'c:\\news\\'
ls_filename = os.listdir(dir_path)
for filename in ls_filename:
    id = filename[0:3]
    title = filename[3:-4]
    with open(dir_path+filename, 'r', encoding='utf-8') as f_obj:
        str_content = f_obj.read()
    new = news(id, title)
    new.setContent(str_content)
    ls_news.append(new)

# print(ls_news)


@app.route('/')
def showAllNews():
    res = '<a href="/add">添加新闻</a><br>'
    for item in ls_news:
        res += '{}-<a href ="/{}/show">{}</a>---<a href="/{}/del">删除</a>--<a href="/{}/edit">修改</a><br>'.format(
            item.id, item.id, item.title, item.id, item.id)
    return res


@app.route('/<id>/show')
def showOneNews(id):
    for i in range(0, len(ls_news)):
        if ls_news[i].id == id:
            return ls_news[i].content.replace('\n', '<br>')
            break


@app.route('/<id>/del')
def deleteOneNews(id):
    for i in range(0, len(ls_news)):
        if ls_news[i].id == id:
            ls_news.pop(i)
            break
    return redirect(url_for("showAllNews"), code=302)


@app.route('/<id>/edit')
def editOneNews(id):
    res = ''
    for item in ls_news:
        if item.id == id:
            res += '<form action="/{}/update" method="POST">\
                    标题:<input type="text" name = "title" value="{}" style="width:550px"/>\
                    <input type="submit" value="修改" />\
                        </form>'.format(item.id,item.title)
            break
    return res

@app.route('/<id>/update',methods=['POST'])
def updateOneNews(id):
    if request.method == 'POST':
        title = request.form.get('title')
        for item in ls_news:
            if item.id == id:
                item.title = title
                break
    return redirect(url_for('showAllNews'),code=302)

@app.route('/add')
def addOneNews():
    res =  '<form action="/addsubmit" method="POST">\
                    id:<input type="text" name = "id" value="" /><br>\
                    标题:<input type="text" name = "title" value="" style="width:550px"/><br>\
                    正文:<textarea name = "content" value="" ></textarea><br>\
                    <input type="submit" value="添加" />\
            </form>'
    return res

@app.route('/addsubmit')
def addsubmitOneNews():
    ##
    ##
    
    return redirect(url_for('showAllNews'),code=302)
    
app.run(debug=True)
