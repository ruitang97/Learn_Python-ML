# 定义一个Monkey类
class Monkey(object):
    # 定义一个方法，如show_info，用于打印对象自身的属性信息
    def show_info(self):
        print(f'我的名字叫：{self.name}，我的技能：{self.skill}')

# 实例化对象
swk = Monkey()
# 动态为swk对象添加属性
swk.name = '孙悟空'
swk.skill = '筋斗云、七十二变'
# 调用show_info方法，获取自身属性的相关信息
swk.show_info()