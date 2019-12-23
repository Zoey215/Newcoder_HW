def dealStr(string):
    alpha1 = []
    for i in string:
        if i.isalpha():
            alpha1.append(i)
    alpha2 = sorted(alpha1, key=str.upper)

    j = 0
    L = list(string)
    for i in range(len(L)):
        if L[i].isalpha():
            L[i] = alpha2[j]
            j += 1
    L = ''.join(L)
    print(L)


while True:
    try:
        string = input('')
        dealStr(string)
    except:
        break