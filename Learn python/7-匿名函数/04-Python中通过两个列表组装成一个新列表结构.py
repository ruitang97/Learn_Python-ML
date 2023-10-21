'''
已知:list1 = ["A","B","C"], list2 = ["X","Y","Z"]
使用列表推导式生成['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
'''
list1 = ["A","B","C"]
list2 = ["X","Y","Z"]

list3 = []
for i in list1:
    for j in list2:
        list3.append(i+j)
print(list3)

newlist = [i + j for i in list1 for j in list2]
print(newlist)