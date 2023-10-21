# 定义Game游戏类
class Game(object):
    # 定义一个类属性，用于记录游戏历史最高分
    top_score = 0

    # 定义一个初始化方法，用于声明对象属性
    def __init__(self, name):
        self.player_name = name

    # 定义一个对象方法，用于某个玩家开始游戏
    def start_game(self):
        print('开始游戏...')

    # 定义一个静态方法，用于显示游戏的帮助信息
    @staticmethod
    def show_help():
        print('游戏的帮助信息')

    # 定义一个类方法，用于操作和获取类属性
    @classmethod
    def show_top_score(cls):
        print(cls)
        return cls.top_score


g = Game('heima')
g.show_help()

g.start_game()

Game.show_top_score()
