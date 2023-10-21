# 创建一个Person类
class Person(object):
    # 结论：谁调用了这个方法，这个方法中的self参数就指向谁（实例化对象）
    def eat(self):
        print('喜欢吃零食')
    def drink(self):
        print('喜欢喝可乐')

# 创建一个p1对象
p1 = Person()
print(p1)
p1.eat()

# 创建一个p2对象
p2 = Person()
print(p2)
p2.eat()