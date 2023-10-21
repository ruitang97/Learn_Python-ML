'''
案例：捕获FileNotFoundError异常
'''
try:
    f = open('python.txt', 'r')
except FileNotFoundError:
    print('您要访问的python.txt文件不存在')