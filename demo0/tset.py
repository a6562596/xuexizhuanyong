
list = ['aaabbabbc','badaabbabcab']
a = ",".join(list)
count = 0


def replaceAB(a,count):
    if 'ab' in a:
        c = a.replace("ab","")
        count = (count + 1)
        print('第'+str(count)+'次判断是否还存在ab时替换的结果：'+c)
        replaceAB(c,count)
    else: # a 里面没有'ab'了就要执行else
        b = a
        print('结果 '+b+' 不满足判断条件了,获取最终结果，执行了：'+str(count)+'次')


print()















list = ['aaabbabbc','badaabbabcab']
str = ' '.join(list)
count = 0

def re(str,count):
    if 'ab' in str:
        a = str.replace("ab","")
        count = count+1
        print("处理次数："+count.__str__()+" 结果："+a)
        re(a,count)
    else:
        global b1
        b1 = str

re(str,count)
print(b1)