class C(object):
    def func(self):
        print('C类中的func方法')

class B(C):
    pass

class A(B):
    # A --> B --> C所以可以得出结论A --> C
    pass

a = A()
a.func()