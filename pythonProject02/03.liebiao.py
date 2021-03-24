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