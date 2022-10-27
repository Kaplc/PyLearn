import random

school_teams = [[], [], [], []] # 加个空列表代表第4小组
student_names = ["李小明", "王华", "吴小莉", "张三", "李四", "牛二", "王五", "吴六"]

for i in student_names:
    while 1:
        n = random.randint(0, 3) # 2改3,第4小组在列表下标为3

        if len(school_teams[n]) < 2 : # 判断第n小组有多少个成员,小于2就添加并退出while循环,大于等于2就继续while循环抽组
            school_teams[n].append(i)
            break

print("三个兴趣小组随机分配的小组成员为：")
for i in school_teams:
    print(i)
