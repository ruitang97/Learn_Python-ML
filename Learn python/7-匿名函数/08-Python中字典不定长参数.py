'''
对于一个函数num，当调用num(1,2,a=3,b=4)和调用num(3,4,5,6,a=1)以及num(a=1,b=2)的时候都可以正常运行，
并且可以对元组以及字典类型进行遍历输出，对字典类型进行输出字典的键值对(形式为：key：a，value：1)，请写出这个函数并完成调用。
'''
def num(*args, **kwargs):
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(f'key:{key}, value:{value}')

num(1, 2, a=3, b=4)