'''
案例1：定义学员信息类，包含姓名、成绩属性，定义成绩打印方法（90分及以上显示优秀，80分及以上显示良好，
70分及以上显示中等，60分及以上显示合格，60分以下显示不及格）
'''
class Student(object):
    # 定义魔术方法，用于初始化对象属性
    def __init__(self, name, score):
        # 定义属性
        self.name = name
        self.score = score

    # 定义方法，用于打印学生的成绩信息
    def print_grade(self):
        # 调用自身score属性，判断其值
        if self.score >= 90:
            print(f'学生姓名：{self.name}, 成绩：{self.score}，等级：优秀')
        elif self.score >= 80:
            print(f'学生姓名：{self.name}, 成绩：{self.score}，等级：良好')
        elif self.score >= 70:
            print(f'学生姓名：{self.name}, 成绩：{self.score}，等级：中等')
        elif self.score >= 60:
            print(f'学生姓名：{self.name}, 成绩：{self.score}，等级：及格')
        else:
            print(f'学生姓名：{self.name}, 成绩：{self.score}，等级：不及格')

# 实例化对象
s1 = Student('小明', 85)
s1.print_grade()