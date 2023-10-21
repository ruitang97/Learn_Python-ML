a = 10
print(id(a))

b = a
print(id(b))

# 尝试更改变量a的值
a = 100
print(id(a))

print(id(b))
print(b)  # 10 or 100