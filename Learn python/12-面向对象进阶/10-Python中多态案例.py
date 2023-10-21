# ① 首先要有继承关系 ② 还要编写公共接口 => 以后调用都是通过这个接口（要求传入的参数必须是一个子类对象）
# 同一个方法，由于传递参数的不同，可以产生不同的结果，这种就称之为多态特性
class Dog(object):
    # 抽象方法（内部不需要写任何代码，但是子类必要要拥有字方法（重写））
    def work(self):
        pass

class ArmyDog(Dog):
    # 重写父类中的work方法
    def work(self):
        print('追击敌人')

class DrugDog(Dog):
    # 重写父类中的work方法
    def work(self):
        print('追查毒品')

class Person(object):
    # 定义一个公共接口（必须有一个参数，要求是一个对象类型）
    # dog是一个子类对象
    def work_with_dog(self, dog):
        dog.work()

# 创建Person类对象
p1 = Person()
# 调用公共接口，传递不同的参数，返回结果不同
p1.work_with_dog(DrugDog())
p1.work_with_dog(ArmyDog())