# 1、导入os模块
import os
# 2、创建一个images文件夹
if not os.path.exists('images'):
    os.mkdir('images')

if not os.path.exists('images/avatar'):
    os.mkdir('images/avatar')

# 3、获取当前工作路径（我在哪？）
print(os.getcwd())
# 4、切换到指定目录
os.chdir('images/avatar')
print(os.getcwd())
# 5、跳出到newProject文件夹（需要从当前路径向上跳2级）
os.chdir('../../')
print(os.getcwd())
# 6、打印当前目录下的所有文件信息（以列表形式返回）
print(os.listdir())
# 7、删除images目录下的avatar文件夹
os.rmdir('images/avatar')