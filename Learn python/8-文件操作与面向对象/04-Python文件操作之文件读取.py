# 1、打开文件
f = open('python.txt', 'r', encoding='utf-8')
# 2、读取文件
print(f.readline()) # 读取文件的第一行，然后把文件指针向下移动
print(f.readline()) # 读取文件的第二行，然后把文件指针向下移动
print(f.readline()) # 读取文件的第三行，如果文件已经读取完毕，则此行返回为空
# 3、关闭文件
f.close()