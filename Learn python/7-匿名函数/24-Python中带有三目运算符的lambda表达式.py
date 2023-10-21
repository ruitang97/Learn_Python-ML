# 编写一个函数，用于求两个变量的最大值
def fn1(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# lambda表达式简化以上代码
fn2 = lambda num1, num2 : num1 if num1 > num2 else num2
print(fn2(10, 20))