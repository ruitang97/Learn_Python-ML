'''
需求：用户输入当前目录下任意文件名，完成对该文件的备份功能(test.txt => 备份文件名为xx[备份]后缀，例如：(test[备份].txt)。

实现思路：
① 接收用户输入的文件名    input()
② 规划备份文件名        规划一下新文件名称 => test.txt => test[备份].txt
③ 备份文件写入数据      把原来的文件内容写入到新文件中
'''
# 1、获取用户输入的文件名称
oldname = input('请输入要备份的文件名称：')
# 2、在filename的基础上找到文件名与文件后缀，然后再文件名的基础上 + [备份] => python.txt
index = oldname.rfind('.')
# 判断index是否大于0，如果大于0代表输入的是一个合理的文件名称
if index > 0:
    filename = oldname[:index]
    postfix = oldname[index:]
    newname = filename + '[备份]' + postfix
    # 3、把老文件中的内容写入到新文件中
    old_f = open(oldname, 'rb')
    new_f = open(newname, 'wb')

    while True:
        content = old_f.read(1024)
        # 判断文件是否读取完毕，由于content返回的是一个字符串，我们只需要判断字符串的长度是否等于0
        if len(content) == 0:
            break
        # 把读取到的内容写入到新文件中
        new_f.write(content)

    new_f.close()
    old_f.close()
else:
    print('您输入的文件名称有误，请重新输入!')