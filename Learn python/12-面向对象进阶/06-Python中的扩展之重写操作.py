# 定义父类
class Animal(object):
    def eat(self):
        print('i can eat food')
    def call(self):
        print('i can call')

# 定义子类
class Cat(Animal):
    # 继承Animal类并重写父类中的call方法
    def call(self):
        print('i can miaomiao call')

# 定义子类
class Dog(Animal):
    # 继承Animal类并重写父类中的call方法
    def call(self):
        print('i can wangwang call')

cat = Cat()
cat.eat()
cat.call()

dog = Dog()
dog.eat()
dog.call()