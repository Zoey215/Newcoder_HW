while True:
    try:
        a = list(input())
        a = sorted(a, reverse=True) #先将输入按照字母表倒叙排列
        a = sorted(a, key=lambda x: a.count(x)) #再按照字母出现次数从高到低排列
        b = list(set(a))
        b = sorted(b, key=a.index) #列表去重，并且按照已经处理好的顺序排列
        b.reverse() #把列表倒过来输出字符串即可
        print(''.join(b))
        # print(len(b))
    except:
        break