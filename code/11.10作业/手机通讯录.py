import re
import pypinyin


class person(object):
    def __init__(self, telno, name):
        self.telno = telno
        self.name = name
        self.quanping = pypinyin.lazy_pinyin(name)
        self.shouxie = ''.join(pypinyin.lazy_pinyin(name, style=pypinyin.Style.FIRST_LETTER))

    def search(self, input_str):
        pattern = re.compile(input_str)
        return self if bool(pattern.search(str(self.telno))) or bool(pattern.search(self.name)) or bool(list(filter(lambda x:pattern.search(x) !=None, self.quanping))) or bool(pattern.search(self.shouxie)) else None

    def __repr__(self):
        return "name:{},telno:{}".format(self.name, self.telno)


if __name__ == "__main__":
    ls = [person(13973300737, '张三'), person(15173300737, '李四三')]
    input_str = input("搜索：")
    res = []
    for p in ls:
        res.append(p.search(input_str))
    print(res)
