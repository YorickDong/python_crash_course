alien_0 = {'color':'green',
           'points':5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
print(alien_1)
alien_1['color'] = 'yellow'     #在已有键值对的情况 再次赋值，就是修改。
print(alien_1)

print("Alien_0 original X position ： " + str(alien_0['x_position']))
alien_0['speed'] = 'medium'
if alien_0['speed'] == 'slow':
    x_increase = 1
elif alien_0['speed'] == 'medium':
    x_increase = 2
elif alien_0['speed'] == 'fast':
    x_increase = 3
alien_0['x_position'] = alien_0['x_position'] + x_increase
print("Alien_0 current X position ： " + str(alien_0['x_position']))
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_language  = {
    'Ashley':'SQL',
    'Yorick':'Python',
    'chen':'hadoop',
    'dong':'Java',
    }
print("Ashley's favorite language is " + favorite_language['Ashley'] + '.')

#6-1 人
informations = {
    'first_name':'Ashley',
    'last_name':'Chen',
    'age':24,
    'city':'Shanghai',
    }
print(informations)

dictionary = {
    'del':'删除',
    'append':'列表尾部添加',
    'pop':'弹出',
    'remove':'根据值删除',
    }







