#传递列表
def greet_users(names):
"""向列表中的每位用户都发出简单的问候"""
    for name in names:
        message="Hello, "+name.title()+"!"
        print(message)
usernames=['ynn','sbl','yll']
greet_users(usernames)