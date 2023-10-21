# Python文件操作与面向对象

# 一、文件的概念

## 1、什么是文件

内存中存放的数据在计算机关机后就会消失。要长久保存数据，就要使用硬盘、光盘、U 盘等设备。为了便于数据的管理和检索，引入了==“文件”==的概念。

一篇文章、一段视频、一个可执行程序，都可以被保存为一个文件，并赋予一个文件名。操作系统以文件为单位管理磁盘中的数据。一般来说，==文件可分为文本文件、视频文件、音频文件、图像文件、可执行文件等多种类别。==

![image-20210315171013811](media/image-20210315171013811.png)

## 2、思考：文件操作包含哪些内容呢？

在日常操作中，我们对文件的主要操作：创建文件、打开文件、文件读写、文件备份等等

![image-20210315171310117](media/image-20210315171310117.png)

## 3、文件操作的作用

文件操作的作用就是==把一些内容(数据)存储存放起来==，可以让程序下一次执行的时候直接使用，而不必重新制作一份，省时省力。

# 二、文件的基本操作

## 1、文件操作三步走

① 打开文件

② 读写文件

③ 关闭文件

## 2、open函数打开文件

在Python，使用open()函数，可以打开一个已经存在的文件，或者创建一个新文件，语法如下：

```python
f = open(name, mode)
注：返回的结果是一个file文件对象（后续会学习，只需要记住，后续方法都是f.方法()）
```

name：是要打开的目标文件名的字符串(可以包含文件所在的具体路径)。

mode：设置打开文件的模式(访问模式)：只读r、写入w、追加a等。

> r模式：代表以只读模式打开一个已存在的文件，后续我们对这个文件只能进行读取操作。如果文件不存在，则直接报错。另外，r模式在打开文件时，会将光标放在文件的第一行（开始位置）。

> w模式：代表以只写模式打开一个文件，文件不存在，则自动创建该文件。w模式主要是针对文件写入而定义的模式。但是，要特别注意，w模式在写入时，光标也是置于第一行同时还会清空原有文件内容。

> a模式：代表以追加模式打开一个文件，文件不存在，则自动创建该文件。a模式主要也是针对文件写入而定义模式。但是和w模式有所不同，a模式不会清空文件的原有内容，而是在文件的尾部追加内容。

文件路径：① 绝对路径 ② 相对路径

① 绝对路径：绝对路径表示绝对概念，一般都是从盘符开始，然后一级一级向下查找（不能越级），直到找到我们要访问的文件即可。

比如访问C盘路径下的Python文件夹下面的python.txt文件，其完整路径：

```powershell
Windows
C:\Python\python.txt
Linux
/usr/local/nginx/conf/nginx.conf
```

> 绝对路径一般路径固定了，文件就不能进行移动，另外在迁移过程中会比较麻烦。



② ==相对路径==：相对路径表示相对概念，不需要从盘符开始，首先需要找到一个参考点（就是Python文件本身）

同级关系：我们要访问的文件与Python代码处于同一个目录，平行关系，同级关系的访问可以使用`./文件名称`或者直接写`文件名称`即可

上级关系：如果我们要访问的文件在当前Python代码的上一级目录，则我们可以通过`../`来访问上一级路径（如果是多级，也可以通过../../../去一层一层向上访问

下级关系：如果我们要访问的文件在与Python代码同级的某个文件夹中，则我们可以通过`文件夹名称/`来访问某个目录下的文件

## 3、write函数写入文件

基本语法：

```python
f.write('要写入的内容，要求是一个字符串类型的数据')
```

## 4、close函数关闭文件

```python
f.close()
```

## 5、入门级案例

```python
# 1、打开文件
f = open('python.txt', 'w')
# 2、写入内容
f.write('人生苦短，我学Python！')
# 3、关闭文件
f.close()
```

> 强调一下：中文乱码问题，默认情况下，计算机常用编码ASCII、GBK、UTF-8

## 6、解决写入中文乱码问题

```python
# 1、打开文件
f = open('python.txt', 'w', encoding='utf-8')
# 2、写入内容
f.write('人生苦短，我学Python！')
# 3、关闭文件
f.close()
```

## 7、文件的读取操作

`read(size)方法`：主要用于文本类型或者二进制文件（图片、音频、视频...）数据的读取

