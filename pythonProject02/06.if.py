'''
# 循环列表每一个元素，判断
cars = ['va','bwm','linkco','benchi']
for car in cars:
    if car == 'bwm':
        print(car.upper())#字母全部大写
    else:
        print(car.title())#首字母大写

# 临时笔记
car = 'audi'  这个是给car变量赋值
car == 'bmw'  这个是：变量car的值是bmw吗？

# python中变量值比较区分大小写
car = 'Audi'
car2 = 'audi'
car3 = car.lower()
print(car2 == car3)


str1 = 'hrt'
str2 = 'Hrt'
str3 = 'zmy'
print(str1 == str2.lower())
print(str1 == str2)

print()

sum1 = 20
sum2 = 15
sum3 = 15
print(sum2 == sum3)#相等
print(sum1 != sum2)#不等
print(sum1 > sum2)#大于
print(sum2 < sum1)#小于
print(sum2 >= sum3)#大于等于
print(sum2 <= sum3)#小于等于

print(sum2 == sum3 and sum1 != sum2)#and：都要满足
print(sum2 == sum3 or sum1 == sum2)#or：只要一个满足

liebiao = [1,2,3,4,5,6]
if 1 in liebiao:
    print('1在列表中')

if 7 not in liebiao:
    print('7不在列表中')


# 练习1 射杀外星人
alien_color = 'green'
if alien_color == 'green':
    print("恭喜你，获得5分")

if alien_color != 'green':
    print()

alien_color = 'red'
if alien_color == 'red':
    print("射杀外星人为红色 获得5分")
else:
    print("射杀外星人不是红色的未得分")

alien_color2 = 'red'
if alien_color2 != 'red':
    print("射杀外星人不是红色，未得分")
else:
    print("恭喜，杀死外星人为绿色，获得10分")


alien_color = 'green'
if alien_color == 'green':
    print("恭喜你获得5分！")
elif alien_color == 'yellow':
    print("恭喜你获得10分")
elif alien_color == 'red':
    print("恭喜你获得15分")


# 练习2 人生的不同阶段
age4 = 18 # 青少年
if age4 == 3:
    print("蹒跚学步中")
elif age4 == 12:
    print("你还是一名儿童")
elif age4 >= 18:
    print("你已经是一名青少年了")
elif age4 == 40:
    print("成年人")
else:
    print("老年人")
'''

#练习3
usrs = ['admin','hrt','zmy','jay']
usrs2 = []
for usr in usrs:
    print(usr+'你好')
    if 'admin' in usr:
        print("Hello,admin\n")
    else:
        print("Hello "+usr+",than you for logging in again")
if not usrs2:
    print("这个列表是空的")