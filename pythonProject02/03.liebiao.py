'''
# 列表
bi = ['adf','bfgh','cfhf','dgjg']
print(bi[0].title())
print(bi[1].upper())
# 输出最后一个元素
print(bi[-1])

message = "hello " + bi[2] + " I'm Hrt"
print(message)

print(bi)
# 修改列表中的值
bi[0] = 'hrt'
print(bi)


# 在列表末尾添加元素 123
bi2 = ['adf','bfgh','cfhf','dgjg']
bi2.append('123')
print(bi2)

# 在空列表中添加元素
liebiao = []
liebiao.append('hrt')
liebiao.append('dashaibi')
print(liebiao)
# 在列表中添加元素
bi2 = ['adf','bfgh','cfhf','dgjg']
bi2.insert(1,'hrtdashuaibi')
print(bi2)
# 在列表中删除元素
bi2 = ['adf','bfgh','cfhf','dgjg']
del bi2[0]
print(bi2)

# 弹出值，这个值还能继续用，可以指定索引
motor =['honda','yamaha','suzuki']
print(motor)
tanchu = motor.pop()
print(motor)
print(tanchu)

# 指定名称删除列表值
motor =['honda','yamaha','suzuki']
ya = 'honda'
motor.remove(ya)
print(motor)
print(ya)
'''

# 练习
canzhuo = []
canzhuo.insert(0,'hrt')
canzhuo.insert(1,'zmy')
canzhuo.append('jay')
prople = ','.join(canzhuo)
print('以下几位同学'+prople+'有饭吃')
print('临时通知，餐桌没到，只能邀请两位同学过来吃饭了……')
bunenglai = canzhuo.pop()
print('很抱歉'+bunenglai+'你不能来了')
print('欢迎'+canzhuo[0]+'与我共进晚餐')
print('欢迎'+canzhuo[1]+'与我共进晚餐')
print('共邀请了'+str(len(bunenglai)) + '人')

del canzhuo[:]#清空整个列表
print(canzhuo)

'''
# 删除列表中所有重复的元素
motor =['honda','yamaha','suzuki','honda','honda']
for de in motor:
     if de == 'honda':
         motor.remove('honda')
print(motor)


# 永久排序
motor =['honda','yamaha','suzuki']
motor.sort()
print(motor)
motor.sort(reverse=True)
print(motor)
# 排序一次
print('排序一次')
print(sorted(motor))
print(motor)
print(motor)
# 倒序
motor =['honda','yamaha','suzuki']
print('字母adc顺序的倒序')
print(motor)
mo = sorted(motor,reverse=True)
print(mo)


# 倒着列表的顺序打印列表
motor =['chonda','ayamaha','bsuzuki']
print(motor)
motor.reverse()
print(motor)
#回复原来的顺序
motor.reverse()
print(motor)


# 确定列表的长度
motor =['chonda','ayamaha','bsuzuki']
print(len(motor))


# 练习1
ly = ['beij','shangh','shenz','changs','hangz']
print(ly)
print(sorted(ly))#按字母顺序打印
print('核实……')
print(sorted(ly))
print('________________________')
print(sorted(ly,reverse=True)) #按字母相反打印
print('核实2……')
print(sorted(ly,reverse=True))
print('恢复1')
ly.reverse()#方法reverse()永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，为此只需对列表再次调用reverse()即可。
print(ly)
print('恢复2')
ly.reverse()
print(ly)
ly.sort(reverse=True)
print(ly)
'''
