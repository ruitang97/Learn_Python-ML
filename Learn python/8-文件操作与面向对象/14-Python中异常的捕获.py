# 异常捕获
try:
    f = open('python.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()
except:
    f = open('python.txt', 'w', encoding='utf-8')
    f.write('您要访问的python.txt不存在，我们通过except对其捕获，帮助你新建python.txt文件')
    f.close()

