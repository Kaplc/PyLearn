"""
view-templates流程: view进行逻辑处理调用template生成返回数据给view, 最后经过view发送到服务端

1- 使用模板:
    1) 创建模板: 在项目目录下创建template文件夹, 在template下创建跟子应用同名的目录并把模板文件放入
    2) 设置项目模板查找路径: setting.py下TEMPLATES的'DIRS'添加os.path.join(BASE_DIR, 'temlates']
    3) view传入数据给模板: 定义字典, 通过render()传数据给模板并返回请求
    4) 模板拼接数据: 传入的字典数据会根据对应的key替换 '{{key}}'此标识



"""