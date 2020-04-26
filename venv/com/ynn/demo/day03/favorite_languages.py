#一个键关联多个值，可以在字典中嵌套一个列表，遍历用for循环
favorite_lanuages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}
for name,languages in favorite_lanuages.items():
    print("\n"+name.title()+"'s favorite_languages are:")
    for language in languages:
        print("\t"+language.title())
