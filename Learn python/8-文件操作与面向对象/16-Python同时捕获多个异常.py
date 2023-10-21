try:
    # print(8/0)
    f = open('python.txt', 'r')
except (ZeroDivisionError, FileNotFoundError):
    # print('除数为0异常')
    print('您要访问的python.txt文件不存在')