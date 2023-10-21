# 定义一个Person类
class Person(object):
    # 定义一个__init__魔术方法，用于实现对类进行初始化操作
    def __init__(self, name):
        self.name = name
        # 声明工资信息为私有属性
        self.__salary = 18000  # 公共接口 => set_xxx、get_xxx

    # 定义一个set_salary
    def set_salary(self, salary):
        # 经过角色验证，如果有工资的操作权限，才能让其继续操作（权限验证）
        # 如果权限验证通过，则继续执行
        if 50000 >= salary > 0:
            self.__salary = salary
        else:
            print('您设置的值有误，请重新设置！')

    # 定义一个get_salary
    def get_salary(self):
        # 经过角色验证，如果有工资的操作权限，才能让其继续操作（权限验证）
        # 如果权限验证通过，则继续执行
        print(self.__salary)

# 实例化对象
p1 = Person('张三')
# 操作工资信息时，首先要登录系统，初始化一个角色
p1.set_salary(35000)
p1.get_salary()
