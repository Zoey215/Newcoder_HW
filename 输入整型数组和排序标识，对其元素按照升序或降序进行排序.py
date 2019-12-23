while True:
    try:
        n = input()
        s = input().split()
        i = input()
        s = list(map(int, s))
        s.sort()
        if i != '0':
            s.reverse()
        s = map(str, s)
        print(' '.join(s))
    except:
        break
