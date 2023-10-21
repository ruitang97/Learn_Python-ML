'''
把列表`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`中的每个元素都加100，生成一个新列表
'''
# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = []
# for i in list1:
#     list2.append(i + 100)
# print(list2)

# 推导式
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [i + 100 for i in list1]
print(list2)