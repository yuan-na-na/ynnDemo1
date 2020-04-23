#在列表之间移动元素

#首先创建一个待验证用户的列表
#再创建一个用于储存已验证用户的空列表
unconfirmed_users=['alice','brain','candace']
confirmed_users=[]
#验证每个用户直到没有未验证用户为止
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print("Verifying user: "+current_user.title())
# 将每个经过验证的列表都移到已验证用户的列表中
    confirmed_users.append(current_user)
#显示所有已验证用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())