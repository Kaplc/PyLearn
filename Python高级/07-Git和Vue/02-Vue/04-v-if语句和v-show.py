"""
1- v-if, v-else-if, v-else:

    通过逻辑判断规定标签显不显示

    <p v-if="seen">现在你看到我了</p>
    <img src="" alt="皇帝" v-if="level === 1">
    <img src="" alt="皇亲" v-else-if="level === 2">
    <img src="" alt="国戚" v-else-if="level === 3">
    <img src="" alt="大臣" v-else>

    var app = new Vue({
      el: '#app',
      data: {
        seen:true,
        level: '3'
      }
    })

    解析:
        在vue对象里面, seen的值为"true" p标签显示, level为3 对应第3个img标签显示

2- v-show:
    跟if类似值为true就显示
    注意在vue中使用v-show, 原来的css代码不能设置display属性, 会导致冲突


3- 区别:
    if为false是把元素直接删除源代码中不显示
    v-show是把元素的属性设置display, 源代码还存在


"""
