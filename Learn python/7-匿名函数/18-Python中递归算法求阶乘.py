'''
一个正整数的阶乘（factorial）是所有小于及等于该数的正整数的积，如：n!=1×2×3×...×(n-1)×n
1! = 1
2! = 1x2
3! = 2! x 3
4! = 3! x 4
...
n! = (n-1)! x n
使用递归算法求10的阶乘
'''
# 1、明确这个函数要干什么
def func(n):
    # 2、寻找递归出口
    if n <= 2:
        return n
    # 3、寻找与这个问题相关的数学公式
    return func(n-1) * n

# 调用func函数，求10的阶乘
print(func(10))