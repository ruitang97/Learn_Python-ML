# 定义一个Girl类
class Girl(object):
    # 定义一个__init__魔术方法，用于实现对类进行初始化操作
    def __init__(self, name):
        self.name = name
        # 声明一个私有属性
        self.__age = 18

    # 定义一个set_age函数（接口），主要对私有属性进行设置
    def set_age(self):
        # 在使用这个函数之前，必须要进行权限验证（只有超级管理员这样一些角色才能使用这个函数）
        self.__age += 1

    # 定义一个get_age函数（接口），主要对私有属性进行获取
    def get_age(self):
        # 在使用这个函数之前，必须要进行权限验证（只有超级管理员这样一些角色才能使用这个函数）
        print(self.__age)


# 实例化对象
xm = Girl('小美')
# 普通用户访问私有属性
# print(xm.__age)
# 超级管理员或者一些特定的用户，可以调用对应的接口，通过接口可以访问和设置私有属性
xm.set_age()
xm.get_age()

# 说明：私有属性设置的目的：① 保护数据，防止隐私数据被篡改或者访问