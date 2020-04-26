#for循环
names=['ynn','sbl','yll']
for name in names:
 print(name)

names = ['ynn', 'sbl', 'yll']
for name in names:
 print(name.title()+", he/she is handsome/beautiful!")
 print("I want to see you "+name.title()+".\n")
print("Thank you very much!")
#缩进
#习题
eats=['KFC','Kingbuger','Mcdonald']
for eat in eats:
    print(eat)
    print("I like "+eat.title()+".")
print("I really like eat food")
#创建数值列表
for value in range(1,3):
    print(value)
number=list(range(1,15,3))
print(number)

figure=[]
for value in range(1,5):
    figure.append(value**3)
print(figure)

digits=[0,1,3,4,6,7,8]
min(digits)
print(str(min(digits)))
#列表解析
figure=[value**2 for value in range(1,5)]
print(figure)
#习题
for value in range(1,21):
 print(str(value))

number=list(range(1,101))
print(str(number))
for value in range(1,101):
    print(value)

number = list(range(1, 101))
min(number)
max(number)
sum(number)
print(str(min(number)))
print(str(max(number)))
print(str(sum(number)))

number=list(range(1,20,2))
print(number)
for value in range(1,20,2):
    print(str(value))

number=[]
for value in range(1,10):
 number.append(value*3)
print(number)

number=[]
for value in range(1,10):
 number.append(value**3)
print(number)
#简化
number=[value**3 for value in range(1,10)]
print(number)

for value in range(1,10):
 print(value)
#切片
name=['ynn','sbl','yll','ym']
print(name[0:1])
print(name[1:4])
print(name[:1])
print(name[3:])
print(name[-2:])
#遍历切片
names=['ynn','sbl','yll','ym']
print("They are the best friends:")
for name in names[:2]:
    print(name.title())
#复制列表
#习题
names=['ynn','sbl','yll','ys','ym']
print(names[0:1])
print("The first three items in the list are:")
name=names[:3]
print(name)
print("The first three items in the list are:")
name=names[1:4]
print(name)
print("The first three items in the list are:")
name=names[-3:]
print(name)

eats=['KFC','Kingbuger','Mcdonald']
eat=eats[:]
eats.append('hls')
eat.append('jlzj')
print("I really like eat food are:")
print(eats)
print("I really like eat food are:")
print(eat)

eats=['KFC','Kingbuger','Mcdonald']
eats.append('hls')
print("I really like eat food are:")
for eats_1 in eats:
    print(eats_1)

eats=['KFC','Kingbuger','Mcdonald']
eat=eats[:]
eats.append('hls')
eat.append('jlzj')
print("I really like eat food are:")
for eat_1 in eat:
    print(eat_1)

#元组
tuples=(1,2)
print(tuples[0])
print(tuples[1])

tuples=(1,2,4,6,8,3)
for tuple in tuples:
    print(tuple)

tuples=(1,2,4,6,8,3)
print("Original tuples:")
for tuple in tuples:
    print(tuple)
tuples=(10,20,30)
print("\nModified tuples:")
for tuple in tuples:
    print(tuple)
#习题:与元素是数字有区别，加撇号
meals=('rice','corn','apple','noddle','bread')
for meal in meals:
    print(meal)
meals = ('rice', 'banana', 'apple', 'tea', 'bread')
print("\nnew_meals:")
for meal in meals:
    print(meal)

