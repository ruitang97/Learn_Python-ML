# 定义一个Cat类
class Cat(object):
    # 定义相关属性和方法
    def eat(self):
        print('喜欢吃猫粮')
    def drink(self):
        print('喜欢喝纯净水')

# 实例化对象
cat1 = Cat()
# 动态为对象添加属性name/color => 对象.属性 = 属性值
cat1.name = '喵喵'
cat1.color = '橘黄色'
# 访问对象的属性   =>  对象.属性
print(cat1.name)
print(cat1.color)
cat1.eat()

cat2 = Cat()
cat2.name = '汤姆'
cat2.color = '灰色'
print(cat2.name)
print(cat2.color)
cat2.eat()