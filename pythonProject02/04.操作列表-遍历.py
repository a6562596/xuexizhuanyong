'''
# 遍历
magics = ['ailce','david','carolina']
for magic in magics:
    print(magic.title(),"他们的魔术太精彩了！！！")
    print("真是期待"+magic+"的下一次表演\n")
print("Thank you!")

# range快速生成一段数字
for value in range(1,6):
    print(value)

# 生成1 - 6的数字转化成列表
lists = list(range(1,7))
print(lists)

lists = list(range(2,100,2))#range(从2开始，不超过100，2次递增)
print(lists)

# 计算1-10的平方，并存进列表
liebiao = []
for pingfangs in range(1,11):
    liebiao.append(pingfangs ** 2)
print(liebiao)
print(min(liebiao))
print(max(liebiao))
print(sum(liebiao))

# 列表解析   声明计算立方  for循环给表达式p**3提供值
liebiaos = [p ** 3 for p in range(1,11)]
print(liebiaos)


# 练习
# 打印1-20
for sum1 in range(1,21):
    print(sum1)

# 1-100w存入列表
liebiao = []
for sums in range(1,1000001):
    liebiao.append(sums)
print(liebiao)
print(min(liebiao))
print(max(liebiao))
print(sum(liebiao))

# 1-20奇数
liebiao = []
for qishu in range(1,20,3):
    liebiao.append(qishu)
print(liebiao)

# 能被3整除
liebiao = []
for zhegnchu in range(3,30,3):
    liebiao.append(zhegnchu)
print(liebiao)

# 立方
liebiaos = []
for lifang in range(1,11):
    liebiaos.append(lifang ** 3)
print(liebiaos)

# 立方解析列表
liebiaos = [lifang ** 3 for lifang in range(1,11)]
print(liebiaos)
'''


# 切片
players = ['charles','martina','michael','florence','eli']
print(players[2:4]) # [:3] 不指定从哪开始就从最前面开始  反之。 负数从后开始

# 只遍历前三个
qies = players[0:3]
for qie in qies:
    print(qie.title())

my_pl = players[:]
print(my_pl)
players.append('hrt')
print(players)
print()
my_pl.append('zmy')

print(players)
print(my_pl)
for mys in my_pl:
    print(mys)

