'''
案例2：小明体重75.0公斤，小明每次跑步会减掉0.50公斤，小明每次吃东西体重增加1公斤。
分析：① 对象：小明② 属性：姓名、体重③ 方法：跑步、吃东西
'''
class Person(object):
    # 定义对象属性name/weight
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    # 定义一个run方法，用于实现跑步减体重操作
    def run(self):
        self.weight -= 0.5

    # 定义一个eat方法，用于实现吃东西增加体重操作
    def eat(self):
        self.weight += 1

    # 定义一个__str__魔术方法
    def __str__(self):
        return f'姓名：{self.name}，当前体重为：{self.weight}'


p1 = Person('小明', 75.0)
# 调用run方法，实现跑步减体重效果
p1.run()
print(p1)

# 调用eat方法，实现吃东西增加体重效果
p1.eat()
print(p1)
