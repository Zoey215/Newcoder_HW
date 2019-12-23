while True:
    try:
        n = int(input())
        res = []
        if n:
            res.append(n//2)
        for i in res:
            print(i)
    except:
        break