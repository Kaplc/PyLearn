""""
1- v-for指令可以绑定 数组 的数据来渲染一个项目列表
     语法: v-for="变量 in 可迭代对象" 类似python的for遍历列表
     例:
        <ol>
        <li v-for="todo in todos">
              {{ todo.text }}
        </li>
        </ol>

        # 列表
            todos: [
          { text: '学习 JavaScript' },
          { text: '学习 Vue' },
          { text: '整个牛X项目' }
        ]


2-  迭代索引index(从0开始)
    <ol>
        <li v-for="(todo, index) in todos">
              {{ todo.text }} - {{ index }}
        </li>
        </ol>

    输出:
        学习 JavaScript-0
        学习 Vue-1
        整个牛X项目-2

"""