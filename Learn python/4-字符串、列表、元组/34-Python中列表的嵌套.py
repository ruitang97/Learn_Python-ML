'''
应用场景：要存储班级一、二、三 => 三个班级学生姓名，且每个班级的学生姓名在一个列表。
'''
list1 = ['1班张三', '1班李四']
list2 = ['2班王五', '2班赵六']
list3 = ['3班田七', '3班钱八']

# biglist = [1班信息, 2班信息, 3班信息]
# 列表嵌套
# biglist = [0, 1, 2]
biglist = [['1班张三', '1班李四'], ['2班王五', '2班赵六'], ['3班田七', '3班钱八']]
# 列表嵌套之元素的访问，如访问2班的赵六，应该如何书写？
print(biglist[1])  # 取出2班的信息
print(biglist[1][1])  # 取出2班赵六的信息