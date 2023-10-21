'''
1、打开文件
name：打开文件的名称（可以包含具体的路径）
mode：访问模式
r read只读模式
w write只写模式
a append只写模式，追加模式，在文件的末尾追加
总结：访问模式w和访问模式a之间的区别？
w：代表把文件的内容先清空，然后再写入内容。
a：代表不清空文件的原因内容，而是在文件的末尾追加新内容

encoding='utf-8'：代表以utf-8的编码格式读取文件内容
2、读写文件
3、关闭文件
'''
f = open('File/python.txt', 'r', encoding='utf-8')
content = f.read()
print(content)
f.close()