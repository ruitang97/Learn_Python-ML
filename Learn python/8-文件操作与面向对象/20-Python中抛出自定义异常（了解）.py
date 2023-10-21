'''
在Python中，抛出自定义异常的语法为`raise 异常类对象`。
需求：密码长度不足，则报异常（用户输入密码，如果输入的长度不足6位，则报错，即抛出自定义异常，并捕获该异常）。
'''
def input_password():
    # 1、提示用户输入一个密码
    password = input('请输入您的密码（要求密码长度不能低于6位）：')
    # 2、判断密码长度是否小于6位
    if len(password) < 6:
        # print('您输入的密码长度小于6位，请重新输入！')
        raise Exception('您输入的密码长度小于6位，请重新输入！')
        return

input_password()