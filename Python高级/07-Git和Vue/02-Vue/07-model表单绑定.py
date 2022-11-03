"""
1- v-model在表单(<input>, <textarea>, <select>)中实现数据的双向绑定

    监听用户的输入来实时更新变量

    v-model会忽略所有表单元素的value、checked、selected特性的初始值而总是将 Vue 实例的数据作为数据来源

    所以要通过data声明初始值

    例:
        <td>用 户 名</td> <td><input type="text" v-model="username" > </td></tr>
        <td>密码</td><td> <input type="password" v-model="password1"> </td></tr>
        <td>确认密码</td> <td><input type="password" v-model="password2"></td></tr>

        data: {
            username:'',
            password1:'',
            password2:'',

        },

        输入完成后会自动更新data的数值

"""