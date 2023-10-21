# 求三个数
fn1 = lambda a, b, c=100 : a + b + c

# 使用默认值
print(fn1(10, 20))

# 替换默认值
print(fn1(10, 20, 30))