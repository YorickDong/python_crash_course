magecians = ['alice', 'david', 'carolina']
for magecian in magecians:
    print(magecian.title())
    print(magecian.title() + ', that was a great trick!\n')
print('I hope to see your trick again, ' + magecian.title())

#
# 4-1 披萨
my_pizzas = []
my_pizzas.append('pepperoni pizza')
my_pizzas.append('seafood pizza')
my_pizzas.append('cheese pizza')
for pizza in my_pizzas:
    print(pizza)
    print('I like '+ pizza + '.')
    print('I can\'t like ' + pizza + ' anymore!\n')
print('I really love pizza!\n')

#4-2 动物
animals = []
animals.append('dog')
animals.append('cat')
animals.append('pig')
for animal in animals:
    print(animal)
    print('A ' + animal + ' would make a great pet!\n')
print('Any of these animals would make a great pet!')

# 4.3.1 range()
for value in range(1,101):
    print(value)
numbers = list(range(1,11))  # 1-10所有整数
print(numbers)

even_numbers = list(range(2,11,2)) # 1-10所有偶数  从2开始 每个加2
print(even_numbers)

# 将1-10的平方放到列表中
squares = []
for value in range(1,11):
    #square = values**2
    squares.append(value**2)
print(squares)
print(sum(squares)) #打印总和
print(max(squares)) #打印最小
print(min(squares)) #打印最大

squares = [value**2 for value in range(1,11,2)]
print(squares)

# 4-3 数到20
for number in range (1,21):
    print(number)

#4-4 1000000
numbers = [number for number in range(1,11)]   # number是表达式 后面的for循环是给表达式赋值
print(numbers)

# 4-5 1-1000000 总和
print(sum(numbers))
print(max(numbers))
print(min(numbers))
#4-6 奇数
odd_numbers = [odd_number for odd_number in range(1,20,2)]
print(odd_numbers)
#4-7 3的倍数
three_times = [three_time for three_time in range(3,31,3)]
print(three_times)
#4-8
cubes=[]
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
print(cubes)
# 4-9 用列表解析算立方
cubes = [cube**3 for cube in range(1,11)]
print(cubes)
#print(cubes[3])  访问cubes列表中第四个

#4.4.1 切片
print(cubes[0:3])  #起始索引0 终止索引3 所以打印0 1 2
print(cubes[1:4])  #起始索引1 终止索引4 所以打印1，2，3
print(cubes[:4])   #不写起始索引 默认从头开始0 #所以打印0，1，2，3
print(cubes[2:])   #不写终止索引 默认结束到表尾 从索引2开始。
print(cubes[-3:])  #倒数三个

# 4.4.3 复制列表
new_list = cubes[:]
print(new_list)
print("Old list is: " + str(cubes))
print("New list is: " + str(new_list))
cubes.append("666")
new_list.append("888")
print("Old list is: " + str(cubes)+"\n")
print("New list is: " + str(new_list))

#4-10 切片
shoes = ["AJ1","AJ6","AJ11","AJ13","Yeeze","Bullet"]
print("The first three items in the list are: " + str(shoes[:3]))   #前三个
print("Three items from the middle of the list are: " + str(shoes[2:5]))   #中间三个
print("The last three items in the list are: " + str(shoes[-3:]))   #后三个

#4-11 你我披萨
my_pizzas = []
my_pizzas.append('pepperoni pizza')
my_pizzas.append('seafood pizza')
my_pizzas.append('cheese pizza')
friend_pizzas = my_pizzas[:]
friend_pizzas.append('fruits_pizza')
for my_pizza in my_pizzas:
    print("My favorite pizzas are: " + my_pizza)
for friend_pizza in friend_pizzas:
    print("My friend's favorite pizzas are: " + friend_pizza)

#4-12 使用多个循环
print("\n4-12")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

for my_food in my_foods:
    print("My favorite foods are: " + my_food)

print("\n")  #会换两行 因为print() 相当于print(end="\n") 本身就换一行
             #print("\n") 就相当于print("\n",end="\n") 所以换了两行
for friend_food in friend_foods:
    print("My friend's favorite foods are: " + friend_food)

#4.5 元组
dimensions = (200,100)
stable_str = ('fa','faf')
print(dimensions[0])
print(stable_str[0])
print()
print("Original dimensions are: ")
for dimension in dimensions:
    print(dimension)
print()
dimensions = (400,50)
print("Modified dimensions are: ")
for dimension in dimensions:
    print(dimension)

#4-16 自助餐
buffets = ('meat','noodle','rice','coffee','juice')
print("This buffet provide: ")
for buffet in buffets:
    print(buffet)
#buffets[1] = "coco"   #元组不可以这样修改参数，但是可以重新赋值
print()
buffets = ('coco','noodle','water','coffee','juice')
print("Modified buffet provide: ")
for buffet in buffets:
    print(buffet)



