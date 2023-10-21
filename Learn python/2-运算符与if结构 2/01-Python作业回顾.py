'''
案例：实现两个变量值的交换
'''
c1 = '可乐'
c2 = '牛奶'

# 通过Python代码实现对两个变量值进行交换
# ① 设置临时变量
# ② 使用元组拆包实现变量的交换
temp = c1
c1 = c2
c2 = temp

print(c1)  # 牛奶
print(c2)  # 可乐