# 定义一个父类Car
class Car():
    def run(self):
        print('i can run')

# 定义一个油车
class GasolineCar(Car):
    pass

# 定义一个电车
class EletricCar(Car):
    pass

# 实例化对象
tesla = EletricCar()
tesla.run()