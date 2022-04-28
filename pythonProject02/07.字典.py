'''
1. 一个简单的字典（键值对）
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

2. 键赋值概念
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

3.字典练习
#用一个字典储存人的信息
info_list = {
    'name':'何润田',
    'age':'24',
    'city':'深圳',
}

number_list = {
    'hrt':'2',
    'jaychou':'7',
    '萨斯给':'1',
}
print(number_list)

cihui_list = {
    'for':'循环',
    'print':'打印',
    'error':'错误',
    'coding':'编码',
}
print('for'+':'+cihui_list['for']+'\n'
      'print'+':'+cihui_list['print']+'\n'
      'error'+':'+cihui_list['error'])

# 循环打印字典中的键和值
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key,value in user_0.items():
    print("key:"+key)
    print("value:"+value+'\n')

#打印每一条和河流的名称
heliu_list = {
    'nile':'egypt',
    'huanghe':'china',
    'mixixibihe':'usa',
}
for key,value in heliu_list.items():
    print("The Nile runs through "+key+'\n')

#打印字典中每个国家的名字
for key, value in heliu_list.items():
    print("国家的名字都有 "+value)


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + " 喜欢的语言是 " +language.title() + "。")

#根据以上字典创建一个会被接受调查的人员名单
diaocharenyuan_list = {
    'jen': 'python',
    'phil': 'python',
    'hrt':'a',
    'zmy':'b',
}
#循环会被调查人员的名单，然后对比上面的字典（favorite_languages）内容
for key,value in diaocharenyuan_list.items():
    if key in favorite_languages:
        print("谢谢你"+key+"参与我们的调查")
    else:
        print(key+"辛苦您来参加我们的调查！")
'''


# 嵌套（需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套）
