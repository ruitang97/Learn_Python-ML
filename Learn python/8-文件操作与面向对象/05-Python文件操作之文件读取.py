# 1、打开文件
f = open('python.txt', 'r', encoding='utf-8')
# 2、读取文件
print(f.readlines())     # 读取完毕后，文件指针指向文件的最后一行
f.seek(0)                # 重置文件指针
for i in f.readlines():
    print(i)
# 3、关闭文件
f.close()