size表示要从文件中读取的数据的长度（单位是字符/字节），如果没有传入size，那么就表示读取文件中所有的数据。

```python
f.read()  # 读取文件的所有内容
f.read(1024)  # 读取1024个字符长度文件内容，字母或数字
```

```python
# 1、打开文件
f = open('python.txt', 'r', encoding='utf-8')
# 2、使用read()方法读取文件所有内容
contents = f.read()
print(contents)
# 3、关闭文件
f.close()
```

`readlines()方法`：主要用于文本类型数据的读取

readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素。

```python
# 1、打开文件
f = open('python.txt', 'r', encoding='utf-8')
# 2、读取文件
lines = f.readlines()
for line in lines:
    print(line, end='')
# 3、关闭文件
f.close()
```

## 8、聊聊文件操作的mode模式

| **模式** | **描述**                                                     |
| -------- | ------------------------------------------------------------ |
| r        | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
| rb       | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。 |
| r+       | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
| rb+      | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。 |
| w        | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb       | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| w+       | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb+      | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| a        | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| ab       | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+       | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+      | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

> 虽然mode文件操作模式很多，但是我们只需要记住3个字符即可。r、w、a

> r+、w+、a+，代加号，功能全，既能读，又能写（区别在于指针到底指向不同）

> rb、wb、ab，代b的字符，代表以二进制的形式对其进行操作，适合读取文本或二进制格式文件，如图片、音频、视频等格式

> rb+、wb+、ab+，代加号，功能全，既能读，又能写（区别在于指针到底指向不同）

## 9、seek函数移动光标

无论是文件读操作，还是写操作。其起始位置都是文件光标决定的。

r => 文件头

w => 清空文件内容，指向文件头

a => 文件尾

![image-20210315183136345](media/image-20210315183136345.png)

光标在刚打开文件时，默认情况下是根据r、w、a模式相关固定的。但是我们可以通过某些方法，人为移动光标。可以通过seek方法实现。

```
f.seek(offset,whence=0)

offset：开始的偏移量，也就是代表需要移动偏移的字节数
whence：给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
```

==实际工作中，seek主要用于重置光标到起始位置。==

```python
f.seek(0)
或
f.seek(0, 0)
```

其他应用（了解）：需要在DOS窗口运行

```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # 从0开始向右移动5个字节
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # 从右向左移动3个字节
13
>>> f.read(1)
b'd'
```

# 三、文件备份案例

## 1、案例需求

