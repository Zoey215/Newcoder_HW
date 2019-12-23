while True:
    try:
        s = int(input())
        if s in range(1, 3):
            print(1)
        else:
            l = [1, 1]
            x = s-2
            while x > 0:
                l.append(l[-1]+l[-2])
                x -= 1
            print(l[-1])
    except:
        break