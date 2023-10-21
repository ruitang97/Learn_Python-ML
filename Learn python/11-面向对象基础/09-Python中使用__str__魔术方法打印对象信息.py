# 定义一个Car类
class Car(object):
    # 注意：在同一个类中，自身的属性都是通用的，可以相互访问
    # 通过__init__()初始化方法来初始化对象
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model

    # 当print(对象)时，__str__()魔术方法会自动被触发（被调用）
    def __str__(self):
        # 要求：必须有return返回值，且返回的数据类型必须是一个字符串类型
        # 应用场景：主要用于输出对象信息
        return f'品牌：{self.brand}, 颜色：{self.color}, 型号：{self.model}'

tesla = Car('特斯拉', '红色', 'Model Y')
print(tesla)

# 结论：__str__是一个魔术方法，当print打印对象时，其会自动被触发
# 实际工作中，我们如果想打印对象相关信息，通常使用__str__()魔术方法
# 注意事项：在编写__str__()魔术方法时，其返回结果必须是一个字符串类型的数据，否则会报错