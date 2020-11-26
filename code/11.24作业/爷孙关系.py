'''
child-parent（孩子——父母）表，要求输出grandchild-grandparent（孙子——爷奶）表。请设计程序，读取child-parent的数据，输出grandchild-grandparent的结果。
样例输入如下所示。
•	Tom Lucy
•	Tom Jack
•	Jone Lucy
•	Jone Jack
•	Lucy Mary
•	Lucy Ben
•	Jack Alice
•	Jack Jesse
•	Terry Alice
•	Terry Jesse
•	Philip Terry
•	Philip Alma
•	Mark Terry
•	Mark Alma
'''
if __name__ == "__main__":
    input = 'Tom Lucy\n\
Tom Jack\n\
Jone Lucy\n\
Jone Jack\n\
Lucy Mary\n\
Lucy Ben\n\
Jack Alice\n\
Jack Jesse\n\
Terry Alice\n\
Terry Jesse\n\
Philip Terry\n\
Philip Alma\n\
Mark Terry\n\
Mark Alma'
    row_ls = input.split('\n')
    dic_child_parent = {}
    dic_parent_child = {}

    for row in row_ls:
        names = row.split(" ")
        childname= names[0]
        parentname = names[1]
        if childname in dic_child_parent:
            dic_child_parent[childname].append(parentname)
        else:
            dic_child_parent[childname] = [parentname]
        if parentname in dic_parent_child:
            dic_parent_child[parentname].append(childname)
        else:
            dic_parent_child[parentname] = [childname]
    print("child-parent")
    print(dic_child_parent)
    print("parent-child")
    print(dic_parent_child)

    grandchild_grandparent_ls = []
    for parent in dic_parent_child:
        for child in dic_child_parent:
            if parent == child:
                for childname in dic_parent_child[parent]:
                    for parentname in dic_child_parent[child]:
                        grandchild_grandparent_ls.append(childname+" "+parentname)
    
    grandchild_grandparent_ls=sorted(grandchild_grandparent_ls)

    print("grandchild-grandparent")
    print(grandchild_grandparent_ls)