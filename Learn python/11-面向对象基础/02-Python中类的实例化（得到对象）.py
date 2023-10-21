# 定义一个Person类
class Person(object):
    # 定义相关属性和方法
    def eat(self):
        print('喜欢吃零食')
    def drink(self):
        print('喜欢喝可乐')

# 实例化一个p1对象，通过对象调用对应的属性和方法
p1 = Person()
print(p1)  # 如果我们直接打印Person实例化对象，则其返回p1对象所指向的内存地址

# 调用Person类中的属性或方法
p1.eat()
p1.drink()