cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print()
car ='Audi'
print(car.lower() == 'audi')

#5.2.3 !=
requested_topping = 'mushroom'
if requested_topping != 'anchovy':
    print('unequal')

# 5.2.5 and
print('第一个人年龄：')
#age_0 = int(input())
age_0 = 21
print('第二个人年龄：')
#age_1 = int(input())
age_1 = 13
if age_0 > 20 and age_1 > 20:
    print("你俩都20多了")
else:
    print("还差点")
#5.2.5 or
age_2 = 23
age_3 = 15
if age_2 > 21 or age_3 > 21:
    print("至少一个大于21")
#5.2.6 判断值在列表中 in
#列表里的值都要小写的，输入的用lower与列表比较。
users = ['yorick','ashley','dong','chen']
#user = input()
user = 'Ashley'
if user.lower() in users:
    print(user + '在列表中')
else:
    print(user + '不在列表中')

#5.2.7 判断值在不列表中 not in
#列表里的值都要小写的，输入的用lower与列表比较。
users = ['yorick','ashley','dong','chen']
#user = input()
user = 'siwen'
if user.lower() not in users:
    print(user + '不在列表中')
else:
    print(user + '在列表中')



names = ['yorick', 'ashley', 'dong', 'chen']
print('''是否要新增用户： 
        1. 是
        2. 否''')
if input() == '1':
    print("请输入用户名： ")
    new_name = input()
    if new_name.lower() not in names:               #检查是否有重复用户名
        names.append(new_name)
        print("用户名 " + new_name + " 添加成功")
        print(names)
    else:
        print("该用户名已存在")
else:
    print('''是否要查看列表现有值： 
          1.是
          2.否''')
    if input() == '1':
        for name in names:
            print(name.title())
    else:
        print('再见吧！')

toppings = ['mushroom', 'extra cheese']
if 'mushroom' in toppings:
    print('Adding mushroom.')
if 'pepperoni' in toppings:
    print('Adding pepperoni.')
if 'extra cheese' in toppings:
    print('Adding extra cheese.')
print("\nFinished making your pizza.")

#5-3 外星人颜色
print("5-3")
alien_color_green = ['green', 'yellow', 'red']
if 'green' in alien_color_green:
    print("You get 5 points.")
    print()

#5-4 外星人颜色
print("5-4")
alien_color_green = ['green', 'yellow', 'red']
if 'black' in alien_color_green:
    print("You get 5 points.")
else:
    print("You get 10 points.")
    print()

#5-5 外星人颜色
print("5-5")
alien_color_green = 'green'
if alien_color_green == 'green':
    print("You get 5 points.")
elif alien_color_green == 'yellow':
    print("You get 10 points.")
elif alien_color_green == 'red':
    print("You get 15 points.")
    print()

alien_color_yellow = 'yellow'
if alien_color_yellow == 'green':
    print("You get 5 points.")
elif alien_color_yellow == 'yellow':
    print("You get 10 points.")
elif alien_color_yellow == 'red':
    print("You get 15 points.")
    print()

alien_color_red = 'red'
if alien_color_red == 'green':
    print("You get 5 points.")
elif alien_color_red == 'yellow':
    print("You get 10 points.")
elif alien_color_red == 'red':
    print("You get 15 points.")
    print()

#5-6 人生不同阶段
print("5-6")
age = 25
if age < 2:
    print("他是婴儿")
elif age <4:
    print("他正蹒跚学步")
elif age < 13:
    print("他是儿童")
elif age < 20:
    print("他是青少年")
elif age < 65:
    print("他是成年人")
elif age >= 65:
    print("他是老年人")

toppings = ['mushroom', 'extra cheese','pepperoni']
for topping in toppings:
    if topping == 'mushroom':
        print("Sorry, we are out of mushroom right now.")
    else:
        print("Adding " + topping + ".")
print()

#5.4.2 确定列表不是空的
print("5.4.2")
toppings = ['mushroom', 'extra cheese','pepperoni']
if toppings:                    #if 后面用列表名在条件表达式中，列表至少有一个元素时返回TRUE，空元素返回false。
    for topping in toppings:
        print("Adding " + topping + ".")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza.")

#5-8 特殊方式跟admin打招呼
print("5-8")
users = ['admin','yorick','ashley','chen','dong']
for user in users:
    if user.lower() == 'admin':
        print("Hello, " + user.title() + " would you like to see a status report?")
    else:
        print("Hello, " + user.title() + " thank you for logging again.")
print()

# 5-9 处理没有用户的情形
print("5-9")
users1 = []
if users1:
    for user1 in users1:
        if user1.lower() == 'admin':
            print("Hello, " + user1.title() + " would you like to see a status report?")
        else:
            print("Hello, " + user1.title() + " thank you for logging again.")
else:
    print("We need to find some users!")
print()

# 5-10 检查用户名
print("5-10")
current_users = ['admin','yorick','Ashley','chen','dong']
new_users = ['youwei','Chen','ASHLEY','siwen','dyw']
for new_user in new_users:
    if new_user.lower() in [current_user.lower() for current_user in current_users]:       #后面是列表解析，
    #if new_user.lower() in current_users:
        print(new_user + "已被使用，请使用其他用户名")
    else:
        print(new_user + "未被使用")
print()

#5-11 序数
numbers = list(range(1,10))
for number in numbers:              #遍历出的每一个都是整型 不是字符串！！！！
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")