需求：用户输入当前目录下任意文件名，完成对该文件的备份功能(备份文件名为xx[备份]后缀，例如：(test[备份].txt)。



实现思路：

① 接收用户输入的文件名

② 规划备份文件名

③ 备份文件写入数据

## 2、代码实现

```python
# 1、接收用户输入的文件名（要备份的文件名）
oldname = input('请输入要备份的文件名称：')  # python.txt
# 2、规划备份文件名（python[备份].txt）
# 搜索点号
index = oldname.rfind('.')
# 返回文件名和文件后缀
name = oldname[:index]
postfix = oldname[index:]
newname = name + '[备份]' + postfix
# 3、对文件进行备份操作
old_f = open(oldname, 'rb')
new_f = open(newname, 'wb')

# 读取源文件内容写入新文件
while True:
    content = old_f.read(1024)
    if len(content) == 0:
        break
    new_f.write(content)
# 4、关闭文件
old_f.close()
new_f.close()
```

## 3、查漏补缺

遗留问题：我们要备份的文件名称都是由用户通过input方法输入而来的，但是一定要记住，只要在程序中有人为输入，强烈建议对用户输入的数据进行校检。

> 所有用户的输入都是不靠谱的！

解决用户输入文件名称异常问题：

```python
# 1、接收用户输入的文件名（要备份的文件名）
oldname = input('请输入要备份的文件名称：')  # python.txt
# 2、规划备份文件名（python[备份].txt）
# 搜索点号
index = oldname.rfind('.')
# 对index进行判断，判断是否合理（index > 0)
if index > 0:
    # 返回文件名和文件后缀
    name = oldname[:index]
    postfix = oldname[index:]
    newname = name + '[备份]' + postfix
    # 3、对文件进行备份操作
    old_f = open(oldname, 'r')
    new_f = open(newname, 'w')

    # 读取源文件内容写入新文件
    while True:
        content = old_f.read(1024)
        if len(content) == 0:
            break
        new_f.write(content)
    # 4、关闭文件
    old_f.close()
    new_f.close()
else:
    print('请输入正确的文件名称，否则无法进行备份操作...')
```

# 四、文件和文件夹操作

## 1、os模块

在Python中文件和文件夹的操作要借助os模块里面的相关功能，具体步骤如下：

第一步：导入os模块

```python
import os
```

第二步：调用os模块中的相关方法

```python
os.函数名()
```

## 2、与文件操作相关方法

| **编号** | **函数**                          | **功能**             |
| -------- | --------------------------------- | -------------------- |
| 1        | os.rename(旧文件名称，新文件名称) | 对文件进行重命名操作 |
| 2        | os.remove(要删除文件名称)         | 对文件进行删除操作   |

案例：把Python项目目录下的python.txt文件，更名为linux.txt，休眠20s，刷新后，查看效果，然后对这个文件进行删除操作。

```python
# 第一步：导入os模块
import os
# 第三步：引入time模块
import time


# 第二步：使用os.rename方法对python.txt进行重命名
os.rename('python.txt', 'linux.txt')

# 第四步：休眠20s
time.sleep(20)

# 第五步：删除文件（linux.txt)
os.remove('linux.txt')
```

## 3、与文件夹操作相关操作

前提：

```python
import os
```

相关方法：

| **编号** | **函数**                 | **功能**                                    |
| -------- | ------------------------ | ------------------------------------------- |
| 1        | os.mkdir(新文件夹名称)   | 创建一个指定名称的文件夹                    |
| 2        | os.getcwd()              | current  work   directory，获取当前目录名称 |
| 3        | os.chdir(切换后目录名称) | change  directory，切换目录                 |
| 4        | os.listdir(目标目录)     | 获取指定目录下的文件信息，返回列表          |
| 5        | os.rmdir(目标目录)       | 用于删除一个指定名称的"空"文件夹            |

案例1：

```python
# 导入os模块
import os


# 1、使用mkdir方法创建一个images文件夹
if not os.path.exists('images'):
	os.mkdir('images')

if not os.path.exists('images/avatar')
    os.mkdir('images/avatar')

# 2、getcwd = get current work directory
print(os.getcwd())

# 3、os.chdir，ch = change dir = directory切换目录
os.chdir('images/avatar')
print(os.getcwd())

# 切换到上一级目录 => images
os.chdir('../../')
print(os.getcwd())

# 4、使用os.listdir打印当前所在目录下的所有文件，返回列表
print(os.listdir())

# 5、删除空目录
os.rmdir('images/avatar')
```

案例2：准备一个static文件夹以及file1.txt、file2.txt、file3.txt三个文件

① 在程序中，将当前目录切换到static文件夹

② 创建一个新images文件夹以及test文件夹

③ 获取目录下的所有文件

④ 移除test文件夹

```python
# 导入os模块
import os

# ① 在程序中，将当前目录切换到static文件夹
os.chdir('File')
# print(os.getcwd())

# ② 创建一个新images文件夹以及test文件夹
if not os.path.exists('images'):
    os.mkdir('images')

if not os.path.exists('test'):
    os.mkdir('test')

# ③ 获取目录下的所有文件
# print(os.listdir())
for file in os.listdir():
    print(file)

# ④ 移除test文件夹
os.rmdir('test')
```

## 4、文件夹删除补充（递归删除、慎重！）

```python
# 导入shutil模块
import shutil

# 递归删除非空目录
shutil.rmtree('要删除文件夹路径')
```

> 递归删除文件夹的原理：理论上，其在删除过程中，如果文件夹非空，则自动切换到文件夹的内部，然后把其内部的文件，一个一个删除，当所有文件删除完毕后，返回到上一级目录，删除文件夹本身。

## 5、普及路径的小知识

绝对路径：从盘符开始，一级一级向下移动，不能越级

```python
D:\PycharmProjects\pythonProject\static
```



相对路径：

① 同级路径，都在同一个文件夹中，兄弟关系，如static目录下有file1.txt和file2.txt，则file1.txt和file2.txt就是同级关系，==同级访问直接使用名称即可==。

② 下一级路径，我们的文件与另外一个文件存在上下级关系，如images文件夹中存在一个avatar文件夹，则images是上级目录，avatar是下级目录。==则我们访问avatar可以通过images/avatar来实现==。

③ 上一级路径，如果我们某些时候，向从当前目录下，跳出到外一层路径，我们可以使用==../==来实现。

## 6、学生管理系统（文件版）

所谓的文件版就是使用文件来充当学生管理系统的数据库，以达到数据永久存储的目的。



#五、Python异常

## 1、什么是异常

当检测到一个错误时，解释器就无法继续执行了，反而出现了一些错误的提示，这就是所谓的"异常"。

## 2、异常演示

```python
# 运算符
# print(10/0)

# 文件异常
f = open('python.txt', 'r')
content = f.readlines()
print(content)
```

## 3、异常捕获

基本语法：

```python
try:
    可能发生错误的代码
except(捕获):
    如果出现异常执行的代码
```

> try...except主要用于捕获代码运行时异常

案例：

```python
try:
    f = open('python.txt', 'r')
    content = f.readline()
    print(content, end='')
except:
    f = open('python.txt', 'w', encoding='utf-8')
    f.write('发生异常，执行except语句中的代码')

f.close()
```

## 4、捕获指定异常

在以上案例代码中，except相当于捕获了所有异常，无论遇到什么错误都会自动执行except中封装的代码。但是有些情况下，我们向针对性的捕获异常，并执行相应的代码。

基本语法：

```python
try:
    可能遇到异常的代码
except 异常类型:
    捕获到对应的错误以后，执行的代码
```

> ① 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常。
>
> ② 一般try下方只放一行尝试执行的代码。

案例：捕获FileNotFoundError异常

```python
try:
    f = open('python.txt', 'r')
except FileNotFoundError as e:
    print(e)
```

## 5、同时捕获多个异常

```python
try:
    print(name)
    # print(10/0)
except (NameError, ZeroDivisionError) as e:
    print(e)
```

## 6、捕获所有未知异常

无论我们在except后面定义多少个异常类型，实际应用中，也可能会出现无法捕获的未知异常。这个时候，我们考虑使用Exception异常类型捕获可能遇到的所有未知异常：

```python
try:
    可能遇到的错误代码
except Exception as e:
    print(e)
```

案例：打印一个未定义变量，使用Exception异常类进行捕获

```python
try:
    print(name)
except Exception as e:
    print(e)
```

## 7、异常捕获中else语句

else语句：表示的是如果没有异常要执行的代码。

```python
try:
    print(1)
except Exception as e:
    print(e)
else:
    print('哈哈，真开森，没有遇到任何异常')
```

案例：

```python
try:
    f = open('python.txt', 'r')
except Exception as e:
    print(e)
else:
    content = f.readlines()
    print(content, end='')
    f.close()
```

## 8、异常捕获中的finally语句

finally表示的是无论是否异常都要执行的代码，例如关闭文件、关闭数据库连接。

```python
try:
    f = open('python.txt', 'r')
except:
    f = open('python.txt', 'w')
else:
    print('哈哈，真开森，没有遇到任何异常')
finally:
    print('关闭文件')
    f.close()
```

## 9、异常的综合案例

### ☆ 异常的传递

需求：

① 尝试只读方式打开python.txt文件，如果文件存在则读取文件内容，文件不存在则提示用户即可。

② 读取内容要求：尝试循环读取内容，读取过程中如果检测到用户意外终止程序，则`except`捕获

③ 文件操作完毕后，要及时关闭文件，避免占用内存空间

```python
import time

try:
   f = open('python.txt', 'r')
   try:
       while True:
           content = f.readline()
           if len(content) == 0:
               break
           time.sleep(3)
           print(content, end='')
   except:
       # Ctrl + C（终端里面，其代表终止程序的继续执行）
       print('python.txt未全部读取完成，中断了...')
   finally:
       f.close()
except:
   print('python.txt文件未找到...')
```

### ☆ raise抛出自定义异常

在Python中，抛出自定义异常的语法为`raise 异常类对象`。

需求：密码长度不足，则报异常（用户输入密码，如果输入的长度不足6位，则报错，即抛出自定义异常，并捕获该异常）。

原生方法：

```python
def input_password():
    password = input('请输入您的密码，不少于6位：')
    if len(password) < 6:
        # 抛出异常
        raise Exception('您的密码长度少于6位')
        return
    # 如果密码长度正常，则直接显示密码
    print(password)
        
input_password()
```
