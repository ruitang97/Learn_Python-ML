'''
1 1 2 3 5 8 13 21 34 ...
# 1、明确这个函数要做什么？
求斐波那契第15位的结果
# 2、寻找递归出口（这个死循环在什么情况下会自动结束）
当n==1或n==2，其会自动终止
# 3、寻找与问题相关的数学模型
func(n) = func(n-1) + func(n-2)
'''
def func(n):
    # 如果n == 1 or n == 2
    if n == 1 or n == 2:
        return 1
    # 寻找与问题相关的最小数学公式
    # return func(4) + func(3)
    # return func(3) + func(2)
    # return func(2) + func(1)
    # 先求func(2) = 1
    # 在求func(1) = 1
    return func(n-1) + func(n-2)

# 调用func函数
print(func(5))