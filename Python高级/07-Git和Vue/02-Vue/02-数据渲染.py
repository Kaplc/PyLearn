"""
1- data语法: {{ 变量名 }}

2- 修改默认语法:
    在vue对象内添加: delimters: ['[[', ']]']
    例:
        var vm = new Vue({
        el: '#app',
        delimiters: ['[[', ']]'],
        data: {
            message: 'Hello Vue!',

        }

    })

"""
