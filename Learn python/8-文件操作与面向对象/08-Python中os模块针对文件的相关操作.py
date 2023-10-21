'''
案例：把当前项目目录下的python.txt文件，更名为linux.txt，休眠20s，刷新后，查看效果，然后对这个文件进行删除操作。
'''

# 1、导入os模块
import os
import time

# 2、os模块中相关功能的使用 => os.方法名()
os.rename('python.txt', 'linux.txt')
# 3、休眠20s
time.sleep(20)
# 4、把linux.txt文件删除
os.remove('linux.txt')
