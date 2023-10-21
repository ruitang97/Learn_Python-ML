students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Rose', 'age': 19},
    {'name': 'Jack', 'age': 22}
]
# 按照name值升序排列（a-z/A-Z）
# sort(key=按照元素的key指向的value进行排序）
# sort(key=必须是一个函数），实际工作中，key=经常与lambda表达式相结合
# ① 按照name进行升序排列
# students.sort(key=lambda x : x['name'])
# 执行流程
# students本身是一个列表，其内部是由个字典组成的。
# students.sort()，系统首先会将列表中的3个字典元素通过遍历的方式循环取出
# 当第1次循环时，系统会将第一个字典取出来，然后放入变量x中，经过lambda表达式，返回结果x['name'] = Tom
# 当第2次循环时，系统会将第二个字典取出来，然后放入变量x中，经过lambda表达式，返回结果x['name'] = Rose
# ...取出结果为Jack
# 数据全部取出完毕后，系统会自动对字典对应三个值（Tom/Rose/Jack）按字母排序，排序完成后，其对应的字典也会自动进行排序

# ② 使用lambda表达式对以上内容进行降序排列
# students.sort(key=lambda x : x['name'], reverse=True)

# ③ 使用lambda表达式对以上内容进行age升序排列
students.sort(key=lambda x : x['age'])
print(students)