# 定义一个House类（房子类）
class House(object):
    # 定义属性
    def __init__(self, area, addr):
        self.area = area
        self.addr = addr
        # 初始化一个属性，用于'将来'保存房子内的所有家具
        # [s1, s2, s3]
        self.containsItem = []

    # 定义addItem()方法，用于实现向self.containsItem中添加家具信息
    # addItem(self, 家具对象) => 这个函数才让House类与Bed类真正产生联系
    def addItem(self, item):
        # 有了item这个家具对象，首先要获取其占用面积
        needArea = item.getUsedArea()  # 床的面积
        if self.area >= needArea:
            # 在家具列表self.containsItem中追加家具对象信息
            self.containsItem.append(item)
            # 把房子的总面积-家具占用的面积
            self.area -= needArea
            # 打印摆放成功信息
            print('家具摆放成功')
        else:
            print(f'由于家具的面积{needArea}大于房间的剩余面积{self.area}，所以无法摆放此家具')

    # 定义输出方法
    def __str__(self):
        msg = '房子的地址：' + self.addr + '，房子的面积：' + str(self.area) + '平，房子内拥有的家具：'
        # 判断房子内是否有家具
        if len(self.containsItem) > 0:
            for i in self.containsItem:
                msg += i.getName() + ','
            # 再循环结束后，去掉最后面这个逗号
            msg = msg.strip(', ')
        else:
            msg += '暂无任何家具'
        return msg


class Bed(object):
    # 定义属性
    def __init__(self, name, area):
        self.name = name  # 家具名称
        self.area = area  # 存放这个家具需要多大空间
    # 定义方法
    def getName(self):
        return self.name

    def getUsedArea(self):
        return self.area

# 实例化House类
newHouse = House(100, '深圳市宝安区')
print(newHouse)

newBed1 = Bed('席梦思', 10)
newHouse.addItem(newBed1)
print(newHouse)

newBed2 = Bed('木板床', 5)
newHouse.addItem(newBed2)
print(newHouse)
