# 定义一个函数
def func(names):
    # names = ['张三','李四','王五']
    names.append('赵六')


# 定义一个全局变量
list1 = ['张三', '李四', '王五']
# 调用函数
func(list1)

print(list1)  # ['张三', '李四', '王五'] or ['张三', '李四', '王五', '赵六]