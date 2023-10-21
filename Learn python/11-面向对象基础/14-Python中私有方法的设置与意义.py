'''
银行取钱 => ATM机操作
① 插卡 ② 用户验证（验证密码）③ 输入取款金额 ④ 取款 ⑤ 打印输出账单
'''
class ATM(object):
    # 1、插卡
    def __func1(self):
        print('插卡')
    # 2、用户验证
    def __func2(self):
        print('用户验证')
    # 3、输入取款金额
    def __func3(self):
        print('输入取款金额')
    # 4、取款
    def __func4(self):
        print('取款')
    # 5、打印输出账单
    def __func5(self):
        print('输出账单')

    # 6、定义一个公共方法withdraw()专门用于实现取款整个操作
    def withdraw(self):
        self.__func1()
        self.__func2()
        self.__func3()
        self.__func4()
        self.__func5()


# 实例化对象
atm = ATM()
# 执行取款操作
atm.withdraw()