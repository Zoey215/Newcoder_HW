while True:
    try:
        m, n = map(int, input().split())
        s = list(map(int, input().split()))
        print(' '.join(map(str, sorted(s)[:n])))
    except:
        break
