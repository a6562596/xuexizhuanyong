list = ['aaabbabbc','badaabbabcab']
a = ",".join(list)
count = 0

def replaceAB(a,count):
    if 'ab' in a:
        a = a.replace("ab","")
        count = (count + 1)
        print('第'+str(count)+'次判断是否还存在ab时替换的结果：'+a)
        replaceAB(a,count)
    else: # a 里面没有'ab'了就要执行else
        global b
        b = a

replaceAB(a,count)
print('最终结果：'+b)