import time

try:
    f = open('python.txt', 'r')
    try:
        while True:
            content = f.read(1)
            if len(content) == 0:
                break
            print(content)
            time.sleep(3)
    except:
        # 如果人为中止这个程序，则弹出提示信息
        print('文件读取未完成，人为中断了以上代码的执行')
    finally:
        f.close()
except:
    print('您访问的python.txt文件不存在')