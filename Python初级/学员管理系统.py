'''
学员管理系统
系统简介
需求：进入系统显示系统功能界面，功能如下
● 1、添加学员
● 2、删除学员
● 3、修改学员信息
● 4、查询学员信息
● 5、显示所有学员信息
● 6、退出系统
● 7、备份与恢复
系统共6个功能，用户根据自己需求选取。

步骤分析
1．显示功能界面
2．用户输入功能序号实现各个功能
3. 实现完成后返回主菜单，可以继续选择功能

====================================

添加学员
1．接收用户输入学员信息，并保存
2．判断是否添加学员信息
    2.1如果学员姓名已经存在，则报错提示
    2.2如果学员姓名不存在，则准备空字典，将用户输入的数据追加到字典，再列表追加字典数据
3．对应的 if 条件成立的位置调用该函数

====================================

删除学员
按用户输入的学员姓名进行删除
1．用户输入目标学员姓名
2．检查这个学员是否存在
    2.1如果存在，则列表删除这个数据
    2.2如果不存在，则提示“该用户不存在”
3．对应的 if 条件成立的位置调用该函数

=====================================

修改学员信息
1．用户输入目标学员姓名
2．检查这个学员是否存在
    2.1如果存在，则修改这位学员的信息，例如手机号
    2.2如果不存在，则报错
3．对应的 if 条件成立的位置调用该函数

=====================================

查询学员信息
1．用户输入目标学员姓名
2．检查学员是否存在
    2.1如果存在，则显示这个学员的信息
    2.2如果不存在，则报错提示
3．对应的 if 条件成立的位置调用该函数

======================================

显示所有学员信息
1.打印所有学员信息

======================================

退出系统
1.在用户输入功能序号6的时候要退出系统

'''

def MainMeau():
    '''显示主菜单函数'''
    print()
    print()
    print('学员管理系统v1.0')
    print('=' * 20)
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员信息')
    print('4、查询学员信息')
    print('5、显示所有学员信息')
    print('6、退出系统')
    print('=' * 20)
    print('请输入对应功能序号：', end='')

def fileRead():
    file1 = open('../data.txt', 'r', encoding='utf-8')
    datalist = file1.readlines()
    file1.close()
    return datalist

def dataCopy():
    pass

def addStudent() -> object:
    global datalist
    print('===========')
    print('  添加学员 ')
    print('===========')
    print('请输入所添加学员（输入0返回）')
    k = 1
    while 1:
        newStudentName = input('姓名：')
        if newStudentName == '0':
            return
        while 1:
            newStudentID = input('身份证号：')
            if len(newStudentID) == 18 and newStudentID.isdigit():
                newStudentDateStr = newStudentName + '-' + newStudentID
                break
            elif newStudentID == '0':
                return
            else:
                print('请输入正确的身份证号码!!!')
        for i in datalist:
            if newStudentDateStr == i:
                k = 0
                print('该学员已存在!!!')
                print('++++++++++++')
            else:
                k = 1
        if k == 1:
            file = open('../data.txt', 'a', encoding='utf-8')
            file.writelines(newStudentDateStr + '\n')
            file.close()
            print('该学员信息录入成功！数据已自动备份！')
            print('+++++++++++++++')





'''
主函数
'''
# 文件初始化
file1 = open('../data.txt', 'a', encoding='utf-8')
file1.close()
# 获取数据列表
datalist = fileRead()
MainMeau()

while 1:
    num = input()
    if num == '1':
        addStudent()
        MainMeau()
    elif num == '2':
        print('2、删除学员')
    elif num == '3':
        print('3、修改学员信息')
    elif num == '4':
        print('4、查询学员信息')
    elif num == '5':
        print('==============')
        print('  所有学员信息 ')
        print('==============')
        for i in fileRead():
            print(i, end='')
        input('（输入任意键返回）')
        MainMeau()
    elif num == '6':
        print('系统已退出！')
        break
    elif num == '7':
        print('7、备份与恢复')
    else:
        print('输入有误请重新输入！')
