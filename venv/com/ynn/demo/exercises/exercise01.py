#习题 第六章
person={
    'first_name':'yuan',
    'last_name':'nana',
    'age':25,'city':'shanghai',
    }
print(person)
print(person['city'])
print(person['age'])

people={
    'yuannana':{
        'first_name':'yuan',
        'last_name':'nana',
        'age':25,
        'city':'shanghai',
    },
    'songbinglong':{
        'first_name':'song',
        'last_name':'binglong',
        'age':26,
        'city':'shanghai',
    },
    'yuancunfa':{
        'first_name':'yuan',
        'last_name':'cunfa',
        'age':17,
        'city':'heze',
    },

}
for peoplename,people_info in people.items():
    print("/nPeoplename: "+peoplename)
    fullname=people_info['first_name']+" "+people_info['last_name']
    age=people_info['age']
    city=people_info['city']
    print("\tFullname: "+fullname.title())
    print("\tAge: "+str(age))
    print("\tCity: "+city.title())
# 习题 第七章
# cars_type=input("What kind of car would you like to rent?")
#cars_type=subaru
#print("Let me see if I can find you a "+cars_type.title()+".")

#熟食店
print("牛肉味买完了")
sandwich_orders=['鸡肉味','牛肉味','猪肉味']
finished_sandwiches=[]
for sandwich_order in sandwich_orders:
    print("I made your "+sandwich_order.title()+" sandwich.")
while sandwich_orders:
    chioced_sandwich=sandwich_orders.pop()
    finished_sandwiches.append(chioced_sandwich)
    while "牛肉味" in finished_sandwiches:
        finished_sandwiches.remove('牛肉味')
print(finished_sandwiches)

#第八章
def display_message():
    print("本章学习函数")
display_message()

def favorite_book(title):
    print("One of my favorite book is "+ title.title()+".")
favorite_book("Alice in wonderland")

def make_shirt(size,type):
    print("Shirt size is "+size+" and type is "+type+".")
make_shirt('27','short')

def make_shirt(size,type='I love Python'):
    print("Shirt size is "+size+" and type is "+type.title()+".")
make_shirt(size='big')
make_shirt(size='middle')
make_shirt(size='20')

def describe_city(city_name,contry):
    print(city_name+" is in "+contry+".")
describe_city('Reykjavik','Iceland')

def describe_city(city_name,contry='china'):
    print(city_name+" is in "+contry+".")
describe_city(city_name='beijing')
describe_city(city_name='shanghai')
describe_city(city_name='jinan')

def city_country(city_name,country_name):
    print(city_name+", "+country_name)
city_country('Santiago','Chile')
city_country('Shanghai','China')
city_country('Heze','China')

def make_ablum(singer,ablum,number=''):
    a={'name':singer,'music':ablum}
    if number:
        a['number']=number
    return a
b=make_ablum('周杰伦','菊花台',number=4)
print(b)
b=make_ablum('张杰','明天过后',number=5)
print(b)
b=make_ablum('华晨宇','国王与乞丐')
print(b)

#def make_ablum(singer,ablum):
#    a={'name':singer,'music':ablum}
#    return a
#while True:
#    print("\nOne singer and his ablum:")
#    print("(enter 'q' at any time to quite)")
#    b=input("Singer: ")
#    if b=='q':
#        break
#    c=input("Ablum: ")
#    if c=='q':
#        break
#d=make_ablum(b,c)
#print(d)

def show_magicians(names):
    for name in names:
        print(name)
magiciannames=['ynn','sbl','yll']
show_magicians(magiciannames)

def make_magicians(names):
    while names:
        name=names.pop()
        print("the Great "+name)
        nowname.append(name)
magiciannames=['ynn','sbl','yll']
nowname=[]
make_magicians(magiciannames)

#三明治
def make_sandwich(*toppings):
    print("\nThe sandwich with the following toppings:")
    for topping in toppings:
        print("+ "+topping)
make_sandwich("egg")

def make_sandwich(toppingnumber,*toppings):
    print("\nThe sandwich with "+str(toppingnumber)+" sandwich with the following toppings:")
    for topping in toppings:
        print("+ "+topping)
make_sandwich(3,'egg')
make_sandwich(2,'bread','tomato','egg')

def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切信息"""
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('yuan','nana',age='25',location='shanghai',field='physics')
print(user_profile)
#汽车
def make_car(manufacturer,modle,**car_info):
    car={}
    for key,value in car_info.items():
        car[key]=value
    return car
uesr_car=make_car('subaru','outback',color='bule',tow_package='Ture')
print(uesr_car)
#三明治
def make_sandwich(*toppings):
    print("\nThe sandwich with the following toppings: ")
    print(toppings)
make_sandwich("egg")