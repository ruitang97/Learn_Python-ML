# 定义一个类GasolineCar汽油车
class GasolineCar(object):
    def run_with_gasoline(self):
        print('i can run with gasoline')

# 定义一个类EletricCar电动车
class EletricCar(object):
    def run_with_eletric(self):
        print('i can run with eletric')


# 定义一个混合动力汽车
class HybridCar(GasolineCar, EletricCar):
    pass


# 定义一个对象
bmw = HybridCar()
bmw.run_with_gasoline()
bmw.run_with_eletric()