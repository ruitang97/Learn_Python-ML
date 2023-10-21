# 定义一个Game类
class Game(object):
    # 定义一个menu()菜单功能：这个功能既不需要调用对象属性也不需要调用对象方法，也不需要调用类属性也不需要调用类方法
    @staticmethod
    def menu():
        print('1、开始游戏')
        print('2、暂停游戏')
        print('3、退出游戏')

# 调用方式
Game.menu()

# 实例化对象
g = Game()
g.menu()
