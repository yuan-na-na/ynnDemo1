#在字典中嵌套字典
users={
    'aeinstein':{
        'first':'elbert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}
for username,user_info in users.items():
    print("\nUsername: "+username)
    full_name=user_info['first']+" "+user_info['last']
    location=user_info['location']
    print("\tFullname: "+full_name.title())
    print("\tLocation: "+location.title())
