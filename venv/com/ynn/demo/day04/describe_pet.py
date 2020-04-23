#调用函数多次
def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+" 's name is "+pet_name.title()+".")
describe_pet('hamster','harry')
describe_pet('dog','willie')
#关键字实参
def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+" 's name is "+pet_name.title()+".")
describe_pet(animal_type='hamster',pet_name='harry')
#默认值
def describe_pet(pet_name,animal_type='dog'):
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+" 's name is "+pet_name.title()+".")
describe_pet(pet_name='willie')