#if语句
foods=['kfc','kingbuger','mocdonlad','pizza']
for food in foods:
    if food=='kfc':
        print(food.upper())
    else:
        print(food.title())
#左右相等判定==
#左右不相等判定!=
food='pizza'
if food=='kfc':
    print("false")
else:
    print("ture")

foods = 'pizza'
if food != 'kfc':
    print("ture")
else:
    print("false")

age=18
if age==16:
    print("no!")
else:
    print("yes!")
age=18
if age>=12:
    print("no!")
else:
    print("yes!")
#检查多个条件and、or
age_1=5
age_2=10
if age_1>1 and age_2<9:
    print("yes!")
else:
    print("no!")
ge_1=5
age_2=10
if age_1>1 or age_2<9:
    print("yes!")
else:
    print("no!")
#检查特征值in、not in
foods=['kfc','kingbuger','mocdonlad','pizza']
if 'kfc' in foods:
    print("ture!")
else:
    print("false")
if 'rice'  not in foods:
    print("false!")
else:
    print("ture!")
#elif
number=10
if number<5:
    print("small!")
elif number>15:
    print("big!")
elif number==10:
    print("ture!")
else:
    print("no!")
#习题
alien_color=['green','yellow','red']
if 'green'in alien_color:
    print("Attain 5 pionts!")
else:
    print("Attain 10 points!")
alien_color=['green','yellow','red']
if 'blue'in alien_color:
    print("Attain 5 pionts!")
else:
    print("Attain 10 points!")
alien_color=['green','yellow','red']
if 'green'in alien_color:
    print("Attain 5 pionts!")
elif 'yellow'in alien_color:
    print("Attain 10 points!")
else:
    print("Attain 15 points!")

age=25
if age<2:
    print("he is a baby!")
elif age>=2 and age<4:
    print("he is canot run!")
elif age>=4 and age<13:
    print("he is a children!")
elif age>=13 and age<20:
    print("he is a teenager")
elif age>=20 and age<65:
    print("he is a adult")
else:
    print("he is a aged")
#if语句处理列表
users=['ynn','sbl','yll','admin','ym']
for user in users:
    if 'admin' in user:
        print("Hello Admin,would you like to see a statu report?")
    else:
        print("Hello Eric,thank you for logging in again")
users=[]
if users:
    for user in users:
        print("Hello Eric,thank you for logging in again")
else:
    print("We need to find some users!")

current_users=['ynn','sbl','yll','admin','ym']
new_users=['ynn','sb','yl','zj','ym']
for new_user in new_users:
    if new_user in current_users:
        print(new_user)
    else:
        print("the name not use")
#有问题？？？？？？
numbers=[]
for value in range(1,10):
    numbers.append(value)
print(numbers)
for number in numbers:
    if number==1:
        print("1st")
    elif number==2:
        print("2nd")
        print("3rd")
    else:
        print(str(number) + "th")


