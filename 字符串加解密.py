while True:
    try:
        A = input()
        B = input()
        newA = ''
        newB = ''
        for i in A:
            if i.isupper():
                if i != 'Z':
                    newA += chr(ord(i) + 1).lower()
                else:
                    newA += 'a'
            elif i.islower():
                if i != 'z':
                    newA += chr(ord(i) + 1).upper()
                else:
                    newA += 'A'
            elif i.isdigit():
                if i != '9':
                    newA += chr(ord(i) + 1)
                else:
                    newA += '0'
        for i in B:
            if i.isupper():
                if i != 'A':
                    newB += chr(ord(i) - 1).lower()
                else:
                    newB += 'z'
            elif i.islower():
                if i != 'a':
                    newB += chr(ord(i) - 1).upper()
                else:
                    newB += 'Z'
            elif i.isdigit():
                if i != '0':
                    newB += chr(ord(i) - 1)
                else:
                    newB += '9'
        print(newA)
        print(newB)
    except:
        break