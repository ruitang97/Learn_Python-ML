# 定义一个父类B
class B(object):
    def show(self):
        print('B类中的show方法')

# 定义一个子类A
class A(B):
    pass

# 实例化对象
a = A()
a.show()