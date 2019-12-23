while True:
    try:
        s = input().split()
        p = []
        n = []
        for i in s:
            if int(i) < 0:
                n.append(int(i))
            else:
                p.append(int(i))
        print(len(n))
        if p:
            print(round(sum(p)/len(p), 1))
        else:
            print('0.0')
    except:
        break
