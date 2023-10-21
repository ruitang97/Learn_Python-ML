class Car(object):
    # 定义一个魔术方法__init__
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model

    def run(self):
        print('i can run')

# 定义子类GasolineCar()
class Gasolinecar(Car):
    pass

# 定义子类EletricCar()
class EletricCar(Car):
    # 定义一个魔术方法__init__
    def __init__(self, brand, color, model, battery):
        # 强制调用父类中的__init__初始化方法，用于实现对brand/color/model属性进行初始化
        super().__init__(brand, color, model)
        # 早期版本
        # super(EletricCar, self).__init__()
        self.battery = battery

    def run(self):
        print('i can run with eletric')

# 了解类的继承关系（继承顺序）
print(EletricCar.__mro__)
print(EletricCar.mro())