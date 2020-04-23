#删除包含特性值的所有列表元素

pets=['cat','dog','cat','rabbit','dog','cat']
print(pets)
while 'cat'in pets:
    pets.remove('cat')
print(pets)

#传递实参
#位置实参
def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+" 's name is "+pet_name.title()+".")
describe_pet('hamster','harry')

