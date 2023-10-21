'''
多态特性：一种公共方法，随着传入参数（对象）不同，则同一个方法可以返回不同的结果
'''
class Fruit(object):
    # 这个makejuice方法里面可以什么都不写，主要是为了规范子类的行为
    # 父类有makejuice方法，则子类必须拥有这个方法，然后对其进行重写
    # 在其他编程语言中，这个方法叫抽象方法
    def makejuice(self):
        print('i can make juice')

# 定义Apple类，继承Fruit类，并重写父类中的makejuice方法
class Apple(Fruit):
    def makejuice(self):
        print('i can make apple juice')

# 定义Banana类，继承Fruit类，并重写父类中的makejuice方法
class Banana(Fruit):
    def makejuice(self):
        print('i can make banana juice')

# 定义Orange类，继承Fruit并重写父类中的makejuice方法
class Orange(Fruit):
    def makejuice(self):
        print('i can make orange juice')

# 定义一个公共的方法，用于调用makejuice功能
def service(obj):
    obj.makejuice()

service(Apple())
service(Banana())
service(Orange())