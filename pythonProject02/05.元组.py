# 元组里面的元素是不可修改的
foods = ('皮皮虾','橙子','冰淇淋','牛排','可乐')
for food in foods:
    print(food)

print()
#foods[0] = '小龙虾'
#print(foods)

foods = ('小龙虾','橙子','牛肚','牛排','可乐') # 用变量赋值的方式来修改元组
for food2 in foods:
    print(food2)
