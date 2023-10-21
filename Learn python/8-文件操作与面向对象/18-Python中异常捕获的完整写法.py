'''
try:
    可能出错的代码
except Exception as e:
    捕获异常类型
else:
    表示的是如果没有异常要执行的代码
finally:
    表示的是无论是否异常都要执行的代码，例如关闭文件、关闭数据库连接
'''
try:
    f = open('python.txt', 'r')
except:
    f = open('python.txt', 'w')
else:
    # 没有遇到任何异常，则读取python.txt文件内容
    print(f.read())
finally:
    # 无论是否遇到异常，都要执行finally语句中的代码
    f.close()