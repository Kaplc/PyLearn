"""
1- v-on 可以监听事件并触发js代码( 简写@ )
    例:
        <div id="app">
            # 定义click事件并命名"add"
            <button v-on:click="add">Add {{counter}}</button>
        </div>

        # vue对象中添加methods方法控制事件
        data: {
            counter:0
        },
        methods:{
        add:function(){
          # this表示本对象中的counter
          this.counter = num+this.counter
          alert(this.counter)
        }
      }

      ------------
      # 事件含参数
      <div id="app">
            # 定义click事件并命名"add"
            <button v-on:click="add(counter)">Add {{counter}}</button>
            # 简写
            <button @click="add(counter)">Add {{counter}}</button>
      </div>

      methods:{
        # 传入参数
        add:function(counter){
          this.counter = num+this.counter
          alert(this.counter)
        }
      }
"""