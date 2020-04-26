#将列表存储在字典中
#存储pizza的信息
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
#概述多点的pizza
print("You order a "+pizza["crust"]+"-crust pizza"+"with the following topppings:")
for topping in pizza['toppings']:
    print("\t"+topping)

#函数===传递任意数量的实参
def make_pizza(*toppings):
    print(toppings)
make_pizza('mushrooms')
make_pizza('mushrooms','extra cheese')
#结合使用位置实参和任意数量的实参
def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the follow toppings:")
    for topping in toppings:
        print("- "+topping)
make_pizza(12,'mushrooms')
make_pizza(16,'mushrooms','extra cheese')