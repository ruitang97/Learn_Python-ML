'''
生成如下列表 [[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8],[0,3,6,9,12]]
第一个想到的就是for循环嵌套
① for循环可以用于生成一层列表
② 多层列表（嵌套）肯定是使用for循环嵌套实现
'''
list1 = []
# i = 0
# i = 1
for i in range(4):
    temp = []
    for j in range(5):
        temp.append(i * j)
    list1.append(temp)
print(list1)

# 另外一种写法（推导式）
# 推导式 => 可以优化 => for循环、for循环...if结构、for循环嵌套
list2 = [[i * j for j in range(5)] for i in range(4)]
print(list2)