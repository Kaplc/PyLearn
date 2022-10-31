"""
1- 作用：
    1) 区分生产环境代码以及开发环境代码
    2) 研究新的功能或者攻关难题
    3) 解决线上bug

2- 流程:
    1) 创建分支:
        查看当前分支
            git branch
        创建并切换
            git checkout -b dev
        分支推送到远程
            git push -u origin dev

    2) 合并分支:
        1, 先切换到主分支
            git checkout master
        2, dev分支合并到master分支
            git merge dev
        3, push到服务器同步

"""
