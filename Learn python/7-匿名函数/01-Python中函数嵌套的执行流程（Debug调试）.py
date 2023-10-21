def funcB():
    print('开始执行funcB函数')
    print('结束调用funcB函数')

def funcA():
    print('开始执行funcA函数')
    funcB()
    print('结束调用funcA函数')

funcA()

# step over：代码一步一步向下执行，遇到函数，直接返回函数的执行结果（不进入函数内部）
# step into：代码一步一步向下执行，遇到函数，直接进入到函数体内容，一步一步执行，直到函数执行完毕