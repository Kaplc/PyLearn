if __name__ == '__main__':
    # 多装饰器
    def make_div(func):
        print("div装饰器")

        def inner():
            result_div = "<div>" + func() + "</div>"
            return result_div

        return inner


    def make_p(func):
        print("p装饰器")

        def inner():
            result_p = "<p>" + func() + "</p>"
            return result_p
        return inner

    # 执行顺序就进原则, 逐层装饰
    @make_div
    @make_p
    def content():
        return "标签"

    result = content()
    print(result)
