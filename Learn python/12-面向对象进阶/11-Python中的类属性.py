# 定义一个Person类，为其定义一个类属性 => count，用于统计这个类被实例化了多少次（统计总人数）
class Person(object):
    # 定义类属性
    count = 0
    # 定义实例属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # 类名.属性，相当于调用类属性
        Person.count += 1

# 实例化对象
p1 = Person('Tom', 23)
p2 = Person('Lily', 19)

# 尝试访问Person类中的count属性
print(f'Person类一共实例化了{Person.count}次')