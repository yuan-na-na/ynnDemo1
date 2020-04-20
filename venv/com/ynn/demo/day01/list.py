#【列表】，索引从0开始表示第一个列表元素，-1表示倒数第一个列表元素
name=['ynn','sbl','yll','ym','lh']
print(name[0])
print(name[4])
print(name[0].title())
print(name[-2])
name=['ynn','sbl','yll','ym','lh']
message="My name is "+name[0].title()+'.'
print(message)
name=['ynn','sbl','yll','ym','lh']
print(name)
name[0]='袁娜娜'
print(name)
#append（）在列表添加元素
name=['ynn','sbl','yll','ym','lh']
print(name)
name.append('袁娜娜')
print(name)
#insert（）列表插入元素
name=['ynn','sbl','yll','ym','lh']
print(name)
name.insert(1,'袁娜娜')
print(name)
#del语句删除元素
name=['ynn','sbl','yll','ym','lh']
print(name)
del name[2]
print(name)
#pop()删除元素,删除列表最后一个元素或者任意元素
name=['ynn','sbl','yll','ym','lh']
print(name)
popped_name=name.pop()
print(name)
print(popped_name)
name=['ynn','sbl','yll','ym','lh']
print(name)
popped_name=name.pop(0)
print(name)
print(popped_name)
#remove()根据值删除列表元素
name=['ynn','sbl','yll','ym','lh']
print(name)
So_beautiful='ynn'
name.remove(So_beautiful)
print(name)
print(So_beautiful.title()+" is a so besutiful girl.")
#第三章习题
dinner_people=['袁娜娜','岳玲玲','张昀','于敏','于爽','翟晶晶']
print("我将邀请"+dinner_people[0]+"共进晚餐。")
no_time='岳玲玲'
dinner_people.remove(no_time)
dinner_people.insert(1,'宋丙龙')
print(dinner_people)
print("我将邀请"+dinner_people[0]+"共进晚餐。")
print("我将邀请"+dinner_people[1]+"共进晚餐。")
print("我将邀请"+dinner_people[2]+"共进晚餐。")
print("我将邀请"+dinner_people[3]+"共进晚餐。")
print("我将邀请"+dinner_people[4]+"共进晚餐。")
print("我将邀请"+dinner_people[5]+"共进晚餐。")
dinner_people=['袁娜娜','岳玲玲','张昀','于敏','于爽','翟晶晶']
dinner_people.insert(0,'李行')
print(dinner_people)
dinner_people.append('袁存发')
print(dinner_people)
print("我将邀请"+dinner_people[-2]+"共进晚餐。")
message='only two people can invite'

dinner_people=['袁娜娜','岳玲玲','张昀','于敏','于爽','翟晶晶']
popped_dinner_people=dinner_people.pop()
popped_dinner_people=dinner_people.pop()
popped_dinner_people=dinner_people.pop()
popped_dinner_people=dinner_people.pop()
print(dinner_people)
del dinner_people[0]
print(dinner_people)
del dinner_people[0]
print(dinner_people)
#组织列表
alphabet=['b','d','g','q','m']
alphabet.sort()
print(alphabet)
alphabet.sort(reverse=True)
print(alphabet)

alphabet=['b','d','g','q','m']
print('original list:')
print(alphabet)
print('sorted list:')
print(sorted(alphabet))
print('original list again:')
print(alphabet)

alphabet=['b','d','e','a','c']
print(alphabet)
alphabet.reverse()
print(alphabet)

alphabet=['b','d','e','a','c']
len(alphabet)
print(str(len(alphabet)))

place=['beijing','shanghai','gongzhou','shenzhen']
print(place)
print(sorted(place))
print(sorted(place))
# place.sorted(reverse=True)
print(place)