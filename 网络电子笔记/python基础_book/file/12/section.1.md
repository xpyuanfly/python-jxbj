## 面向对象方式的学生管理系统

整个系统中有3个程序文件:

### 1. student.py

这个文件中定义了学生类.

```python
# 学生类
class Student(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
```

### 2.student\_manager\_system.py

这个文件中定义了**StudentManagerSystem**类

```python
from student import Student
import os


# 定义学生管理系统类， 顶级函数和顶级类都要有两个换行
class StudentManagerSystem(object):

    def __init__(self):
        # 用于存储学生信息
        self.student_list = []

    # 显示功能菜单
    @staticmethod
    def show_menu():
        print("-----学生管理系统V1.0-------")
        print("1. 添加学生")
        print("2. 删除学生")
        print("3. 修改学生")
        print("4. 查询学生")
        print("5. 查询所有学生")
        print("6. 退出")

    # 添加学生
    def append_student(self):
        print("添加学生")
        # 接收学生信息
        name = input("请输入学生的姓名:")
        age = input("请输入学生的年龄:")
        sex = input("请输入学生的性别:")

        # # 创建空的字典
        # student_dict = {}
        # # 给字典添加键值对
        # student_dict["name"] = name
        # student_dict["age"] = age
        # student_dict["sex"] = sex

        # 创建学生对象
        student = Student(name, age, sex)

        # 把学生字典添加到学生列表里面
        self.student_list.append(student)

    # 显示所有的学生信息
    def show_all(self):
        print("查询所有学生")
        for index, student in enumerate(self.student_list):
            print("学号: %d 姓名: %s 年龄: %s 性别: %s" % (index + 1,
                                                   student.name,
                                                   student.age,
                                                   student.sex))

    # 删除学生
    def remove_student(self):
        print("删除学生")
        # 接收用户输入的学号
        student_no = int(input("请输入要删除学生的学号:"))
        # 把学号转成下标
        index = student_no - 1

        # 判断下标是否合法
        if index >= 0 and index < len(self.student_list):
            # 根据下标删除对应的学生
            del self.student_list[index]
        else:
            print("您要删除的学生不存在!")

    # 修改学生信息
    def modify_student(self):
        print("修改学生")
        # 获取要修改学生的学号
        student_no = int(input("请输入要修改学生的学号:"))
        # 把学号转成下标
        index = student_no - 1
        # 判断下标是否合法
        if index >= 0 and index < len(self.student_list):
            # 根据下标获取要修改学生的字典信息
            student = self.student_list[index]
            # 接收用户输入修改后的信息
            new_name = input("请输入修改后姓名:")
            new_age = input("请输入修改后的年龄:")
            new_sex = input("请输入修改后的性别:")
            # # 修改字典里面的信息
            # student_dict["name"] = new_name
            # student_dict["age"] = new_age
            # student_dict["sex"] = new_sex

            # 修改对象属性
            student.name = new_name
            student.age = new_age
            student.sex = new_sex

        else:
            print("您要修改的学生不存在!")

    # 查询学生
    def query_student(self):
        print("查询学生")
        # 接收用户输入的姓名
        name = input("请输入您要查询的学生姓名:")

        # 遍历学生列表，判断姓名是否相同
        for index, student in enumerate(self.student_list):
            if student.name == name:
                print("找到了,信息如下:")
                print("学号: %d 姓名: %s 年龄: %s 性别: %s" % (index + 1,
                                                       student.name,
                                                       student.age,
                                                       student.sex))
                break
        else:
            print("对不起，没有找到该学生")

    # 保存数据
    def save_data(self):
        # 打开文件
        file = open("students.data", "w", encoding="utf-8")

        # [{"name": "张三"}, person2]
        # 把列表对象转成列表字典存储到文件里面，因为字典是数据，可以根据字典创建后续使用的学生对象
        # 1. 列表推导式  2. map
        new_list = [student.__dict__ for student in self.student_list]
        # 列表转成字符串
        student_list_str = str(new_list)

        print("写入文件的数据:", student_list_str)
        # 写入数据，把学生列表写入文件
        file.write(student_list_str)
        # 关闭文件
        file.close()

    # 加载文件中的数据
    def load_data(self):

        print("读取文件中的数据")
        # 判断数据文件是否存在
        if os.path.exists("students.data"):

            # 打开文件
            file = open("students.data", "r", encoding="utf-8")
            # 读取数据, 这里的数据是字符串
            file_data = file.read()

            # "[{'name': '张三', 'age': '20', 'sex': '男'}]"

            new_student_list = eval(file_data)

            # 把列表字典转成列表学生对象
            new_list = [Student(student_dict["name"],
                                 student_dict["age"],
                                 student_dict["sex"])
                                 for student_dict in new_student_list]

            print("读取文件的数据:", new_list)

            # 1. 把数据直接赋值给student_list 这个全局变量
            # global student_list
            # student_list = new_student_list
            # print("load_data:", student_list)

            # 2. 把文件读取到的数据添加到学生列表里面来
            self.student_list.extend(new_list)
            # 关闭文件
            file.close()
        else:
            print("还没有本地文件数据")

    # 程序的入口函数，程序启动后执行的函数
    def run(self):

        # 加载文件中的数据，只加载一次
        self.load_data()

        while True:

            # 显示功能菜单
            self.show_menu()
            # 接收用户输入的功能选项
            menu_option = int(input("请输入功能选项:"))
            if menu_option == 1:
                # 添加学生
                self.append_student()
            elif menu_option == 2:
                # 删除学生
                self.remove_student()
            elif menu_option == 3:
                # 修改学生
                self.modify_student()
            elif menu_option == 4:
                # 查询学生
                self.query_student()
            elif menu_option == 5:
                self.show_all()
            elif menu_option == 6:
                # 在程序退出之前，保存学生列表中的数据到文件
                self.save_data()
                print("程序退出了")
                break
```

### 3. main.py

这个文件是系统启动的入口文件,运行这个文件系统才能启动.

```python
from student_manager_system import StudentManagerSystem

if __name__ == '__main__':
    # 创建学生管理系统对象
    system = StudentManagerSystem()
    # 让系统运行起来
    system.run()
```



