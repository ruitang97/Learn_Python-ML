# 定义一个Person类
class Person(object):
    # 定义一个魔术方法__init__()，通常这个方法用于实现对对象的初始化（如赋予相关属性）
    def __init__(self, name, age):
        # self代表实例化对象，self.name代表为对象添加一个name属性，其值是刚传递过来的name参数
        self.name = name
        self.age = age


# 实例化Person类，产生p1对象，然后为其自动赋予name/age属性
p1 = Person('张飞', 35)
# 调用p1对象自身的name/age属性
print(p1.name)
print(p1.age)

# 实例化Person类，产生p2对象，然后为其自动赋予name/age属性
p2 = Person('赵云', 28)
# 调用p2对象自身的name/age属性
print(p2.name)
print(p2.age)

# 结论：在Python类中，通过__函数名称__()命名的函数都称之为魔术方法，拥有特殊的功能
# __init__() ： 初始化方法或构造方法，主要是实现为对象进行初始化操作（为对象赋予相关属性、如果是文件操作，可以使用__init__魔术方法打开文件）
# 执行过程：当这个类被实例化时，则__init__()方法会自动被系统调用
