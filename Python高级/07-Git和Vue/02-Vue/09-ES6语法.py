"""
1- 变量声明
    var: 在方法中是局部变量, 在全局中是全局变量
    let: 只在{}内的代码块有用
        for使用的计数器用let很合适
    const: 声明一个只读常量, 不能更改


2- 对象写法
    ES5:
    var person = {
        name:'itcast',
        age:13,
        say:function(){
            alert('hello')
        }
    }
    person.say()

    或者

    var person = {};
    person.name='itheima';
    person.age=13;
    person.say = function (){alert('hello')}
    person.say();

    ----------
    ES6:
    //定义变量
    var name='itcast';
    var age=13;
    //创建对象
    var person = {
        name,
        age,
        say:function(){
            alert('hello');
        }
    };
    //调用
    person.say()

3- ES6箭头函数
    1) 定义函数
        //无参数,无返回值
        var say = ()=> {
            alert('我是无参数无返回值函数');
        }
        //有参数,无返回值
        var eat = (food) => {
            alert('我喜欢吃'+food);
        }
        //有参数,有返回值
        var total = (num1,num2) => {
            return num1+num2;
        }

    2) 改变this指向; 层级比较深的时候, this的指向就变成了window, 这时候就可以通过箭头函数解决这个指向的问题
        var person = {
            name:'itcast',
            age:13,
            say:function(){
                alert('my name is ' + this.name);
            }
        }
        //调用
        person.say()



"""