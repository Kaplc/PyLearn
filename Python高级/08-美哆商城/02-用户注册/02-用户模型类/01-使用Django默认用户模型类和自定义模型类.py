"""
1- 自定义用户模型类继承Django默认用户模型类
    class User(AbstractUser):

2- 将修改默认Django迁移用户模型的类

3- Django默认迁移默认的用户模型类, 要修改成自定义的用户模型类
    setting下添加:
        AUTH_USER_MODEL = 'users.User'

"""
