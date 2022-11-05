"""
1- vue实例对象在整个生命周期会默认执行以下方法:

    var vm = new Vue({
            el: "#app",
            data: {
                message: 123
            },
            beforeCreate() {
                console.log("vm对象实例化之前")
            },
            created() {
              console.log("vm对象实例化之后")
            },
            beforeMount() {
                console.log("vm将作用标签之前")
            },
            mounted() { // 重要时机初始化数据使用
                console.log("vm将作用标签之后")
            },
            beforeUpdate() {
                console.log("数据或者属性更新之前")
            },
            updated() {
                console.log("数据或者属性更新之后")
            },
            beforeDestroy() {
                console.log("实例销毁前")
            },
            destroyed() {
                console.log("实例销毁后")
            },
        })




"""