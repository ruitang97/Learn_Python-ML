# 定义一个Person类
class Person(object):
    # 定义相关属性和方法
    def eat(self):
        print('喜欢吃零食')
    def drink(self):
        print('喜欢喝可乐')

# 创建一个p1对象
p1 = Person()
print(p1)

# 创建一个p2对象
p2 = Person()
print(p2)

# 得出结论：我们可以使用同一个类（模板）创建多个对象，但是不同对象指向的内存空间不同（因为不同对象保存的数据可能有所不同）