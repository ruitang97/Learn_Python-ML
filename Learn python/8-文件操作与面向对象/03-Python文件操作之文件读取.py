# 1、打开文件
f = open('python.txt', 'r', encoding='utf-8')
# 2、读取文件
content = f.read()
print(content)
# 3、关闭文件
f.close()