#第六章dictionaries字典
people={'color':'red','years':'25'}
print(people['color'])
print(people['years'])

people={'color':'red','years':25}
new_years=people['years']
print("Iam "+str(new_years)+" old!")
people={'color':'red','years':'25'}
new_years=people['years']
print("Iam "+new_years+" old!")

alien_0={'color':'green','points':5}
print(alien_0)
alien_0['x-position']=0
alien_0['y-position']=25
print(alien_0)

alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

alien_0={'color':'green'}
print("The alien is"+alien_0['color']+".")
alien_0['color']='yellow'
print("The alien is now "+alien_0['color']+".")
#修改字典里的值
alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Original x_position: "+str(alien_0['x_position']))
#向右移动外星人，据当前速度的大小为移动的距离
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
#变量越大说明外星人移动越快，fast
    x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print("New x_position: "+str(alien_0['x_position']))
#del语句删除键-值对
alien_0={'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)
#习题
person={
    'first_name':'yuan',
    'last_name':'nana',
    'age':25,'city':'shanghai',
    }
print(person)
print(person['city'])
print(person['age'])
#遍历字典
person={
    'first_name':'yuan',
    'last_name':'nana',
    'age':'25',
    'city':'shanghai',
    }
#声明两个变量，存储键key与值value,items表示方法;
for key,value in person.items():
    print("\nkey: "+key)
    print("value: "+value)
#遍历所有的键与值
person={
    'first_name':'yuan',
    'last_name':'nana',
    'age':'25',
    'city':'shanghai',
    }
for things in person.keys():
    print(things.title())
for things in person.values():
    print(things.title())
for things in person:
    print(things.title())
#顺序遍历所有的键
favorite_languages={
    'ynn':'python',
    'yll':'c',
    'sbl':'android',
    'ym':'c',
}
for name in sorted(favorite_languages.keys()):
    print(name.title()+", thank you taking the poll!")
#遍历值+集合（去重复）
favorite_languages={
    'ynn':'python',
    'yll':'c',
    'sbl':'android',
    'ym':'c',
}
for language in set(favorite_languages.values()):
    print(language.title())
#习题
rivers={'huanghe':'china',
       'niluo':'india',
       'nile':'egypt',
}
print("The "+"huanghe"+" runs through "+rivers['huanghe'].title()+".")
print("The "+"niluo"+" runs through "+rivers['niluo'].title()+".")
print("The "+"nile"+" runs through "+rivers['nile'].title()+".")
rivers={'huanghe':'china',
       'niluo':'india',
       'nile':'egypt',
}
for river in rivers.keys():
    print( river.title())
for nation in rivers.values():
    print(nation.title())
