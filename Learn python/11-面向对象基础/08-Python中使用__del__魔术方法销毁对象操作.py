# 定义一个Person类
class Person(object):
    # 定义一个__init__初始化方法，为Person实例化对象赋予name/age属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义一个__del__()魔术方法，当对象被删除或销毁时，__del__方法会自动被调用
    def __del__(self):
        # 一般用于执行一些程序的销毁操作（如文件操作中，可以使用__del__专门用于关闭文件）
        print('当对象被删除或销毁时，自动被调用')

p1 = Person('白骨精', 30)
print(p1.name)
print(p1.age)

del p1
# 执行到这里，p1对象没有在继续被调用，则系统要结束了，系统结束前，要把p1对象销毁
# 当系统准备删除p1对象时 => 调用__del__方法（放入一些清理工作） => 真正开始销毁对象p1
