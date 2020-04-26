#嵌套
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#创建存储外星人的空列表
aliens=[]
#创建30个外星人
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
#输出前五个外星人
for alien in aliens[0:5]:
    print(alien)
#显示创建多少外星人
print("Totle number of aliens: "+str(len(aliens)))

aliens=[]
#创建
for alien_number in range(8):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
    elif alien['color']=='yellow':
        alien['color'] = 'red'
        alien['points'] = '15'
        alien['speed'] = 'fast'
for alien in aliens[:5]:
    print(alien)
#显示创建多少外星人
print("Totle number of aliens: "+str(len(aliens)))

