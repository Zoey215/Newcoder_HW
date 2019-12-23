while True:
    try:
        n = int(input())
        total = n*2 + n*(n-1)*3//2
        print(total)
    except:
        break