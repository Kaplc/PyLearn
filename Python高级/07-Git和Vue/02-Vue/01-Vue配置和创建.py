"""
1- 导包:
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

2- 创建vue应用示例:
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title></title>
        <!-- 开发环境版本 -->
        <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    </head>
    <body>
    <div id="app">
      {{ message }}
    </div>
    </body>
    <script type="text/javascript">

    # 创建Vue实例对象
    var app = new Vue({

        # 选择标签
      el: '#app',

      # 数据绑定
      data: {
        message: 'Hello Vue!'
      }
    })
    </script>
    </html>



    # 创建Vue实例对象
    var app = new Vue({

    })

    # 选择标签
    el: '标签id'

    # 数据绑定
    data:{
        '变量名': '值'
    }

"""
