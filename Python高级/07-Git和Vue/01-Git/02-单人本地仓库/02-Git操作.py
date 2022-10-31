"""
1- 查看文件状态
    git status

    红色表示新建文件或者新修改的文件,都在工作区.
    绿色表示文件在暂存区

2- 将工作区文件添加到暂存区
    # 添加项目中所有文件
    git add .

    # 添加指定文件
    git add login.py


3- 将暂存区文件提交到仓库区
    git commit -m '版本描述'


4- 一键提交到仓库
    git commit -am "版本描述"

5- 查看历史版本
    git log

    git reflog

6- 回退版本
     git reset --hard 版本号

7- 撤销修改
    只能撤销工作区、暂存区的代码,不能撤销仓库区的代码
    撤销仓库区的代码就相当于回退版本操作

    撤销工作区:
        git checkout 文件名

    撤销暂存区:
        1) git reset HEAD 文件名
        2) git checkout 文件名


"""
