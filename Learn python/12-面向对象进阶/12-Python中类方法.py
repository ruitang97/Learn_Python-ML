'''
案例：
定义一个工具类
每件工具都有自己的名称
需求 ：在类封装一个" show_tool_count "的类方法，输出使用当前这个类，创建的对象个数
'''
class Tool(object):
    # 统计Tool类创建对象的个数（类属性）
    count = 0
    # 定义一个魔术方法__init__
    def __init__(self, name):
        self.name = name
        # 每实例化一次Tool类，则对其进行+1操作
        Tool.count += 1
    # 定义一个类方法：专门用于操作类属性
    @classmethod
    def show_tool_count(cls):
        print(f'当前{cls}类一共被实例化{cls.count}次')

t1 = Tool('斧头')
t2 = Tool('榔头')

# 调用show_tool_count类方法
Tool.show_tool_count()


