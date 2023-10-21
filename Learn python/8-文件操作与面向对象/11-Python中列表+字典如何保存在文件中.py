# 1、定义一个变量，用于存储所有学员的信息
students = []

# 2、添加学员到students列表中
student = {}
student['name'] = '张三'
student['age'] = 23
student['mobile'] = '10086'

students.append(student)

student = {}
student['name'] = '李四'
student['age'] = 24
student['mobile'] = '10010'

students.append(student)

# 3、保存students中的数据到data.txt文件中
# f = open('data.txt', 'w', encoding='utf-8')
# f.write(str(students))
# f.close()

# 4、从data.txt中读取所有的学生信息
f = open('data.txt', 'r', encoding='utf-8')
content = f.read()
# print(content)
# print(type(content))
# 5、把content（字符串）转换为原数据类型
content = eval(content)
print(content)
print(type(content))
for i in content:
    print(i, type(i))
f.close()