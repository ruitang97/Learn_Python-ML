'''
需求：女朋友生气了，要惩罚：连续说5遍“老婆大人，我错了”，如果道歉正常完毕后女朋友就原谅我了，这个程序怎么写？
'''
# 定义初始化计数器
i = 0
# 编写循环条件
while i < 5:
    if i == 2:
        print('说的一点不够真诚，好好说，否则就不原谅你')
        i += 1
        continue
    print('老婆大人，我错了')
    # 在循环体内部更新计数器
    i += 1
else:
    print('真开森，老婆原谅我了！')