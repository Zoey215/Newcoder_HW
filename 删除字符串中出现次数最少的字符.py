while True:
    try:
        s = input()
        res = []
        n = ''
        for i in range(len(s)):
            res.append(s.count(s[i]))
        for i in range(len(s)):
            if res[i] != min(res):
                n = n + s[i]
        print(n)
    except:
        break
