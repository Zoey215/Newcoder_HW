while True:
    try:
        n = int(input())
        a = n ** (1.0/3)
        print(round(a, 1))
    except:
        break
