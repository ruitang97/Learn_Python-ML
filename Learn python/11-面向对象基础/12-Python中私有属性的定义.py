# 定义一个Girl类
class Girl(object):
    # 定义一个__init__魔术方法，用于实现对类进行初始化操作
    def __init__(self, name):
        self.name = name
        # 声明一个私有属性
        self.__age = 18

# 实例化对象
xm = Girl('小美')
# 尝试访问name公有属性
print(xm.name)
# 尝试访问__age私有属性
print(xm.__age)