#定义函数
def greet_user():
    """显示简单的问候语"""
    print("Hello!")
greet_user()
def greet_user():
    print("你好!")
greet_user()
#向函数传递信息
#实参和形参
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, "+username.title()+"!")
greet_user('jesse')
#结合使用函数和while循环
def get_formatted_name(first_name,last_name):
    """返回简洁的姓名"""
    full_name=first_name+" "+last_name
    return full_name.title()
#这是有个无限循环
while True:
    print("\nPlease tell me your name:")
    f_name=input("first_name")
    l_name=input("last_name")
    formatted_name=get_formatted_name(f_name,l_name)
    print("\nHello, ",+formatted_name+"!")
#停止循环
def get_formatted_name(first_name,last_name):
    """返回简洁的姓名"""
    full_name=first_name+" "+last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quite)")
    f_name=input("first_name")
    if f_name=='q':
        break
    l_name=input("last_name")
    if l_name=='q':
        break
    formatted_name=get_formatted_name(f_name,l_name)
    print("\nHello, ",+formatted_name+"!")

