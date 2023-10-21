# 可变数据类型
a = [1, 2, 3]

print(id(a))

# 修改字典的值
a[2] = 5
# 追加新的内容
a.append(7)

print(id(a))