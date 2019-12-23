while True:
    try:
        s = input().split(';')
        x = 0
        y = 0
        for i in s:
            if len(i) < 2 or len(i) > 3 or not i[1:].isdigit():
                continue
            if i[0] == 'A':
                x -= int(i[1:])
            if i[0] == 'D':
                x += int(i[1:])
            if i[0] == 'W':
                y += int(i[1:])
            if i[0] == 'S':
                y -= int(i[1:])
        print(str(x)+','+str(y))
    except:
        break
